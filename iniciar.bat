@echo off
title Rosa Maria Studio — Iniciando...
cd /d "%~dp0"
color 0B
echo.
echo  ██████╗ ███╗   ███╗
echo  ██╔══██╗████╗ ████║
echo  ██████╔╝██╔████╔██║
echo  ██╔══██╗██║╚██╔╝██║
echo  ██║  ██║██║ ╚═╝ ██║
echo  ╚═╝  ╚═╝╚═╝     ╚═╝
echo.
echo  Rosa Maria Studio — Generador de Contenido
echo  ============================================
echo.

:: ── Intentar Python ──────────────────────────────
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo  [OK] Python encontrado. Arrancando servidor en puerto 8000...
    start "" "http://localhost:8000/rosa-maria-studio-2.html"
    python -m http.server 8000
    goto :fin
)

python3 --version >nul 2>&1
if %errorlevel% == 0 (
    echo  [OK] Python3 encontrado. Arrancando servidor en puerto 8000...
    start "" "http://localhost:8000/rosa-maria-studio-2.html"
    python3 -m http.server 8000
    goto :fin
)

:: ── Intentar Node.js ─────────────────────────────
node --version >nul 2>&1
if %errorlevel% == 0 (
    echo  [OK] Node.js encontrado. Arrancando servidor en puerto 3000...
    start "" "http://localhost:3000/rosa-maria-studio-2.html"
    npx --yes serve . -p 3000
    goto :fin
)

:: ── Ninguno disponible ───────────────────────────
echo.
echo  [!] No se encontro Python ni Node.js instalado.
echo.
echo  Instala uno de estos (gratis):
echo.
echo    Python:  https://www.python.org/downloads/
echo    Node.js: https://nodejs.org/
echo.
echo  Despues de instalar, cierra y vuelve a abrir este archivo.
echo.
pause
goto :fin

:fin
