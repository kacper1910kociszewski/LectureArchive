@echo off
REM Helper script to run the transcription system manually

echo ========================================
echo  Lecture Archive Transcription System
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ERROR: Virtual environment not found!
    echo Please run setup first:
    echo   python -m venv venv
    echo   venv\Scripts\activate
    echo   pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Run the transcription script
echo Running transcription...
echo.
python auto_transcribe.py

REM Keep window open to see results
echo.
echo ========================================
echo  Process completed
echo ========================================
echo Check logs\transcription_log.txt for details
echo.
pause
