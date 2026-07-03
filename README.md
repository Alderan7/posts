# Rosa María Studio — Generador de contenido

Herramienta para crear el contenido de Instagram de **Rosa María Media**
(media buyer para empresas de reformas): posts, carruseles y reels con la
estética de marca, más un módulo aparte para montar reels en vídeo.

Paleta: negro `#1A1A1A` · crema `#F5F1EA` · azul `#38B6FF`.
Fuentes: Montserrat (principal) + Playfair Display (acentos).

---

## ▶ Cómo abrirlo

**Doble clic en `iniciar.py`** → se abre el generador en el navegador.
(Arranca un servidor local, necesario para las fotos, Pexels y la IA.)

> ⚠️ No lo abras con doble clic en el `.html` directo (`file://`): las fotos,
> Pexels y la IA no funcionan por seguridad del navegador. Usa siempre `iniciar.py`.
> El antiguo `iniciar.bat` puede bloquearlo el antivirus — usa el `.py`.

---

## 📁 Dónde está el código

### Generador web (lo que se abre en el navegador)
| Archivo | Qué es |
|---|---|
| **`rosa-maria-studio-2.html`** | La app: estructura + todo el CSS incrustado (así se ve bien se abra como se abra). Enlaza los 2 de abajo. |
| **`app.js`** | Toda la lógica: generar posts/carruseles/reels, motor de feed P1–P9, biblioteca de fotos, Pexels, IA de imágenes, exportar (PNG/ZIP/PPTX), fábrica "Generar Mes". |
| **`datos-ideas.js`** | Banco de 365 ideas de contenido (`window.IDEAS_365`). |

> Estos 3 archivos van **siempre juntos** en la misma carpeta.
> (El CSS va dentro del HTML a propósito: en Windows algunos equipos rechazan
> un `.css` externo por el tipo MIME y la página saldría sin estilos.)

### Módulo de reels en vídeo (Python, aparte)
| Ruta | Qué es |
|---|---|
| **`reel-video/reel_video.py`** | Convierte un clip en un Reel 1080×1920 con tu texto y estética. |
| **`reel-video/LEEME.md`** | Instrucciones de instalación y uso del módulo. |
| **`reel-video/requirements.txt`** | Dependencias Python. |
| `reel-video/videos_entrada/` | Ahí metes tus clips de fondo. |
| `reel-video/salida/` | Ahí aparecen los reels montados. |

### Recursos
| Ruta | Qué es |
|---|---|
| `logo-rm-blanco-iso.png` / `logo-rm-negro-iso.png` | Logos (blanco para fondos oscuros, negro para claros/azules). |
| `FOTOS PROFESIONALES/` | Tus fotos; se auto-cargan en la biblioteca al abrir el Studio. |
| `iniciar.py` | Lanzador del generador. |

---

## 🎯 Qué hace cada parte del generador

- **Post / Carrusel / Reel** (arriba): elige el formato.
- **Posición feed (P1–P9)**: elige qué tipo de post generar, o *Auto* para avanzar por el grid (plantilla de 9 tiles).
- **⚡ Generar**: crea el contenido con una idea del banco.
- **📷 Fotos**: biblioteca. Sube fotos, busca en **Pexels**, o crea imágenes con **✨ IA** (prompt). Clic en una foto = usarla en el slide.
- **📅 Mes**: genera el contenido de varios días de golpe y lo descarga en un ZIP (imágenes + textos + `reel.json` para el módulo de vídeo).
- **↓ Exportar**: PNG (un slide), ZIP (todos), o **PPTX** (editable en Canva).
- **📝 Guión** (modo Reel): descarga el guion del reel en `.txt`.
- Pestaña **COPY**: caption + hashtags + guion, siempre coherentes con lo que ves.

---

## 🔁 Flujo mensual recomendado (rápido)

1. Abre `iniciar.py` → pulsa **📅 Mes** → elige 30 días → descarga el ZIP.
2. Descomprime el ZIP. Ya tienes imágenes + textos listos para pegar.
3. *(Reels)* mete clips en `reel-video/videos_entrada/` y ejecuta:
   ```
   py reel_video.py --mes "ruta a la carpeta descomprimida"
   ```
4. Programa el mes en Meta Business Suite Planner (gratis).

---

## 🛠 Notas técnicas

- Sin build ni dependencias para el generador web: HTML + CSS + JS plano.
- El módulo de vídeo usa Python (`py`) + MoviePy (trae su propio FFmpeg).
- Exportación fija a 1080×1350 (feed 4:5) y 1080×1920 (reel 9:16).
- Repo: `github.com/Alderan7/posts`.
