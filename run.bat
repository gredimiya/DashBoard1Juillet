@echo off
setlocal
cd /d "%~dp0"

set PYTHON_EXE=.venv\Scripts\python.exe

if not exist "%PYTHON_EXE%" (
    py -3 -m venv .venv
)

if not exist "%PYTHON_EXE%" (
    echo Impossible de créer l'environnement virtuel.
    pause
    exit /b 1
)

"%PYTHON_EXE%" -m pip install --upgrade pip
"%PYTHON_EXE%" -m pip install -r requirements.txt
"%PYTHON_EXE%" -m streamlit run app.py

if errorlevel 1 (
    echo.
    echo Une erreur est survenue pendant le lancement de l'application.
    pause
)
