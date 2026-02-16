# Testing the Transcription System

This guide explains how to test the system without real audio files.

## 🧪 Test Options

### Option 1: Quick Syntax Test

Test if the script runs without errors (no transcription):

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS

# Run with empty recordings folder
python auto_transcribe.py
```

Expected output:
```
[YYYY-MM-DD HH:MM:SS] ============================================================
[YYYY-MM-DD HH:MM:SS] STARTING AUTOMATED TRANSCRIPTION WORKFLOW
[YYYY-MM-DD HH:MM:SS] ============================================================
[YYYY-MM-DD HH:MM:SS] All dependencies verified successfully
[YYYY-MM-DD HH:MM:SS] No recordings found. Workflow skipped.
[YYYY-MM-DD HH:MM:SS] ============================================================
```

### Option 2: Test with Real Audio

To fully test the system, you need a real MP3 file:

1. **Get a test audio file:**
   - Record a short voice memo on your phone (30-60 seconds)
   - Convert to MP3 if needed
   - Or download a sample Polish audio file

2. **Place in recordings folder:**
   ```bash
   # Copy your test file
   cp /path/to/your/audio.mp3 recordings/
   ```

3. **Run transcription:**
   ```bash
   python auto_transcribe.py
   ```

4. **Check results:**
   - Transcript: `archive/DD.MM.YYYY/audio.txt`
   - Original: `archive/DD.MM.YYYY/audio.mp3`
   - Logs: `logs/transcription_log.txt`

### Option 3: Test Without WhisperX (Dry Run)

To test the file handling logic without actual transcription, create a mock test:

```bash
# Create a test file
echo "test" > recordings/test.mp3

# The script will try to process it
# It will likely fail on transcription (expected)
# But you can verify folder creation and file movement logic
```

## 🔍 What to Check

After running tests, verify:

### 1. Folder Structure
```bash
ls -R
```

Should show:
```
recordings/         # Empty after processing
archive/
  DD.MM.YYYY/      # Today's date folder
    test.mp3       # Moved file
    test.txt       # Transcript (if successful)
logs/
  transcription_log.txt  # Log file
```

### 2. Log Contents
```bash
cat logs/transcription_log.txt
```

Should contain:
- Timestamp for each operation
- File processing status
- Any errors encountered
- Summary statistics

### 3. Archive Contents
```bash
ls archive/*/
```

Should show processed files organized by date.

## 🎯 Expected Behavior

### Successful Run
```
[2026-02-16 20:00:00] ============================================================
[2026-02-16 20:00:00] STARTING AUTOMATED TRANSCRIPTION WORKFLOW
[2026-02-16 20:00:00] ============================================================
[2026-02-16 20:00:00] All dependencies verified successfully
[2026-02-16 20:00:00] Found 1 file(s) to process
[2026-02-16 20:00:00] Archive folder: archive/16.02.2026
[2026-02-16 20:00:00] ------------------------------------------------------------
[2026-02-16 20:00:00] Processing: lecture.mp3
[2026-02-16 20:00:00] Running transcription...
[2026-02-16 20:05:23] ✓ Successfully processed: lecture.mp3
[2026-02-16 20:05:23] ------------------------------------------------------------
[2026-02-16 20:05:23] ============================================================
[2026-02-16 20:05:23] WORKFLOW COMPLETED
[2026-02-16 20:05:23] Total files: 1
[2026-02-16 20:05:23] Successful: 1
[2026-02-16 20:05:23] Failed: 0
[2026-02-16 20:05:23] Archive location: archive/16.02.2026
[2026-02-16 20:05:23] ============================================================
```

### No Files Found
```
[2026-02-16 20:00:00] No recordings found. Workflow skipped.
```

### Error During Processing
```
[2026-02-16 20:00:00] Processing: corrupted.mp3
[2026-02-16 20:00:05] ✗ ERROR transcribing corrupted.mp3: ...
[2026-02-16 20:00:05] Failed: 1
```

## 🐛 Common Test Issues

### Issue: "whisperx: command not found"

**Cause:** WhisperX not installed or venv not activated

**Fix:**
```bash
# Ensure venv is activated (should see (venv) in prompt)
pip install whisperx
```

### Issue: "ffmpeg: command not found"

**Cause:** FFmpeg not installed or not in PATH

**Fix:**
- Install FFmpeg
- Add to system PATH
- Restart terminal

### Issue: Diarization fails

**Cause:** HuggingFace token not configured

**Fix:**
```bash
huggingface-cli login
# Paste your token
```

### Issue: File processed but no transcript

**Cause:** Audio file may be corrupted or wrong format

**Fix:**
- Verify file: `ffmpeg -i file.mp3`
- Re-encode if needed: `ffmpeg -i input.mp3 -ar 16000 output.mp3`

## 📊 Performance Testing

To test performance on your hardware:

1. **Prepare test file:** 1-hour MP3 recording
2. **Note start time:** Check your watch
3. **Run transcription:** `python auto_transcribe.py`
4. **Note end time:** Check completion time in logs
5. **Calculate:** End time - Start time = Processing time

**Expected times:**
- RTX 3060 GPU: 5-10 minutes
- Ryzen CPU: 30-60 minutes

## 🔄 Continuous Testing

For ongoing development:

1. **Keep test files:** Save a few small MP3s for quick testing
2. **Clear archive:** Periodically clean up test results
3. **Monitor logs:** Review logs after each test
4. **Check memory:** Monitor GPU/RAM usage during processing

## ✅ Test Checklist

Before considering the system ready:

- [ ] Script runs without syntax errors
- [ ] Empty recordings folder is handled correctly
- [ ] Files are transcribed successfully
- [ ] Transcripts contain expected content
- [ ] Original files are moved to archive
- [ ] Date folders are created correctly
- [ ] Logs are written properly
- [ ] Multiple files are processed in sequence
- [ ] Errors are handled gracefully (one file failure doesn't stop others)
- [ ] GPU is detected and used (if available)
- [ ] Task scheduler runs at scheduled time (if automated)

## 🚀 Next Steps

Once basic tests pass:

1. **Test with real lecture recordings**
2. **Verify Polish language accuracy**
3. **Test speaker diarization quality**
4. **Validate automation scheduling**
5. **Monitor for a week** to ensure reliability

---

**Remember:** The first run will download AI models (~2-5GB), so it will take longer than subsequent runs.
