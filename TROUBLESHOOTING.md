# 🔧 Troubleshooting Guide

Common issues and solutions for the Lecture Archive system.

---

## 📋 Quick Diagnostics

Run these checks first:

```bash
# 1. Check Python
python --version
# Expected: Python 3.10.x or higher

# 2. Check FFmpeg
ffmpeg -version
# Expected: FFmpeg version info

# 3. Check virtual environment
# Windows: Should see (venv) in prompt
# Linux/macOS: Should see (venv) in prompt

# 4. Check WhisperX (in venv)
whisperx --help
# Expected: WhisperX help text

# 5. Check GPU (NVIDIA only)
nvidia-smi
# Expected: GPU info, or "command not found" if CPU-only
```

---

## 🚨 Common Issues

### Issue: "python: command not found"

**Cause:** Python not installed or not in PATH

**Solutions:**

**Windows:**
1. Download Python from https://www.python.org
2. Run installer
3. ✔ Check "Add Python to PATH"
4. Restart Command Prompt
5. Verify: `python --version`

**Linux:**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**macOS:**
```bash
brew install python@3.10
```

---

### Issue: "ffmpeg: command not found"

**Cause:** FFmpeg not installed or not in PATH

**Solutions:**

**Windows:**
1. Download from https://www.gyan.dev/ffmpeg/builds/
2. Extract to `C:\ffmpeg`
3. Add to PATH:
   - Windows Key → "Environment Variables"
   - Edit "Path"
   - Add `C:\ffmpeg\bin`
4. Restart Command Prompt
5. Verify: `ffmpeg -version`

**Linux:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

---

### Issue: "whisperx: command not found"

**Cause:** WhisperX not installed or venv not activated

**Solutions:**

1. **Activate virtual environment:**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/macOS
   source venv/bin/activate
   ```
   You should see `(venv)` in your prompt

2. **Install WhisperX:**
   ```bash
   pip install whisperx
   ```

3. **Verify installation:**
   ```bash
   whisperx --help
   ```

---

### Issue: "ModuleNotFoundError: No module named 'whisperx'"

**Cause:** Running script outside virtual environment

**Solutions:**

1. **Always activate venv first:**
   ```bash
   cd LectureArchive
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/macOS
   ```

2. **Then run script:**
   ```bash
   python auto_transcribe.py
   ```

**Pro Tip:** Use the helper scripts:
- Windows: `run_transcription.bat`
- Linux/macOS: `./run_transcription.sh`

---

### Issue: "CUDA out of memory"

**Cause:** GPU doesn't have enough VRAM for the model

**Solutions:**

**Option 1 - Use smaller model:**
```python
# Edit auto_transcribe.py
WHISPER_MODEL = "small"  # Instead of "medium"
```

**Option 2 - Close other GPU applications:**
- Close games
- Close video editors
- Close other AI applications

**Option 3 - Use CPU mode:**
```bash
# Reinstall PyTorch without CUDA
pip uninstall torch torchvision torchaudio
pip install torch torchvision torchaudio
```

**Option 4 - Reduce batch size:**
```python
# In auto_transcribe.py, add to cmd:
"--batch_size", "8"  # Default is 16
```

---

### Issue: Diarization fails / "pyannote.audio error"

**Cause:** HuggingFace authentication not configured

**Solutions:**

1. **Create HuggingFace account:**
   - Go to https://huggingface.co
   - Sign up

2. **Create access token:**
   - Settings → Access Tokens
   - Create new token (read access)
   - Copy token

3. **Login via CLI:**
   ```bash
   huggingface-cli login
   ```
   Paste your token when prompted

4. **Test again:**
   ```bash
   python auto_transcribe.py
   ```

---

### Issue: "Transcription is very slow"

**Symptoms:** 1 hour audio takes 2+ hours to process

**Diagnosis:**
```bash
# Check if GPU is being used
nvidia-smi

# While script is running, GPU usage should show
```

**Solutions:**

**If GPU not detected:**
1. Install CUDA Toolkit
2. Reinstall PyTorch with CUDA:
   ```bash
   pip uninstall torch torchvision torchaudio
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

