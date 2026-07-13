#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Iniciar Rosa María Studio
=========================
Doble clic en este archivo para abrir el generador en el navegador.
Arranca un pequeño servidor local (necesario para Pexels, fotos e IA) y
abre rosa-maria-studio-2.html automáticamente.

Si el doble clic no funciona: clic derecho -> "Abrir con" -> Python.
Para cerrar: cierra esta ventana negra.
"""

import os
import sys
import socket
import threading
import webbrowser
import http.server
import socketserver
import mimetypes

# Windows a veces registra .css/.js como text/plain -> Chrome rechaza el CSS
# y la pagina sale SIN estilos. Forzamos los tipos correctos.
mimetypes.add_type("text/css", ".css")
mimetypes.add_type("text/javascript", ".js")
mimetypes.add_type("application/json", ".json")

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ARCHIVO = "rosa-maria-studio-2.html"


def puerto_libre(inicio=8000, intentos=20):
    """Devuelve el primer puerto libre a partir de `inicio`."""
    for p in range(inicio, inicio + intentos):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", p)) != 0:   # no hay nada escuchando
                return p
    return inicio


def instancia_ya_abierta(puerto=8000):
    """¿Ya hay UNA instancia de ESTA app corriendo en este puerto?
    Si abrimos una segunda instancia en OTRO puerto, el navegador la trata
    como un sitio distinto: Diseños guardados, IA usadas, etc. de la carpeta
    IndexedDB/localStorage de un puerto NO se ven en el otro -> "no se
    guardan" (en realidad se guardaron, pero en el sitio anterior).
    Por eso: si el 8000 ya sirve esta misma app, reutilizarlo siempre."""
    import urllib.request
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{puerto}/{ARCHIVO}", timeout=1) as r:
            return r.status == 200 and b"Rosa Mar" in r.read(2000)
    except Exception:
        return False


# Trabajos de reel en curso (el montaje tarda minutos y va en segundo plano)
REEL_JOBS = {}
REEL_LOCK = threading.Lock()


def _limpiar_salida(mantener=8):
    """Borra reels antiguos de reel-video/salida (deja los `mantener` más
    recientes) y los ficheros de voz temporales viejos, para que la carpeta no
    se llene. Nunca toca archivos modificados en los últimos 2 min (por si hay
    un montaje en curso)."""
    import time
    try:
        base = os.path.dirname(os.path.abspath(__file__))
        sal = os.path.join(base, "reel-video", "salida")
        if not os.path.isdir(sal):
            return
        ahora = time.time()
        reels = []
        for nombre in os.listdir(sal):
            ruta = os.path.join(sal, nombre)
            if not os.path.isfile(ruta):
                continue
            if nombre.startswith("_voz_grabada_"):        # temporales de voz
                try:
                    if ahora - os.path.getmtime(ruta) > 1800:   # > 30 min
                        os.remove(ruta)
                except OSError:
                    pass
                continue
            if nombre.lower().endswith(".mp4"):
                try:
                    reels.append((os.path.getmtime(ruta), ruta))
                except OSError:
                    pass
        reels.sort(reverse=True)                          # más nuevos primero
        borrados = 0
        for mtime, ruta in reels[mantener:]:              # todo lo que sobra
            try:
                if ahora - mtime > 120:                   # no tocar montajes recientes
                    os.remove(ruta); borrados += 1
            except OSError:
                pass
        if borrados:
            print("  [reel] limpieza: %d reel(s) antiguo(s) borrado(s)" % borrados, flush=True)
    except Exception as e:
        print("  [reel] limpieza de salida falló:", e, flush=True)


def _trabajo_reel(job, data):
    """Genera el reel en un hilo y deja el resultado en REEL_JOBS[job]."""
    try:
        ruta = generar_reel_desde_data(data)
        with REEL_LOCK:
            REEL_JOBS[job] = {"estado": "listo", "archivo": os.path.basename(ruta)}
        print("  [reel] %s listo: %s" % (job, os.path.basename(ruta)), flush=True)
        _limpiar_salida()          # deja solo los reels recientes
    except Exception as e:
        import traceback; traceback.print_exc()
        with REEL_LOCK:
            REEL_JOBS[job] = {"estado": "error", "error": str(e)}
        print("  [reel] %s ERROR: %s" % (job, e), flush=True)


def generar_reel_desde_data(data):
    """Monta un reel MP4 con reel_video.py y devuelve su ruta.
    data: {hook, sub, cta, buscar, clips[], narrar, voz, audio, subtitulos, color}."""
    import time, base64, re
    base = os.path.dirname(os.path.abspath(__file__))
    rv_dir = os.path.join(base, "reel-video")
    if rv_dir not in sys.path:
        sys.path.insert(0, rv_dir)
    import reel_video as RV

    hook = (data.get("hook") or "").strip()
    sub = (data.get("sub") or "").strip()
    cta = (data.get("cta") or "").strip()
    narrar = data.get("narrar") or None
    voz = data.get("voz") or "es-ES-ElviraNeural"
    buscar = (data.get("buscar") or "").strip()
    color = data.get("color") or "dark"
    subtitulos = bool(data.get("subtitulos"))
    transicion = data.get("transicion") or "corte"
    try:
        sombra = max(0, min(100, int(data.get("sombra", 45))))
    except Exception:
        sombra = 45

    # Música de fondo: SOLO el nombre del archivo (lo eliges en la app, ya
    # colocado a mano en la carpeta MUSICA). Sin rutas ni "..": se busca tal
    # cual dentro de esa carpeta, nunca fuera.
    musica = None
    nombre_musica = os.path.basename((data.get("musica") or "").strip())
    if nombre_musica:
        ruta_musica = os.path.join(base, "MUSICA", nombre_musica)
        if os.path.exists(ruta_musica):
            musica = ruta_musica
        else:
            print("  [reel] música no encontrada:", nombre_musica, flush=True)

    # TU voz grabada en el navegador (data URL base64 -> archivo)
    audio_voz = None
    audio_b64 = data.get("audio") or ""
    if audio_b64:
        try:
            m = re.match(r"data:audio/(\w+);base64,(.*)$", audio_b64, re.S)
            ext, crudo = (m.group(1), m.group(2)) if m else ("webm", audio_b64)
            destino = os.path.join(rv_dir, "salida", "_voz_grabada_%d.%s" % (int(time.time()), ext))
            os.makedirs(os.path.dirname(destino), exist_ok=True)
            with open(destino, "wb") as f:
                f.write(base64.b64decode(crudo))
            audio_voz = destino
            print("  [reel] usando tu voz grabada:", os.path.basename(destino), flush=True)
        except Exception as e:
            print("  [reel] no pude usar el audio grabado:", e, flush=True)

    # Fondo. Cada "clip" puede ser:
    #   - texto  -> palabra que busca la IA/tú en Pexels
    #   - objeto -> {"url": mp4 elegido a mano, "dur": segundos, "inicio": recorte por delante}
    videos, duraciones, inicios = [], [], []
    for item in (data.get("clips") or [])[:6]:
        try:
            if isinstance(item, dict):
                v = RV.descargar_video_url(str(item.get("url") or "").strip())
                d = item.get("dur")
                ini = item.get("inicio")
            else:
                if not str(item).strip():
                    continue
                v = RV.buscar_video_pexels(str(item).strip(), RV.pexels_key(data.get("pexels_key")))
                d = None
                ini = None
            if v:
                videos.append(v)
                duraciones.append(float(d) if d else None)
                inicios.append(float(ini) if ini else 0.0)
        except Exception as e:
            print("  [reel] clip falló (%s): %s" % (item, e), flush=True)

    video = None
    if not videos and buscar:
        try:
            video = RV.buscar_video_pexels(buscar, RV.pexels_key(data.get("pexels_key")))
        except Exception as e:
            print("  [reel] Pexels falló, uso fondo de color:", e, flush=True)
            video = None

    logo = None
    try:
        logo = RV._logo_por_defecto()
    except Exception:
        pass

    dur = data.get("duration")
    try:
        dur = int(dur) if dur else None
    except Exception:
        dur = None

    nombre = "reel_%d.mp4" % int(time.time())
    return RV.crear_reel(video=video, videos=(videos or None),
                         duraciones=(duraciones if any(duraciones) else None),
                         inicios=(inicios if any(inicios) else None), transicion=transicion,
                         sombra=sombra, audio_voz=audio_voz, musica=musica,
                         subtitulos=subtitulos, color=color, hook=hook, sub=sub, cta=cta,
                         logo=logo, narrar=narrar, voz=voz, duracion=dur, salida=nombre)


def main():
    # Servir siempre desde la carpeta de este archivo
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    _limpiar_salida()   # de paso, limpia reels viejos al arrancar

    if not os.path.exists(ARCHIVO):
        print(f"[!] No encuentro {ARCHIVO} en esta carpeta.")
        input("Pulsa Enter para cerrar...")
        return

    # Si ya hay OTRA ventana de iniciar.py abierta (el 8000 sigue vivo), no
    # arranques una segunda en otro puerto: eso deja tus Diseños guardados y
    # tu progreso "atrapados" en el puerto anterior, como si no se hubieran
    # guardado. Reutiliza siempre el 8000 cuando ya es esta misma app.
    if instancia_ya_abierta(8000):
        url = f"http://localhost:8000/{ARCHIVO}"
        print("=" * 50)
        print("  ROSA MARÍA STUDIO")
        print("=" * 50)
        print("  Ya había una ventana abierta de la app (puerto 8000).")
        print(f"  Abriendo esa misma:  {url}")
        print("  (Así no se te 'pierden' los Diseños guardados en otro puerto).")
        print("  Puedes cerrar ESTA ventana: la otra sigue sirviendo la app.")
        print("=" * 50)
        webbrowser.open(url)
        return

    puerto = puerto_libre(8000)
    url = f"http://localhost:{puerto}/{ARCHIVO}"

    print("=" * 50)
    print("  ROSA MARÍA STUDIO")
    print("=" * 50)
    print(f"  Abriendo:  {url}")
    if puerto != 8000:
        print(f"  ⚠ El puerto 8000 estaba ocupado por OTRA cosa (no esta app).")
        print(f"    Usando el {puerto} en su lugar. Si tenías Diseños guardados")
        print(f"    con la app en el 8000, aquí NO los verás (son sitios distintos).")
    print("  Para cerrar: cierra esta ventana.")
    print("=" * 50)

    # Abrir el navegador cuando el servidor ya esté listo
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()

    Handler = http.server.SimpleHTTPRequestHandler

    class Silencioso(Handler):
        # HTTP/1.1 con keep-alive: sin esto (HTTP/1.0) Chrome abre y cierra
        # decenas de conexiones al cargar, y los ficheros grandes (app.js,
        # datos-ideas.js, fotos de varios MB) se cortaban con
        # ERR_CONNECTION_RESET -> la app arrancaba sin funcionar o sin fotos.
        protocol_version = "HTTP/1.1"

        # Forzar tipos correctos aunque el registro de Windows diga otra cosa
        extensions_map = {
            **Handler.extensions_map,
            ".css": "text/css",
            ".js": "text/javascript",
            ".mjs": "text/javascript",
            ".json": "application/json",
            ".html": "text/html",
        }
        def log_message(self, *a):    # no llenar la consola de líneas
            pass
        def end_headers(self):
            # Evitar que el navegador cachee versiones antiguas
            self.send_header("Cache-Control", "no-store, must-revalidate")
            super().end_headers()

        # ── API: generar un reel en vídeo (en segundo plano) ───────────────
        # Montar el reel tarda 1-4 min. Si dejásemos la petición abierta todo
        # ese rato sin enviar nada, la conexión se resetea. Por eso: se responde
        # al instante con un id de trabajo, se genera en un hilo, y el navegador
        # pregunta el estado hasta que puede descargar el MP4.
        def do_POST(self):
            if self.path.split("?")[0] != "/api/reel":
                self.send_error(404, "No existe")
                return
            import json, uuid, threading
            try:
                n = int(self.headers.get("Content-Length", 0) or 0)
                data = json.loads(self.rfile.read(n).decode("utf-8") or "{}") if n else {}
            except Exception:
                return self._enviar_json(400, {"error": "peticion invalida"})
            job = uuid.uuid4().hex[:12]
            with REEL_LOCK:
                REEL_JOBS[job] = {"estado": "procesando"}
            threading.Thread(target=_trabajo_reel, args=(job, data), daemon=True).start()
            print("  [reel] trabajo %s en marcha…" % job, flush=True)
            self._enviar_json(202, {"job": job})

        def do_GET(self):
            if self.path.split("?")[0] == "/api/reel/estado":
                from urllib.parse import urlparse, parse_qs
                job = (parse_qs(urlparse(self.path).query).get("job") or [""])[0]
                with REEL_LOCK:
                    info = REEL_JOBS.get(job)
                if not info:
                    return self._enviar_json(404, {"error": "trabajo desconocido"})
                return self._enviar_json(200, info)
            return super().do_GET()

        def _enviar_json(self, code, obj):
            import json
            body = json.dumps(obj).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    # Servidor MULTIHILO: evita que se reseteen conexiones al cargar varios
    # archivos a la vez (CSS/JS/datos grandes en paralelo).
    class ServidorHilos(socketserver.ThreadingMixIn, socketserver.TCPServer):
        daemon_threads = True
        allow_reuse_address = True
        # Backlog grande: al abrir, Chrome lanza ~20 conexiones a la vez
        # (CSS/JS/datos + precarga de fotos). Con el backlog por defecto (5)
        # algunas se reseteaban (ERR_CONNECTION_RESET) y app.js llegaba a
        # medias → la app salía sin funcionar. 128 lo evita.
        request_queue_size = 128

    try:
        with ServidorHilos(("", puerto), Silencioso) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("[!] Error:", e)
        input("Pulsa Enter para cerrar...")


if __name__ == "__main__":
    main()
