@echo off
echo ========================================
echo  Discord MD Color Tool GUI - Builder
echo ========================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not installed
    pause
    exit /b 1
)

echo Installing dependencies...
pip install pyinstaller

echo.
echo Building GUI EXE (no console window)...
pyinstaller --onefile --windowed --name "DiscordMDColorGUI" discord_color_gui.py

echo.
if exist "dist\DiscordMDColorGUI.exe" (
    echo SUCCESS! GUI EXE at: dist\DiscordMDColorGUI.exe
) else (
    echo Build failed - check errors
)
pause
