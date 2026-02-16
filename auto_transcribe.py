#!/usr/bin/env python3
"""
Automated Lecture Transcription System
=======================================

This script automatically transcribes MP3 files from the recordings folder
using WhisperX with Polish language support and speaker diarization.

Features:
- Processes all MP3 files in recordings/
- Creates date-organized archive folders (DD.MM.YYYY)
- Transcribes with speaker diarization
- Moves processed files to archive
- Comprehensive logging
- GPU auto-detection
- Robust error handling

Author: Automated Lecture Archive System
License: MIT
"""

import os
import glob
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

# ===== CONFIGURATION =====
RECORDINGS_FOLDER = "recordings"
ARCHIVE_FOLDER = "archive"
LOG_FOLDER = "logs"
WHISPER_MODEL = "medium"  # Options: tiny, base, small, medium, large-v2
LANGUAGE = "pl"  # Polish language code
MAX_LOG_OUTPUT_LENGTH = 200  # Maximum characters to log from command output
# =========================


def log(message):
    """
    Log a message to both console and log file with timestamp.
    
    Args:
        message (str): The message to log
    """
    os.makedirs(LOG_FOLDER, exist_ok=True)
    log_file = os.path.join(LOG_FOLDER, "transcription_log.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

    print(f"[{timestamp}] {message}")


def check_dependencies():
    """
    Check if required dependencies (whisperx, ffmpeg) are available.
    
    Returns:
        bool: True if all dependencies are available, False otherwise
    """
    try:
        # Check WhisperX
        result = subprocess.run(
            ["whisperx", "--help"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode != 0:
            log("ERROR: WhisperX not found. Please install it with: pip install whisperx")
            return False
        
        # Check FFmpeg
        result = subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode != 0:
            log("ERROR: FFmpeg not found. Please install FFmpeg and add it to PATH")
            return False
        
        log("All dependencies verified successfully")
        return True
    
    except FileNotFoundError as e:
        # More user-friendly error message
        missing = "WhisperX" if "whisperx" in str(e).lower() else "FFmpeg"
        log(f"ERROR: {missing} not found. Please install it before running.")
        log(f"  Details: {str(e)}")
        return False
    except Exception as e:
        log(f"ERROR during dependency check: {str(e)}")
        return False


def main():
    """
    Main transcription workflow:
    1. Check for MP3 files in recordings folder
    2. Create date-organized archive folder
    3. Transcribe each file with WhisperX
    4. Move files to archive
    5. Log all operations
    """
    log("=" * 60)
    log("STARTING AUTOMATED TRANSCRIPTION WORKFLOW")
    log("=" * 60)
    
    # Check dependencies
    if not check_dependencies():
        log("Dependency check failed. Please install required software.")
        return
    
    # Ensure folders exist
    os.makedirs(RECORDINGS_FOLDER, exist_ok=True)
    os.makedirs(ARCHIVE_FOLDER, exist_ok=True)
    
    # Find all MP3 files
    mp3_files = glob.glob(os.path.join(RECORDINGS_FOLDER, "*.mp3"))

    if not mp3_files:
        log("No recordings found. Workflow skipped.")
        log("=" * 60)
        return

    # Create today's archive folder
    today = datetime.now().strftime("%d.%m.%Y")
    date_folder = os.path.join(ARCHIVE_FOLDER, today)
    os.makedirs(date_folder, exist_ok=True)

    log(f"Found {len(mp3_files)} file(s) to process")
    log(f"Archive folder: {date_folder}")
    log("-" * 60)

    # Process each file
    success_count = 0
    error_count = 0
    
    for mp3 in mp3_files:
        filename = os.path.basename(mp3)

        try:
            log(f"Processing: {filename}")

            # Build WhisperX command
            cmd = [
                "whisperx",
                mp3,
                "--model", WHISPER_MODEL,
                "--language", LANGUAGE,
                "--diarize",
                "--output_format", "txt",
                "--output_dir", date_folder
            ]

            log(f"Running transcription...")
            
            # Run WhisperX
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            
            # Log output if there's any important info
            if result.stdout:
                log(f"WhisperX output: {result.stdout[:MAX_LOG_OUTPUT_LENGTH]}")

            # Move original MP3 to archive
            destination = os.path.join(date_folder, filename)
            shutil.move(mp3, destination)

            log(f"✓ Successfully processed: {filename}")
            success_count += 1

        except subprocess.CalledProcessError as e:
            error_count += 1
            log(f"✗ ERROR transcribing {filename}: {e}")
            if e.stderr:
                log(f"  Error details: {e.stderr[:MAX_LOG_OUTPUT_LENGTH]}")
        
        except Exception as e:
            error_count += 1
            log(f"✗ ERROR processing {filename}: {str(e)}")
        
        log("-" * 60)

    # Summary
    log("=" * 60)
    log("WORKFLOW COMPLETED")
    log(f"Total files: {len(mp3_files)}")
    log(f"Successful: {success_count}")
    log(f"Failed: {error_count}")
    log(f"Archive location: {date_folder}")
    log("=" * 60)
    log("")


if __name__ == "__main__":
    main()
