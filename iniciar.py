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


def main():
    # Servir siempre desde la carpeta de este archivo
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    if not os.path.exists(ARCHIVO):
        print(f"[!] No encuentro {ARCHIVO} en esta carpeta.")
        input("Pulsa Enter para cerrar...")
        return

    puerto = puerto_libre(8000)
    url = f"http://localhost:{puerto}/{ARCHIVO}"

    print("=" * 50)
    print("  ROSA MARÍA STUDIO")
    print("=" * 50)
    print(f"  Abriendo:  {url}")
    print("  Para cerrar: cierra esta ventana.")
    print("=" * 50)

    # Abrir el navegador cuando el servidor ya esté listo
    threading.Timer(1.0, lambda: webbrowser.open(url)).start()

    Handler = http.server.SimpleHTTPRequestHandler

    class Silencioso(Handler):
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

    try:
        with socketserver.TCPServer(("", puerto), Silencioso) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("[!] Error:", e)
        input("Pulsa Enter para cerrar...")


if __name__ == "__main__":
    main()