**If GPU detected but still slow:**
1. Use smaller model: `tiny` or `base`
2. Check GPU isn't being used by other processes
3. Update GPU drivers

**If on CPU (no GPU):**
- Expected behavior (CPU is 5-10x slower)
- Use smaller model for faster processing
- Process overnight

---

### Issue: Script runs but no transcripts created

**Symptoms:** MP3 files moved to archive, but no .txt files

**Diagnosis:**
```bash
# Check logs
cat logs/transcription_log.txt
# Look for error messages
```

**Common Causes:**

**1. WhisperX failed silently:**
```bash
# Test WhisperX directly
whisperx your_file.mp3 --model small --language pl --output_format txt --output_dir test_output
```

**2. Output format issue:**
Check `auto_transcribe.py`:
```python
"--output_format", "txt"  # Should be "txt"
```

**3. Permission issues:**
```bash
# Check write permissions
ls -la archive/
```

---

### Issue: "Task Scheduler: Task not running"

**Diagnosis:**
1. Open Task Scheduler
2. Find "Lecture Transcription" task
3. Right-click → Properties
4. Check "Last Run Result" column

**Common Issues:**

**Last Run Result: 0x1 (Incorrect path):**
- Verify paths are absolute, not relative
- Example: `C:\Users\YourName\LectureArchive\venv\Scripts\python.exe`
- NOT: `.\venv\Scripts\python.exe`

**Last Run Result: 0x2 (File not found):**
- Check "Start in" path is correct
- Should be: `C:\Users\YourName\LectureArchive`

**Task shows as "Running" forever:**
- Task might be waiting for input
- Check log file for errors
- Disable "Stop if runs longer than" or set to 3 hours

**Task doesn't trigger:**
- Verify trigger is enabled
- Check time is correct
- Ensure computer is on at scheduled time
- Disable "Start only if computer is idle"

---

### Issue: "cron job not running" (Linux/macOS)

**Diagnosis:**
```bash
# Check cron logs
grep CRON /var/log/syslog  # Linux
log show --predicate 'process == "cron"' --last 1h  # macOS
```

**Solutions:**

**1. Verify crontab entry:**
```bash
crontab -l
# Should show your entry
```

**2. Use absolute paths:**
```bash
# Bad:
0 20 * * * cd LectureArchive && python auto_transcribe.py

# Good:
0 20 * * * cd /home/user/LectureArchive && /home/user/LectureArchive/venv/bin/python auto_transcribe.py
```

**3. Add logging:**
```bash
0 20 * * * cd /path/to/LectureArchive && /path/to/venv/bin/python auto_transcribe.py >> /path/to/cron.log 2>&1
```

**4. Check permissions:**
```bash
chmod +x /path/to/LectureArchive/auto_transcribe.py
```

---

### Issue: "Wrong language detected"

**Symptoms:** Transcript in wrong language or gibberish

**Solutions:**

**1. Specify language explicitly:**
```python
# In auto_transcribe.py
LANGUAGE = "pl"  # For Polish
```

**2. Verify audio quality:**
- Audio should be clear
- No excessive background noise
- Speaker should be audible

**3. Try larger model:**
```python
WHISPER_MODEL = "medium"  # Or "large-v2"
```

---

### Issue: "Polish characters (ą, ę, ł) appear as ?"

**Cause:** Encoding issue when viewing file

**Solutions:**

**1. Use UTF-8 compatible editor:**
- VS Code (default UTF-8)
- Notepad++ (Encoding → UTF-8)
- Sublime Text (File → Save with Encoding → UTF-8)

**2. Windows Notepad:**
- File → Save As
- Encoding: UTF-8
- Save

**3. Command line:**
```bash
# Linux/macOS (should work by default)
cat file.txt

# Windows (set console to UTF-8)
chcp 65001
type file.txt
```

---

### Issue: "Speakers not differentiated"

**Symptoms:** All text labeled as SPEAKER_00

**Causes:**
1. Only one person speaking
2. Speakers too similar (same gender, pitch)
3. Poor audio quality
4. Microphone too far from secondary speakers

