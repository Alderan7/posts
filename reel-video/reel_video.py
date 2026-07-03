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


def crear_reel(video=None, color="dark", hook="", sub="", cta="",
               logo=None, musica=None, duracion=None, salida="reel.mp4",
               font=None, font_reg=None):
    """Genera un reel 1080x1920 y lo guarda en `salida`."""
    _check_moviepy()
    from moviepy import (VideoFileClip, ImageClip, ColorClip,
                         CompositeVideoClip, AudioFileClip, concatenate_audioclips)
    import numpy as np
    from PIL import Image, ImageDraw

    font     = font     or buscar_fuente(True)
    font_reg = font_reg or buscar_fuente(False) or font
    dur = duracion or 15

    # ── 1) Fondo: vídeo recortado a 9:16 o color de marca ────────────────
    if video and os.path.exists(video):
        clip = VideoFileClip(video)
        dur = duracion or min(clip.duration, 30)
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

    # ── 7) Música opcional ───────────────────────────────────────────────
    if musica and os.path.exists(musica):
        try:
            aud = AudioFileClip(musica)
            aud = aud.subclipped(0, dur) if hasattr(aud, "subclipped") else aud.subclip(0, dur)
            final = final.with_audio(aud) if hasattr(final, "with_audio") else final.set_audio(aud)
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
    args = ap.parse_args()

    if args.lote:
        modo_lote(args)
    else:
        crear_reel(video=args.video, color=args.color, hook=args.hook, sub=args.sub,
                   cta=args.cta, logo=args.logo or _logo_por_defecto(),
                   musica=args.music, duracion=args.duration, salida=args.out, font=args.font)


if __name__ == "__main__":
    main()
