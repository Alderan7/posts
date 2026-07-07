#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Reel con AVATAR + VOZ REAL — Rosa María Media
=============================================
Genera un reel 9:16 en el que TU avatar (una foto tuya) habla un guion con
TU voz clonada, usando HeyGen (avatar de foto) + tu voz de ElevenLabs
conectada dentro de HeyGen.

Flujo:  guion (lo escribe el Studio) -> HeyGen pone tu cara y tu voz -> MP4.

NO necesita instalar nada (usa solo la librería estándar de Python) ni FFmpeg:
HeyGen devuelve el vídeo ya montado y aquí solo se descarga.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PREPARACIÓN (una sola vez)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1) En ElevenLabs: clona tu voz (1-3 min de audio limpio hablando tú).
2) En HeyGen: Settings -> Integrations -> conecta tu cuenta de ElevenLabs
   (así tu voz aparece como voz de HeyGen).
3) Copia tu API key de HeyGen (Settings -> API).
4) Crea el archivo  reel-video/config_avatar.py  (ver config_avatar.example.py)
   y pega ahí tu HEYGEN_API_KEY.

CÓMO SE USA
━━━━━━━━━━━
# a) Sube tu foto profesional y apunta el talking_photo_id que imprime:
     py reel_avatar.py --subir-foto "../FOTO PERFIL PROFESIONAL.png"

# b) Lista tus voces y fotos para copiar los IDs (voice_id de tu voz clonada):
     py reel_avatar.py --listar

# c) Pega TALKING_PHOTO_ID y VOICE_ID en config_avatar.py y genera el reel:
     py reel_avatar.py --texto "Si tu empresa de reformas depende del boca a boca, esto te interesa..."
     py reel_avatar.py --guion mi_guion.txt