**Solutions:**

**1. Improve recording setup:**
- Use higher quality microphone
- Position mic to capture all speakers
- Record in stereo if possible

**2. Adjust diarization parameters:**
```python
# In auto_transcribe.py, modify cmd:
cmd = [
    "whisperx",
    mp3,
    "--model", WHISPER_MODEL,
    "--language", LANGUAGE,
    "--diarize",
    "--min_speakers", "2",  # Add this
    "--max_speakers", "4",  # Add this
    "--output_format", "txt",
    "--output_dir", date_folder
]
```

**3. Use better model:**
```python
WHISPER_MODEL = "large-v2"
```

---

### Issue: "FileNotFoundError" or "Permission denied"

**Cause:** Folder permissions or missing folders

**Solutions:**

**1. Check folder exists:**
```bash
ls recordings/
ls archive/
ls logs/
```

**2. Check permissions:**
```bash
# Linux/macOS
ls -la recordings/ archive/ logs/

# Should show write permissions
```

**3. Recreate folders:**
```bash
mkdir -p recordings archive logs
```

**4. Windows - Run as Administrator:**
- Right-click script
- "Run as administrator"

---

### Issue: "Script crashes in the middle"

**Symptoms:** Some files processed, then crash

**Diagnosis:**
```bash
# Check last log entry
tail -20 logs/transcription_log.txt
```

**Common Causes:**

**1. Out of memory:**
- Close other applications
- Use smaller model
- Process fewer files at once

**2. Corrupted audio file:**
- Test file: `ffmpeg -i suspect.mp3 -f null -`
- Re-encode: `ffmpeg -i corrupt.mp3 -ar 16000 fixed.mp3`

**3. System going to sleep:**
- Disable sleep mode during processing
- Windows: Power settings
- Linux: `systemd-inhibit`

---

## 🔍 Advanced Debugging

### Enable verbose logging

```python
# In auto_transcribe.py, modify subprocess.run:
result = subprocess.run(
    cmd,
    capture_output=True,
    text=True,
    check=True
)

# Add after subprocess.run:
if result.stdout:
    log(f"STDOUT: {result.stdout}")
if result.stderr:
    log(f"STDERR: {result.stderr}")
```

### Test WhisperX directly

```bash
# Activate venv
venv\Scripts\activate

# Test single file
whisperx test.mp3 \
  --model small \
  --language pl \
  --diarize \
  --output_format txt \
  --output_dir output_test/

# Check output
ls output_test/
cat output_test/test.txt
```

### Check Python package versions

```bash
pip list | grep -E "(whisperx|torch|pyannote)"
```

### Test GPU availability

```python
python -c "import torch; print('CUDA available:', torch.cuda.is_available()); print('GPU:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None')"
```

---

## 📞 Getting Help

If issues persist:

1. **Check logs:**
   ```bash
   cat logs/transcription_log.txt
   ```

2. **Create minimal test case:**
   - Use short (30 sec) audio file
   - Test with simple command
   - Note exact error message

3. **Gather information:**
   - Python version: `python --version`
   - OS version
   - GPU model (if applicable)
   - Error messages
   - Log file contents

4. **Check GitHub issues:**
   - WhisperX: https://github.com/m-bain/whisperX/issues
   - This project: [GitHub Issues](https://github.com/kacper1910kociszewski/LectureArchive/issues)

5. **Create issue with:**
   - Clear description of problem
   - Steps to reproduce
   - Error messages
   - System information
   - What you've tried

---

## ✅ Prevention Checklist

Avoid issues before they happen:

- [ ] Use virtual environment (always activate)
- [ ] Install all dependencies before first run
- [ ] Test with short audio first
- [ ] Keep models updated
- [ ] Monitor disk space (models need 2-10GB)
- [ ] Check GPU memory regularly
- [ ] Back up archive folder
- [ ] Review logs periodically
- [ ] Test automation before relying on it
- [ ] Keep Python and packages updated

---

**Remember:** Most issues are dependency-related. Always ensure your virtual environment is activated and all packages are installed correctly.
