@echo off
cd /d "%~dp0"
python -m PyInstaller --noconfirm --onefile --name PanjatSengsara --add-data "game.html;." --add-data "three.min.js;." app.py
echo.
echo Hasil: dist\PanjatSengsara.exe
pause
