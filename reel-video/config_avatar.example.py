# -*- coding: utf-8 -*-
# ─────────────────────────────────────────────────────────────────────────
# CONFIG del reel con avatar + voz (HeyGen).  COPIA este archivo a:
#     config_avatar.py
# y rellena tus datos. config_avatar.py está en .gitignore (NO se sube).
# ─────────────────────────────────────────────────────────────────────────

# 1) API key de HeyGen  (HeyGen → Settings → API)
HEYGEN_API_KEY = "pega_aqui_tu_api_key_de_heygen"

# 2) Tu foto-avatar. Sácalo con:  py reel_avatar.py --subir-foto "../FOTO PERFIL PROFESIONAL.png"
TALKING_PHOTO_ID = ""

# 3) Tu voz clonada. Sácalo con:  py reel_avatar.py --listar
#    (conecta antes tu ElevenLabs en HeyGen → Settings → Integrations)
VOICE_ID = ""

# 4) Formato del vídeo (9:16 vertical). 720x1280 va en todos los planes;
#    1080x1920 puede requerir plan superior en HeyGen.
WIDTH = 720
HEIGHT = 1280
SPEED = 1.0   # velocidad de habla (1.0 = normal)
