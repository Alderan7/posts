# 🎬 Módulo de Reels en vídeo — Rosa María Media

Convierte un clip de fondo en un **Reel vertical 1080×1920** con tu gancho,
subtítulo y CTA, en la estética de marca (negro / crema / azul #38B6FF).

Es el complemento del **Studio HTML** (botón 🎬 Reel): allí generas la
**portada + guion**, aquí montas el vídeo final.

---

## 1) Instalación (una sola vez)

### a) Dependencias de Python
```powershell
cd "F:\.CLAUDE CODE\POSTS\reel-video"
py -m pip install -r requirements.txt
```

### b) FFmpeg (motor de vídeo — imprescindible)
Opción fácil con winget:
```powershell
winget install Gyan.FFmpeg
```
Luego **cierra y reabre** la terminal. Comprueba con:
```powershell
ffmpeg -version
```
Si `winget` no está, descarga FFmpeg de https://www.gyan.dev/ffmpeg/builds/
(“release full”), descomprime y añade la carpeta `bin` al PATH de Windows.

### c) (Opcional) Fuente Montserrat
Para que el texto use tu tipografía, pon `Montserrat-Bold.ttf` y
`Montserrat-Regular.ttf` en una subcarpeta `fonts/`. Si no, usa una fuente
del sistema automáticamente. Descarga gratis: https://fonts.google.com/specimen/Montserrat

---

## 2) Uso

### Un reel con vídeo de fondo
```powershell
py reel_video.py --video videos_entrada/obra.mp4 `
  --hook "5 señales de que dependes del boca a boca" `
  --sub  "Y cómo dejar de perder presupuestos" `
  --cta  "Escríbeme REFORMAS"
```

### Sin vídeo (fondo de color de marca)
```powershell
py reel_video.py --color dark --hook "Estrategia que convierte" --cta "Hablemos"
```

### En lote (varios clips de golpe)
1. Mete tus clips en `videos_entrada/`.
2. Edita `textos.csv` (separador `;`):
   ```
   archivo;hook;sub;cta
   obra1.mp4;Tu mejor obra es tu mejor anuncio;Deja de esconderla;Hablemos
   ```
3. Ejecuta:
   ```powershell
   py reel_video.py --lote
   ```

Los reels salen en `salida/`.

---

## 3) Flujo recomendado (rápido)

1. En el **Studio** → modo 🎬 **Reel** → *Generar* → botón 📝 **Guión**
   (descarga el guion con gancho + claves + caption).
2. Graba/consigue el clip de fondo (tu obra, un time-lapse, stock de Pexels).
3. Aquí: `py reel_video.py --video tuclip.mp4 --hook "..." --cta "..."`.
4. Sube el `.mp4` a Instagram como Reel y usa la portada del Studio como *cover*.

---

## Opciones (todas)
| Flag | Qué hace |
|------|----------|
| `--video` | vídeo de fondo (mp4/mov/webm) |
| `--color dark\|light` | color de fondo si no hay vídeo |
| `--hook` | gancho principal (texto grande) |
| `--sub` | subtítulo |
| `--cta` | llamada a la acción (píldora azul) |
| `--logo` | PNG transparente (por defecto usa `../logo-rm-blanco-iso.png`) |
| `--music` | pista de audio opcional |
| `--duration` | segundos (por defecto: duración del clip o 15) |
| `--out` | nombre del archivo de salida |
| `--font` | ruta a fuente TTF |
| `--lote` | procesa toda la carpeta `videos_entrada/` |

---

## Problemas comunes
- **`ffmpeg not found`** → no instalaste FFmpeg o no reiniciaste la terminal (paso 1b).
- **Texto con recuadro/fuente fea** → falta Montserrat; ponla en `fonts/` (paso 1c).
- **Se ve lento** → normal, renderizar vídeo tarda; sube `--duration` solo lo necesario.
