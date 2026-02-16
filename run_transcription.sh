#!/bin/bash
# Helper script to run the transcription system manually

echo "========================================"
echo " Lecture Archive Transcription System"
echo "========================================"
echo ""

# Get the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if virtual environment exists
if [ ! -f "venv/bin/activate" ]; then
    echo "ERROR: Virtual environment not found!"
    echo "Please run setup first:"
    echo "  python3 -m venv venv"
    echo "  source venv/bin/activate"
    echo "  pip install -r requirements.txt"
    echo ""
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Run the transcription script
echo "Running transcription..."
echo ""
python auto_transcribe.py

# Show completion message
echo ""
echo "========================================"
echo " Process completed"
echo "========================================"
echo "Check logs/transcription_log.txt for details"
echo ""
