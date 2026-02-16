# ⚡ Quick Start Guide

Get up and running in minutes!

## 🎯 Goal

Set up automated Polish lecture transcription in 5 steps.

---

## ✅ Prerequisites Checklist

Before starting, ensure you have:

- [ ] Python 3.10+ installed
- [ ] FFmpeg installed and in PATH
- [ ] (Optional) NVIDIA GPU with CUDA for speed
- [ ] HuggingFace account created
- [ ] Internet connection (for initial setup only)

---

## 🚀 5-Minute Setup

### Step 1: Get the Code (1 min)

```bash
git clone https://github.com/kacper1910kociszewski/LectureArchive.git
cd LectureArchive
```

### Step 2: Create Environment (1 min)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies (2-3 min)

**With GPU (NVIDIA):**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
```

**CPU Only:**
```bash
pip install -r requirements.txt
```

### Step 4: Login to HuggingFace (30 sec)

```bash
huggingface-cli login
```
Paste your token from: https://huggingface.co/settings/tokens

### Step 5: Test It! (30 sec)

```bash
# Copy an MP3 file to recordings/
python auto_transcribe.py
```

**Done!** Check `archive/` for results.

---

## 📝 First Use

1. **Copy MP3 file** to `recordings/` folder
2. **Run manually** to test:
   ```bash
   python auto_transcribe.py
   ```
3. **Check output** in `archive/DD.MM.YYYY/`
4. **Review logs** in `logs/transcription_log.txt`

---

## ⏰ Set Up Automation (Optional)

### Windows - Task Scheduler

Quick steps:
1. Open Task Scheduler (`Win+R` → `taskschd.msc`)
2. Create Task → Name: "Lecture Transcription"
3. Trigger: Daily at 20:00
4. Action: Run `venv\Scripts\python.exe auto_transcribe.py`
5. Start in: Your LectureArchive folder path

📖 **Detailed guide:** See [SETUP.md](SETUP.md#setting-up-daily-automation)

### Linux/macOS - Cron

```bash
crontab -e
# Add this line (replace /path/to with actual path):
0 20 * * * cd /path/to/LectureArchive && /path/to/LectureArchive/venv/bin/python auto_transcribe.py
```

---

## 🎓 Usage Pattern

**Daily workflow:**
1. Record lectures during the day
2. Copy MP3 files to `recordings/` before 20:00
3. System runs automatically at 20:00
4. Next day: Find transcripts in `archive/`

**Or run manually anytime:**

**Windows:**
```bash
run_transcription.bat
```

**Linux/macOS:**
```bash
./run_transcription.sh
```

---

## 📊 What to Expect

### First Run
- Downloads AI models (~2-5GB)
- Takes 5-15 minutes for 1-hour audio
- Models cached for offline use

### Subsequent Runs
- Fully offline
- Faster (models cached)
- GPU: 5-10 min per hour
- CPU: 30-60 min per hour

---

## 🆘 Quick Troubleshooting

### "Command not found" errors
```bash
# Verify installations:
python --version    # Should show 3.10+
ffmpeg -version     # Should show FFmpeg info
```

### "Module not found" errors
```bash
# Ensure venv is activated (you should see (venv) in prompt)
pip install -r requirements.txt
```

### GPU not detected
- Check: `nvidia-smi`
- Reinstall PyTorch with CUDA support
- System falls back to CPU automatically

### Diarization fails
```bash
# Login to HuggingFace:
huggingface-cli login
```

---

## 📁 Project Structure

```
LectureArchive/
├── recordings/          ← Put MP3 files here
├── archive/            ← Find transcripts here
│   └── DD.MM.YYYY/
├── logs/               ← Check logs here
├── auto_transcribe.py  ← Main script
└── requirements.txt    ← Dependencies
```

---

## 🎯 Next Steps

Once basic setup works:

1. **📖 Read full documentation:** [SETUP.md](SETUP.md)
2. **⚙️ Customize settings:** [CONFIGURATION.md](CONFIGURATION.md)
3. **🤖 Set up automation:** [SETUP.md](SETUP.md#setting-up-daily-automation)
4. **🚀 Try different models:** Edit `WHISPER_MODEL` in script

---

## 💡 Pro Tips

- **First test with short audio** (1-2 minutes) to verify setup
- **Use medium model** for Polish (best accuracy/speed balance)
- **GPU gives 5-10x speedup** over CPU
- **System works offline** after first run downloads models
- **Check logs** if something goes wrong

---

## 📖 Full Documentation

- [SETUP.md](SETUP.md) - Complete setup instructions
- [CONFIGURATION.md](CONFIGURATION.md) - Customization options
- [README.md](README.md) - Full project documentation

---

**🎉 You're ready to go! Start recording and transcribing!**
