@echo off
echo ========================================
echo  Discord Markdown Color Tool - Builder
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install pyperclip pyinstaller

echo.
echo Building EXE...
pyinstaller --onefile --console --name "DiscordMDColor" discord_color.py

echo.
echo ========================================
if exist "dist\DiscordMDColor.exe" (
    echo SUCCESS! EXE created at: dist\DiscordMDColor.exe
) else (
    echo Build may have failed - check for errors above
)
echo ========================================
pause
