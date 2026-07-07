#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generador de Reels en vídeo — Rosa María Media
================================================
Coge un vídeo de fondo, lo recorta a 9:16 (1080x1920), le aplica un
oscurecimiento elegante y superpone tu GANCHO, subtítulo y CTA con la
estética de marca (#1A1A1A / #F5F1EA / #38B6FF).

Pensado para acompañar al "Studio" HTML: exporta la PORTADA + guion desde
la web (botón 🎬 Reel) y aquí conviertes un clip en el reel final.

USO RÁPIDO
----------
1) Instala dependencias (una sola vez):
       py -m pip install -r requirements.txt
   y FFmpeg (ver LEEME.md).

2) Un reel suelto:
       py reel_video.py --video videos_entrada/obra.mp4 ^
           --hook "5 señales de que dependes del boca a boca" ^
           --sub  "Y cómo dejar de perder presupuestos" ^
           --cta  "Escríbeme REFORMAS"

3) Sin vídeo (fondo de color de marca):
       py reel_video.py --color dark --hook "Estrategia que convierte"

4) Lote: mete varios clips en videos_entrada/ y un textos.csv (ver LEEME.md):
       py reel_video.py --lote

Salida en:  salida/
"""

import os
import sys
import csv
import argparse

# Consola Windows: forzar UTF-8 para poder imprimir acentos y símbolos
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# ── Paleta e identidad de marca ──────────────────────────────────────────
NEGRO  = (26, 26, 26)       # #1A1A1A
CREMA  = (245, 241, 234)    # #F5F1EA
AZUL   = (56, 182, 255)     # #38B6FF
W, H   = 1080, 1920         # 9:16 vertical
HANDLE = "@rosamariamedia"

# Zonas seguras de Instagram/TikTok (no tapar con texto importante)
SAFE_TOP = 220              # cabecera (perfil)
SAFE_BOT = 430              # caption + botones laterales

AQUI = os.path.dirname(os.path.abspath(__file__))
DIR_ENTRADA = os.path.join(AQUI, "videos_entrada")
DIR_SALIDA  = os.path.join(AQUI, "salida")

# Key de Pexels (la misma del Studio, gratis). Se puede sobreescribir con
# --pexels-key o la variable de entorno PEXELS_KEY.
PEXELS_KEY_DEFAULT = "DQlg4GAqeCIIF3CkZpcFQBopg7PztGO8uKcVXHi8XnYCyWDSEo1QvyqC"


def pexels_key(cli=None):
    return (cli or os.environ.get("PEXELS_KEY") or PEXELS_KEY_DEFAULT).strip()


def _es_error_ssl(e):
    import ssl, urllib.error
    if isinstance(e, ssl.SSLError):
        return True
    if isinstance(e, urllib.error.URLError) and isinstance(getattr(e, "reason", None), ssl.SSLError):
        return True
    return "SSL" in str(e) or "CERTIFICATE" in str(e)


def _url_abrir(url, headers=None, timeout=25):
    """Abre una URL https. Intenta con verificación de certificado y, si falla
    por SSL (típico con antivirus que intercepta HTTPS), reintenta sin verificar."""
    import ssl, urllib.request
    h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"}
    h.update(headers or {})
    req = urllib.request.Request(url, headers=h)
    # 1) verificado (con certifi si está disponible)
    try:
        try:
            import certifi
            ctx = ssl.create_default_context(cafile=certifi.where())
        except Exception:
            ctx = ssl.create_default_context()
        return urllib.request.urlopen(req, timeout=timeout, context=ctx)
    except Exception as e:
        if not _es_error_ssl(e):
            raise
        # 2) reintento sin verificar (red con antivirus/proxy que rompe el cert)
        ctx = ssl._create_unverified_context()
        return urllib.request.urlopen(req, timeout=timeout, context=ctx)


def buscar_video_pexels(query, key, dest_dir=None):
    """Busca un vídeo vertical en Pexels por `query`, descarga el mejor archivo
    (HD vertical, alto <= 1920) y devuelve su ruta local. None si falla.
    Cachea por consulta en videos_entrada/ para no re-descargar."""
    import json, re, urllib.parse
    dest_dir = dest_dir or DIR_ENTRADA
    os.makedirs(dest_dir, exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "_", (query or "reel").lower()).strip("_")[:40] or "reel"
    destino = os.path.join(dest_dir, f"pexels_{slug}.mp4")
    if os.path.exists(destino) and os.path.getsize(destino) > 10000:
        return destino  # ya descargado antes

    url = ("https://api.pexels.com/videos/search?query="
           + urllib.parse.quote(query or "home renovation")
           + "&per_page=8&orientation=portrait&size=medium")
    try:
        with _url_abrir(url, headers={"Authorization": key}) as r:
            data = json.load(r)
    except Exception as e:
        print(f"    (aviso) Pexels no respondió para '{query}': {e}")
        return None

    vids = data.get("videos") or []
    if not vids:
        print(f"    (aviso) Pexels sin resultados para '{query}'")
        return None

    # Elegir el mejor archivo: vertical (h>w), calidad hd, alto <= 1920 lo mayor posible
    mejor, mejor_score = None, -1
    for v in vids[:5]:
        for f in v.get("video_files", []):
            w, h = f.get("width") or 0, f.get("height") or 0
            if not w or not h or h < w:      # descartar horizontales
                continue
            score = h if h <= 1920 else 1920 - (h - 1920)   # penaliza pasarse de 1920
            if f.get("quality") == "hd":
                score += 200
            if score > mejor_score:
                mejor, mejor_score = f, score
    if not mejor:
        # sin verticales claros: coger el primero disponible
        mejor = (vids[0].get("video_files") or [None])[0]
    if not mejor or not mejor.get("link"):
        return None

    try:
        print(f"    ↓ Pexels: '{query}' ({mejor.get('width')}x{mejor.get('height')})")
        import shutil
        with _url_abrir(mejor["link"], timeout=90) as r, open(destino, "wb") as f:
            shutil.copyfileobj(r, f)
        return destino if os.path.getsize(destino) > 10000 else None
    except Exception as e:
        print(f"    (aviso) fallo al descargar vídeo Pexels: {e}")
        return None


# ── Utilidades ───────────────────────────────────────────────────────────
def _check_moviepy():
    try:
        import moviepy  # noqa
    except ImportError:
        sys.exit("✖ Falta MoviePy. Instala:  py -m pip install -r requirements.txt")


def buscar_fuente(negrita=True):
    """Devuelve una ruta de fuente TTF válida. Prioriza Montserrat; si no,
    cae a fuentes del sistema (Windows). Puedes forzar con --font."""
    candidatas = [
        os.path.join(AQUI, "fonts", "Montserrat-Bold.ttf" if negrita else "Montserrat-Regular.ttf"),
        r"C:\Windows\Fonts\Montserrat-Bold.ttf" if negrita else r"C:\Windows\Fonts\Montserrat-Regular.ttf",
        r"C:\Windows\Fonts\segoeuib.ttf" if negrita else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if negrita else r"C:\Windows\Fonts\arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if negrita else
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for c in candidatas:
        if c and os.path.exists(c):
            return c
    return None  # MoviePy usará su fuente por defecto


def _rgba(color, a=255):
    return (color[0], color[1], color[2], a)


def _wrap(txt, max_chars):
    """Envuelve el texto en líneas de ~max_chars sin partir palabras."""
    palabras = txt.split()
    lineas, actual = [], ""
    for w in palabras:
        if len(actual) + len(w) + 1 <= max_chars:
            actual = (actual + " " + w).strip()
        else:
            if actual:
                lineas.append(actual)
            actual = w
    if actual:
        lineas.append(actual)
    return "\n".join(lineas)


def _texto(txt, font, fontsize, color, size=None, align="center", max_chars=18):
    """Crea un TextClip con salto de línea MANUAL (fiable en 2.x).
    Envuelve el texto a max_chars por línea y usa method='label'."""
    from moviepy import TextClip
    wrapped = _wrap(txt, max_chars) if max_chars else txt
    col = "rgb%s" % (tuple(color),)
    try:
        return TextClip(text=wrapped, font=font, font_size=fontsize, color=col,
                        method="label", text_align=align)
    except TypeError:
        # API MoviePy 1.x
        return TextClip(wrapped, font=font, fontsize=fontsize, color=col,
                        method="label", align=align)


# ── Voz IA GRATIS (Microsoft Edge TTS: voces neuronales, sin cuenta ni pagar) ──
# Voces españolas útiles: es-ES-ElviraNeural (mujer, España), es-ES-AlvaroNeural
# (hombre), es-MX-DaliaNeural, es-AR-ElenaNeural...
def generar_voz(texto, salida_mp3, voz="es-ES-ElviraNeural"):
    """Convierte `texto` en un mp3 con voz de IA. Devuelve la ruta o None.
    Necesita el paquete gratuito 'edge-tts' (py -m pip install edge-tts)."""
    texto = (texto or "").strip()
    if not texto:
        return None
    try:
        import edge_tts, asyncio
    except ImportError:
        print("  (aviso) Para la voz IA instala una vez:  py -m pip install edge-tts")
        return None
    async def _go():
        await edge_tts.Communicate(texto, voz).save(salida_mp3)
    try:
        asyncio.run(_go())
    except Exception as e:
        print("  (aviso) no se pudo generar la voz IA:", e)
        return None
    return salida_mp3 if os.path.exists(salida_mp3) and os.path.getsize(salida_mp3) > 800 else None


def crear_reel(video=None, color="dark", hook="", sub="", cta="",
               logo=None, musica=None, duracion=None, salida="reel.mp4",
               font=None, font_reg=None, narrar=None, voz="es-ES-ElviraNeural"):
    """Genera un reel 1080x1920 y lo guarda en `salida`."""
    _check_moviepy()
    from moviepy import (VideoFileClip, ImageClip, ColorClip,
                         CompositeVideoClip, AudioFileClip, concatenate_audioclips,
                         concatenate_videoclips)
    import numpy as np
    from PIL import Image, ImageDraw

    font     = font     or buscar_fuente(True)
    font_reg = font_reg or buscar_fuente(False) or font
    dur = duracion or 15

    # ── 0) Voz IA (gratis): si se pide, la duración del reel = la de la voz ──
    voz_path = None
    if narrar:
        os.makedirs(DIR_SALIDA, exist_ok=True)
        stem = os.path.splitext(os.path.basename(salida))[0] or "reel"
        voz_path = generar_voz(narrar, os.path.join(DIR_SALIDA, f"_voz_{stem}.mp3"), voz)
        if voz_path:
            try:
                _va = AudioFileClip(voz_path)
                dur = max(3.0, min(90.0, _va.duration + 0.6))   # cola de 0.6s
                _va.close()
            except Exception:
                pass

    # ── 1) Fondo: vídeo recortado a 9:16 o color de marca ────────────────
    if video and os.path.exists(video):
        clip = VideoFileClip(video)
        if not voz_path:
            dur = duracion or min(clip.duration, 30)
        # Si el clip es más corto que la narración, se repite para cubrirla
        if clip.duration < dur:
            n = int(dur // clip.duration) + 1
            clip = concatenate_videoclips([clip] * n)
        clip = clip.subclipped(0, dur) if hasattr(clip, "subclipped") else clip.subclip(0, dur)
        # Escalar para cubrir y recortar centrado (cover)
        escala = max(W / clip.w, H / clip.h)
        nw, nh = int(clip.w * escala), int(clip.h * escala)
        clip = clip.resized((nw, nh)) if hasattr(clip, "resized") else clip.resize((nw, nh))
        x, y = (nw - W) // 2, (nh - H) // 2
        clip = (clip.cropped(x1=x, y1=y, x2=x + W, y2=y + H)
                if hasattr(clip, "cropped")
                else clip.crop(x1=x, y1=y, x2=x + W, y2=y + H))
        fondo = clip
    else:
        base = NEGRO if color != "light" else CREMA
        fondo = ColorClip((W, H), color=base, duration=dur)

    capas = [fondo]

    # ── 2) Oscurecimiento elegante (degradado) para legibilidad ──────────
    grad = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    px = grad.load()
    for yy in range(H):
        # más oscuro arriba y abajo (donde va el texto), suave en el centro
        t = yy / H
        a = int(150 * (1 - t) ** 1.5 + 190 * t ** 2.2)     # 0..~190
        a = max(40, min(a, 210))
        for xx in range(0, W, 1):
            px[xx, yy] = (NEGRO[0], NEGRO[1], NEGRO[2], a)
    ov = ImageClip(np.array(grad)).with_duration(dur) if hasattr(ImageClip(np.array(grad)), "with_duration") \
        else ImageClip(np.array(grad)).set_duration(dur)
    capas.append(ov)

    def _pos(clip, pos):
        return clip.with_position(pos) if hasattr(clip, "with_position") else clip.set_position(pos)

    def _dur(clip, d):
        return clip.with_duration(d) if hasattr(clip, "with_duration") else clip.set_duration(d)

    # ── 3) Bloque de texto (barra + gancho + subtítulo) dibujado con PIL ──
    #     PIL nos da control exacto de altura y saltos de línea (fiable).
    if hook or sub:
        bloque = _bloque_texto(hook, sub, font, font_reg)
        bclip = _dur(ImageClip(np.array(bloque)), dur)
        capas.append(_pos(bclip, ("center", int(H * 0.42) - bloque.height // 2)))

    # ── 4) Píldora CTA (fondo azul) abajo, sobre la zona segura ──────────
    if cta:
        pill = _pildora_cta(cta, font, 44)
        cimg = _dur(ImageClip(np.array(pill)), dur)
        capas.append(_pos(cimg, ("center", H - SAFE_BOT - 40)))

    # ── 6) Logo RM arriba + handle abajo ─────────────────────────────────
    if logo and os.path.exists(logo):
        lg = ImageClip(logo)
        lg = lg.resized(height=90) if hasattr(lg, "resized") else lg.resize(height=90)
        capas.append(_pos(_dur(lg, dur), ("center", 90)))
    thandle = _dur(_texto(HANDLE, font_reg, 34, _rgba(CREMA)[:3], size=(W, None), align="center"), dur)
    capas.append(_pos(thandle, ("center", H - 150)))

    final = CompositeVideoClip(capas, size=(W, H))
    final = _dur(final, dur)

    # ── 7) Audio: voz IA (prioridad) o música ────────────────────────────
    def _set_audio(cl, aud):
        return cl.with_audio(aud) if hasattr(cl, "with_audio") else cl.set_audio(aud)
    if voz_path:
        try:
            final = _set_audio(final, AudioFileClip(voz_path))   # tu guion locutado
        except Exception as e:
            print("  (aviso) no se pudo añadir la voz:", e)
    elif musica and os.path.exists(musica):
        try:
            aud = AudioFileClip(musica)
            aud = aud.subclipped(0, dur) if hasattr(aud, "subclipped") else aud.subclip(0, dur)
            final = _set_audio(final, aud)
        except Exception as e:
            print("  (aviso) no se pudo añadir música:", e)

    os.makedirs(DIR_SALIDA, exist_ok=True)
    ruta = salida if os.path.isabs(salida) else os.path.join(DIR_SALIDA, salida)
    print(f"→ Renderizando {os.path.basename(ruta)} ({int(dur)}s)...")
    final.write_videofile(ruta, fps=30, codec="libx264", audio_codec="aac",
                          preset="medium", threads=4, logger="bar")
    print(f"✓ Listo: {ruta}")
    return ruta


def _bloque_texto(hook, sub, font_bold, font_reg):
    """Dibuja barra de acento + gancho (bold) + subtítulo (regular) centrados,
    en una imagen RGBA de ancho W. Devuelve la imagen PIL."""
    from PIL import Image, ImageDraw, ImageFont

    def cargar(path, sz):
        try:
            return ImageFont.truetype(path, sz) if path else ImageFont.load_default()
        except Exception:
            return ImageFont.load_default()

    fb = cargar(font_bold, 82)
    fr = cargar(font_reg, 44)
    medidor = ImageDraw.Draw(Image.new("RGBA", (4, 4)))

    def envolver(txt, fnt, max_w):
        pals, lineas, cur = txt.split(), [], ""
        for w in pals:
            prueba = (cur + " " + w).strip()
            if medidor.textlength(prueba, font=fnt) <= max_w:
                cur = prueba
            else:
                if cur:
                    lineas.append(cur)
                cur = w
        if cur:
            lineas.append(cur)
        return lineas

    max_w = W - 200
    hook_lines = envolver(hook, fb, max_w) if hook else []
    sub_lines = envolver(sub, fr, W - 260) if sub else []

    def alto(fnt):
        a, d = fnt.getmetrics()
        return a + d

    lh_h = int(alto(fb) * 1.12)
    lh_s = int(alto(fr) * 1.2)
    barra_h, gap1, gap2 = 8, 46, 44
    total = barra_h + gap1 + len(hook_lines) * lh_h
    if sub_lines:
        total += gap2 + len(sub_lines) * lh_s

    img = Image.new("RGBA", (W, total), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    y = 0
    # barra de acento azul centrada
    d.rounded_rectangle([W // 2 - 45, y, W // 2 + 45, y + barra_h], radius=barra_h // 2, fill=_rgba(AZUL))
    y += barra_h + gap1
    for ln in hook_lines:
        w = medidor.textlength(ln, font=fb)
        d.text(((W - w) / 2, y), ln, font=fb, fill=_rgba(CREMA))
        y += lh_h
    if sub_lines:
        y += gap2
        for ln in sub_lines:
            w = medidor.textlength(ln, font=fr)
            d.text(((W - w) / 2, y), ln, font=fr, fill=(CREMA[0], CREMA[1], CREMA[2], 220))
            y += lh_s
    return img


def _pildora_cta(texto, font_path, fontsize):
    """Dibuja una píldora azul con un triángulo ▶ (dibujado) + texto blanco."""
    from PIL import Image, ImageDraw, ImageFont
    try:
        fnt = ImageFont.truetype(font_path, fontsize) if font_path else ImageFont.load_default()
    except Exception:
        fnt = ImageFont.load_default()
    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    l, t, r, b = tmp.textbbox((0, 0), texto, font=fnt)
    tw, th = r - l, b - t
    tri = int(fontsize * 0.55)                 # tamaño del triángulo play
    padx, pady, gap = 50, 30, 22
    w = tri + gap + tw + padx * 2
    h = th + pady * 2
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, w, h], radius=h // 2, fill=_rgba(AZUL))
    # triángulo play (blanco)
    cy = h // 2
    tx = padx
    d.polygon([(tx, cy - tri // 2), (tx, cy + tri // 2), (tx + tri, cy)], fill=(255, 255, 255, 255))
    # texto
    d.text((tx + tri + gap - l, pady - t), texto, font=fnt, fill=(255, 255, 255, 255))
    return img


def modo_lote(args):
    """Procesa todos los vídeos de videos_entrada/ usando textos.csv si existe.
    textos.csv (separador ;):  archivo;hook;sub;cta"""
    textos = {}
    csv_path = os.path.join(AQUI, "textos.csv")
    if os.path.exists(csv_path):
        with open(csv_path, encoding="utf-8-sig") as f:
            for row in csv.reader(f, delimiter=";"):
                if len(row) >= 2 and row[0].strip().lower() != "archivo":
                    textos[row[0].strip()] = row[1:]
    vids = [f for f in os.listdir(DIR_ENTRADA)
            if f.lower().endswith((".mp4", ".mov", ".webm", ".mkv", ".avi"))]
    if not vids:
        sys.exit(f"✖ No hay vídeos en {DIR_ENTRADA}")
    print(f"Lote: {len(vids)} vídeo(s)\n")
    logo = args.logo or _logo_por_defecto()
    for i, v in enumerate(vids, 1):
        t = textos.get(v, [args.hook, args.sub, args.cta])
        hook = t[0] if len(t) > 0 else args.hook
        sub = t[1] if len(t) > 1 else args.sub
        cta = t[2] if len(t) > 2 else args.cta
        out = f"reel_{i:02d}_{os.path.splitext(v)[0]}.mp4"
        print(f"[{i}/{len(vids)}] {v}")
        crear_reel(video=os.path.join(DIR_ENTRADA, v), hook=hook, sub=sub, cta=cta,
                   logo=logo, musica=args.music, duracion=args.duration,
                   salida=out, font=args.font)


def modo_mes(args, carpeta):
    """Lee la carpeta descomprimida del ZIP 'Generar Mes' del Studio y monta
    los reels de los días de Reel. Cada día trae un reel.json {hook,sub,cta,busqueda}.

    Fondo de cada reel (en este orden):
      1) clip de videos_entrada/ (por orden) si los hay y NO se usa Pexels
      2) vídeo de Pexels descargado por la palabra 'busqueda' del día (por defecto)
      3) fondo de color de marca (--color) si nada de lo anterior
    Usa --sin-pexels para no descargar de Pexels (solo clips locales/color).
    """
    import glob
    if not os.path.isdir(carpeta):
        sys.exit(f"✖ No existe la carpeta: {carpeta}")

    # Buscar reel.json en cualquier subcarpeta (dia_XX_reel_portada/)
    jsons = sorted(glob.glob(os.path.join(carpeta, "**", "reel.json"), recursive=True))
    if not jsons:
        sys.exit("✖ No hay reel.json en la carpeta. ¿Generaste el mes con días de Reel?\n"
                 "  (Descomprime el ZIP rm_contenido_XXdias.zip y apunta --mes a esa carpeta)")

    clips = sorted([os.path.join(DIR_ENTRADA, f) for f in os.listdir(DIR_ENTRADA)
                    if f.lower().endswith((".mp4", ".mov", ".webm", ".mkv", ".avi"))]) \
        if os.path.isdir(DIR_ENTRADA) else []

    logo = args.logo or _logo_por_defecto()
    usar_pexels = not getattr(args, "sin_pexels", False)
    key = pexels_key(getattr(args, "pexels_key", None))
    print(f"Mes: {len(jsons)} reel(s) · {len(clips)} clip(s) locales · "
          f"Pexels: {'sí' if usar_pexels else 'no'}\n")

    import json
    for i, jf in enumerate(jsons, 1):
        try:
            data = json.load(open(jf, encoding="utf-8"))
        except Exception as e:
            print(f"  (aviso) {jf}: json ilegible ({e}); salto")
            continue
        dia = data.get("dia", i)
        # 1) clip local · 2) vídeo de Pexels por keyword · 3) color
        video = clips[(i - 1) % len(clips)] if clips else None
        if not video and usar_pexels:
            video = buscar_video_pexels(data.get("busqueda") or data.get("hook", ""), key)
        out = f"reel_dia_{int(dia):02d}.mp4"
        origen = os.path.basename(os.path.dirname(jf))
        print(f"[{i}/{len(jsons)}] {origen}  ({'clip: '+os.path.basename(video) if video else 'fondo color'})")
        crear_reel(video=video, color=args.color,
                   hook=data.get("hook", ""), sub=data.get("sub", ""), cta=data.get("cta", ""),
                   logo=logo, musica=args.music, duracion=args.duration, salida=out, font=args.font)
    print(f"\n✓ {len(jsons)} reels en {DIR_SALIDA}")


def _logo_por_defecto():
    """Usa el logo blanco transparente del repo si existe (../logo-rm-blanco-iso.png)."""
    cand = os.path.join(AQUI, "..", "logo-rm-blanco-iso.png")
    return cand if os.path.exists(cand) else None


def main():
    ap = argparse.ArgumentParser(description="Genera Reels 1080x1920 con estética Rosa María Media")
    ap.add_argument("--video", help="vídeo de fondo (mp4/mov). Si se omite, usa --color")
    ap.add_argument("--color", default="dark", choices=["dark", "light"], help="color de fondo si no hay vídeo")
    ap.add_argument("--hook", default="", help="gancho principal (texto grande)")
    ap.add_argument("--sub", default="", help="subtítulo")
    ap.add_argument("--cta", default="", help="llamada a la acción (píldora azul)")
    ap.add_argument("--logo", help="ruta a logo PNG transparente (por defecto usa el del repo)")
    ap.add_argument("--music", help="pista de audio opcional")
    ap.add_argument("--duration", type=int, help="duración en segundos")
    ap.add_argument("--out", default="reel.mp4", help="nombre de salida")
    ap.add_argument("--font", help="ruta a fuente TTF (por defecto busca Montserrat/sistema)")
    ap.add_argument("--lote", action="store_true", help="procesa toda la carpeta videos_entrada/")
    ap.add_argument("--mes", metavar="CARPETA",
                    help="carpeta del ZIP 'Generar Mes' descomprimido: monta los reels de los días de Reel")
    ap.add_argument("--buscar", metavar="PALABRA",
                    help="descarga un vídeo de fondo de Pexels por esa palabra (en vez de --video)")
    ap.add_argument("--pexels-key", dest="pexels_key",
                    help="API key de Pexels (por defecto usa la del Studio o env PEXELS_KEY)")
    ap.add_argument("--sin-pexels", dest="sin_pexels", action="store_true",
                    help="en --mes: no descargar de Pexels (solo clips locales/color)")
    ap.add_argument("--narrar", nargs="?", const="__AUTO__", metavar="TEXTO",
                    help="añade VOZ IA gratis. Sin texto: locuta el hook+subtítulo. "
                         "Con texto: locuta ese guion. (necesita: py -m pip install edge-tts)")
    ap.add_argument("--voz", default="es-ES-ElviraNeural",
                    help="voz IA (por defecto es-ES-ElviraNeural; también es-ES-AlvaroNeural, es-MX-DaliaNeural…)")
    args = ap.parse_args()

    # Si --narrar viene sin texto, se locuta el hook + subtítulo
    narrar = args.narrar
    if narrar == "__AUTO__":
        narrar = ". ".join(t for t in [args.hook, args.sub] if t).strip() or None

    if args.mes:
        modo_mes(args, args.mes)
    elif args.lote:
        modo_lote(args)
    else:
        video = args.video
        if not video and args.buscar:
            video = buscar_video_pexels(args.buscar, pexels_key(args.pexels_key))
        crear_reel(video=video, color=args.color, hook=args.hook, sub=args.sub,
                   cta=args.cta, logo=args.logo or _logo_por_defecto(),
                   musica=args.music, duracion=args.duration, salida=args.out, font=args.font,
                   narrar=narrar, voz=args.voz)


if __name__ == "__main__":
    main()
