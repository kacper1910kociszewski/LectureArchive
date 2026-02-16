# 🚀 Automated Lecture Archive - Setup Guide

Complete installation and configuration guide for the automated lecture transcription system.

---

## 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Installation Steps](#installation-steps)
3. [Configuration](#configuration)
4. [Setting Up Daily Automation](#setting-up-daily-automation)
5. [Usage](#usage)
6. [Troubleshooting](#troubleshooting)

---

## 🖥 System Requirements

### Hardware

**Recommended (Desktop with RTX 3060 8GB):**
- GPU acceleration for fast transcription
- ~5-10 minutes per 1 hour of audio
- GPU memory usage: 4-6GB

**Alternative (Laptop with Ryzen CPU):**
- CPU-only mode (slower)
- ~30-60 minutes per 1 hour of audio
- Works but not optimal

### Software

- **Python 3.10+** (3.10 recommended)
- **FFmpeg** (audio processing)
- **CUDA Toolkit 11.8+** (optional, for GPU acceleration)
- **HuggingFace account** (required for speaker diarization)

---

## 📦 Installation Steps

### Step 1: Install Python 3.10

1. Download from: https://www.python.org/downloads/
2. During installation:
   - ✔ Check "Add Python to PATH"
   - ✔ Check "Install pip"

3. Verify installation:
```bash
python --version
# Should show: Python 3.10.x or higher
```

---

### Step 2: Install FFmpeg

FFmpeg is required for audio file processing.

#### Windows:
1. Download from: https://www.gyan.dev/ffmpeg/builds/
2. Extract to `C:\ffmpeg`
3. Add to PATH:
   - Open System Environment Variables
   - Edit Path variable
   - Add: `C:\ffmpeg\bin`

4. Verify installation:
```bash
ffmpeg -version
# Should show FFmpeg version info
```

#### Linux:
```bash
sudo apt update
sudo apt install ffmpeg
```

#### macOS:
```bash
brew install ffmpeg
```

---

### Step 3: Install CUDA (GPU Users Only)

If using NVIDIA GPU (like RTX 3060):

1. Check GPU availability:
```bash
nvidia-smi
# Should show your GPU info
```

2. Install CUDA Toolkit 11.8 or compatible:
   - Download from: https://developer.nvidia.com/cuda-downloads
   - Follow installer instructions

---

### Step 4: Clone Repository

```bash
# Clone the repository
git clone https://github.com/kacper1910kociszewski/LectureArchive.git
cd LectureArchive
```

---

### Step 5: Create Virtual Environment

**Important:** Always use a virtual environment to avoid conflicts.

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

---

### Step 6: Install Python Dependencies

#### For GPU (NVIDIA):
```bash
# Install PyTorch with CUDA support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install WhisperX and other dependencies
pip install -r requirements.txt
```

#### For CPU Only:
```bash
# Install all dependencies (PyTorch CPU version)
pip install -r requirements.txt
```

---

### Step 7: HuggingFace Authentication

**Required for speaker diarization feature.**

1. Create account at: https://huggingface.co
2. Go to Settings → Access Tokens
3. Create a new token (read access is sufficient)
4. Login via CLI:

```bash
huggingface-cli login
```

5. Paste your token when prompted

---

## ⚙️ Configuration

### Folder Structure

The system uses these folders:

```
LectureArchive/
│
├── recordings/          # Place MP3 files here
├── archive/            # Transcribed files organized by date
├── logs/               # System logs
├── auto_transcribe.py  # Main script
└── requirements.txt    # Dependencies
```

### Script Configuration

Edit `auto_transcribe.py` if needed:

```python
# Configuration section (lines 29-33)
RECORDINGS_FOLDER = "recordings"  # Input folder
ARCHIVE_FOLDER = "archive"        # Output folder
LOG_FOLDER = "logs"               # Log folder
WHISPER_MODEL = "medium"          # Model size: tiny, base, small, medium, large-v2
LANGUAGE = "pl"                   # Language code (pl = Polish)
```

**Model sizes:**
- `tiny`: Fastest, least accurate (~1GB VRAM)
- `base`: Fast, decent accuracy (~1.5GB VRAM)
- `small`: Balanced (~2GB VRAM)
- `medium`: Recommended for Polish (~5GB VRAM)
- `large-v2`: Best accuracy, slowest (~10GB VRAM)

---

## ⏰ Setting Up Daily Automation

### Windows Task Scheduler

1. **Open Task Scheduler**
   - Press `Win + R`
   - Type `taskschd.msc`
   - Press Enter

2. **Create New Task**
   - Click "Create Task" (not "Create Basic Task")
   - Name: `Lecture Transcription`
   - Description: `Daily automated lecture transcription at 20:00`
   - Select "Run whether user is logged on or not"

3. **Triggers Tab**
   - Click "New"
   - Begin the task: `On a schedule`
   - Settings: `Daily`
   - Start time: `20:00:00`
   - Click OK

4. **Actions Tab**
   - Click "New"
   - Action: `Start a program`
   - Program/script: 
     ```
     C:\path\to\LectureArchive\venv\Scripts\python.exe
     ```
   - Add arguments:
     ```
     auto_transcribe.py
     ```
   - Start in:
     ```
     C:\path\to\LectureArchive
     ```
   - Click OK

5. **Settings Tab**
   - ✔ Allow task to be run on demand
   - ✔ Stop task if it runs longer than 3 hours
   - Click OK

6. **Test the Task**
   - Right-click the task
   - Select "Run"
   - Check logs folder for output

### Linux/macOS (cron)

1. Edit crontab:
```bash
crontab -e
```

2. Add this line:
```bash
0 20 * * * cd /path/to/LectureArchive && /path/to/LectureArchive/venv/bin/python auto_transcribe.py
```

3. Save and exit

---

## 📖 Usage

### Daily Workflow

1. **Record lectures** on your phone/device
2. **Copy MP3 files** to `recordings/` folder
3. **At 20:00**, the script automatically:
   - Finds all MP3 files
   - Creates archive folder: `archive/DD.MM.YYYY/`
   - Transcribes each file (Polish + speaker diarization)
   - Moves MP3 and transcript to archive
   - Logs everything

### Manual Run

To run manually at any time:

```bash
# Activate virtual environment first
cd LectureArchive
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/macOS

# Run the script
python auto_transcribe.py
```

### Output Structure

After processing, you'll have:

```
archive/
└── 16.02.2026/
    ├── lecture1.mp3
    ├── lecture1.txt      # Transcript with speaker labels
    ├── lecture2.mp3
    └── lecture2.txt

logs/
└── transcription_log.txt  # Detailed processing logs
```

---

## 🔧 Troubleshooting

### Issue: "WhisperX not found"

**Solution:**
```bash
pip install whisperx
```

### Issue: "FFmpeg not found"

**Solution:**
- Verify FFmpeg is installed: `ffmpeg -version`
- Ensure FFmpeg's `bin` folder is in PATH
- Restart terminal after adding to PATH

### Issue: "CUDA out of memory"

**Solutions:**
1. Use smaller model:
   ```python
   WHISPER_MODEL = "small"  # Instead of "medium"
   ```
2. Close other GPU-using applications
3. Use CPU mode (slower but works)

### Issue: Diarization fails

**Cause:** HuggingFace token not configured

**Solution:**
```bash
huggingface-cli login
# Paste your token
```

### Issue: Script doesn't run automatically

**Windows Task Scheduler:**
1. Check task is enabled
2. Verify paths are absolute (not relative)
3. Check "Last Run Result" column
4. View task history for errors

**Linux/macOS cron:**
```bash
# Check cron logs
grep CRON /var/log/syslog
```

### Issue: Transcription is slow

**Solutions:**
- Use GPU instead of CPU
- Use smaller model (`small` or `base`)
- Ensure CUDA is properly installed
- Close other applications using GPU

### Issue: Audio file not recognized

**Solutions:**
- Ensure file is actually MP3 format
- Check file is not corrupted: `ffmpeg -i file.mp3`
- Verify file has .mp3 extension

---

## 📊 Performance Expectations

### With RTX 3060 (8GB):
- 1 hour audio → 5-10 minutes processing
- GPU memory usage: 4-6GB
- Fully offline processing

### With CPU (Ryzen):
- 1 hour audio → 30-60 minutes processing
- Higher CPU usage
- Fully offline processing

---

## 🎯 What's Included

✅ Automated daily transcription at 20:00  
✅ Polish language support  
✅ Speaker diarization (who said what)  
✅ Date-organized archive  
✅ Comprehensive logging  
✅ Error handling (continues if one file fails)  
✅ GPU auto-detection  
✅ Fully offline operation  

---

## 🚀 Next Steps

After basic setup works, you can enhance with:
- Automatic subject detection from transcripts
- Weekly ZIP export of archives
- Email notifications when processing completes
- Web dashboard for browsing transcripts
- Multi-language support

---

## 📝 Notes

- First run downloads AI models (~1-5GB depending on model size)
- Models are cached locally for offline use
- System works completely offline after initial setup
- Processing time depends on audio length and hardware

---

## 🆘 Support

If you encounter issues:
1. Check logs in `logs/transcription_log.txt`
2. Verify all dependencies are installed
3. Test manual run before automating
4. Check GPU availability if using GPU mode

For more help, check the [GitHub repository](https://github.com/kacper1910kociszewski/LectureArchive).