Salida en:  salida/
"""

import os
import sys
import json
import time
import argparse
import mimetypes
import urllib.request
import urllib.error

# Consola Windows: forzar UTF-8 para acentos/símbolos
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, "salida")

# ── Configuración: config_avatar.py (gitignored) o variables de entorno ──
CFG = {"HEYGEN_API_KEY": "", "TALKING_PHOTO_ID": "", "VOICE_ID": "",
       "WIDTH": 720, "HEIGHT": 1280, "SPEED": 1.0}
try:
    sys.path.insert(0, AQUI)
    import config_avatar as _c   # type: ignore
    for k in CFG:
        if hasattr(_c, k):
            CFG[k] = getattr(_c, k)
except Exception:
    pass
for k in CFG:  # las variables de entorno tienen prioridad si existen
    if os.environ.get(k):
        CFG[k] = os.environ[k]

API = "https://api.heygen.com"
UPLOAD = "https://upload.heygen.com"


def _key():
    k = str(CFG.get("HEYGEN_API_KEY", "")).strip()
    if not k:
        print("[!] Falta tu HEYGEN_API_KEY. Créala en config_avatar.py "
              "(mira config_avatar.example.py).")
        sys.exit(1)
    return k


def _req(url, method="GET", data=None, headers=None, is_json=True):
    hdr = {"X-Api-Key": _key(), "Accept": "application/json"}
    if headers:
        hdr.update(headers)
    body = None
    if data is not None:
        if is_json:
            hdr["Content-Type"] = "application/json"
            body = json.dumps(data).encode("utf-8")
        else:
            body = data  # bytes crudos (subida de foto)
    req = urllib.request.Request(url, data=body, headers=hdr, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read()
    except urllib.error.HTTPError as e:
        detalle = e.read().decode("utf-8", "replace")
        print(f"[!] HTTP {e.code} en {url}\n    {detalle[:300]}")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Error de red en {url}: {e}")
        sys.exit(1)
    try:
        return json.loads(raw)
    except Exception:
        return {"_raw": raw.decode("utf-8", "replace")}


def subir_foto(ruta):
    if not os.path.exists(ruta):
        print(f"[!] No encuentro la foto: {ruta}")
        sys.exit(1)
    ctype = mimetypes.guess_type(ruta)[0] or "image/jpeg"
    with open(ruta, "rb") as f:
        img = f.read()
    print(f"Subiendo {os.path.basename(ruta)} a HeyGen ({len(img)//1024} KB)…")
    out = _req(f"{UPLOAD}/v1/talking_photo", method="POST", data=img,
               headers={"Content-Type": ctype}, is_json=False)
    d = out.get("data", out)
    tp = d.get("talking_photo_id") or d.get("id") or d.get("talking_photo")
    if not tp:
        print("[!] HeyGen no devolvió talking_photo_id. Respuesta:", json.dumps(out)[:300])
        sys.exit(1)
    print("\n  ✓ Foto subida. Copia esto en config_avatar.py:")
    print(f"      TALKING_PHOTO_ID = \"{tp}\"\n")
    return tp


def listar():
    print("── TUS FOTOS/AVATARES (talking_photo_id) ──")
    av = _req(f"{API}/v2/avatars").get("data", {})
    for tp in (av.get("talking_photos") or []):
        print(f"   foto : {tp.get('talking_photo_id')}  ·  {tp.get('talking_photo_name','(sin nombre)')}")
    for a in (av.get("avatars") or [])[:10]:
        print(f"   avatar: {a.get('avatar_id')}  ·  {a.get('avatar_name','')}")
    print("\n── TUS VOCES (voice_id) — busca la tuya clonada ──")
    vs = _req(f"{API}/v2/voices").get("data", {})
    voces = vs.get("voices") or []
    # primero las que parezcan personalizadas (ElevenLabs / nombre propio)
    for v in voces[:60]:
        marca = "  ← posible tuya" if not v.get("preview_audio") or v.get("support_pause") is None else ""
        print(f"   voz  : {v.get('voice_id')}  ·  {v.get('name','')} [{v.get('language','')}]{marca}")
    print("\n(Si no ves tu voz, conéctala en HeyGen: Settings → Integrations → ElevenLabs.)")


def leer_guion(args):
    if args.texto:
        return args.texto.strip()
    if args.guion:
        with open(args.guion, encoding="utf-8") as f:
            return f.read().strip()
    print("[!] Dame el guion con --texto \"...\" o --guion archivo.txt")
    sys.exit(1)


def generar(texto):
    tp = str(CFG.get("TALKING_PHOTO_ID", "")).strip()
    voice = str(CFG.get("VOICE_ID", "")).strip()
    if not tp or not voice:
        print("[!] Faltan TALKING_PHOTO_ID y/o VOICE_ID en config_avatar.py.\n"
              "    Sácalos con:  py reel_avatar.py --listar   (o --subir-foto para la foto).")
        sys.exit(1)
    if len(texto) > 1500:
        print(f"[i] Guion largo ({len(texto)} car.); HeyGen lo aguanta pero el reel será largo.")
    payload = {
        "video_inputs": [{
            "character": {"type": "talking_photo", "talking_photo_id": tp, "scale": 1.0},
            "voice": {"type": "text", "voice_id": voice, "input_text": texto,
                      "speed": float(CFG.get("SPEED", 1.0))},
        }],
        "dimension": {"width": int(CFG.get("WIDTH", 720)), "height": int(CFG.get("HEIGHT", 1280))},
    }
    print("Enviando el guion a HeyGen (tu cara + tu voz)…")
    out = _req(f"{API}/v2/video/generate", method="POST", data=payload)
    vid = (out.get("data") or {}).get("video_id") or out.get("video_id")
    if not vid:
        print("[!] No obtuve video_id. Respuesta:", json.dumps(out)[:400])
        sys.exit(1)
    print(f"  · Vídeo en cola (id {vid}). Renderizando…")
    return esperar_y_descargar(vid)


def esperar_y_descargar(vid, max_min=12):
    t0 = time.time()
    url = None
    while time.time() - t0 < max_min * 60:
        st = _req(f"{API}/v1/video_status.get?video_id={vid}").get("data", {})
        estado = st.get("status")
        if estado == "completed":
            url = st.get("video_url")
            break
        if estado in ("failed", "error"):
            print("[!] HeyGen falló:", st.get("error") or st)
            sys.exit(1)
        print(f"    … {estado or 'procesando'} ({int(time.time()-t0)}s)")
        time.sleep(10)
    if not url:
        print("[!] Se agotó el tiempo de espera. Prueba de nuevo en un momento.")
        sys.exit(1)
    os.makedirs(SALIDA, exist_ok=True)
    destino = os.path.join(SALIDA, f"reel_avatar_{int(time.time())}.mp4")
    print("  · Descargando el reel…")
    try:
        urllib.request.urlretrieve(url, destino)
    except Exception as e:
        print(f"[!] No pude descargar el MP4 ({e}). URL directa:\n    {url}")
        sys.exit(1)
    print(f"\n  ✓ LISTO → {destino}\n")
    return destino


def main():
    ap = argparse.ArgumentParser(description="Reel con tu avatar (foto) y tu voz real (HeyGen).")
    ap.add_argument("--subir-foto", dest="foto", help="Sube una foto tuya a HeyGen y devuelve el talking_photo_id")
    ap.add_argument("--listar", action="store_true", help="Lista tus fotos y voces (para copiar los IDs)")
    ap.add_argument("--texto", help="Guion a locutar (texto directo)")
    ap.add_argument("--guion", help="Archivo .txt con el guion")
    a = ap.parse_args()

    if a.foto:
        subir_foto(a.foto); return
    if a.listar:
        listar(); return
    generar(leer_guion(a))


if __name__ == "__main__":
    main()
