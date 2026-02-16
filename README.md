# 🎓 LectureArchive

**Automated Polish Lecture Transcription System with Speaker Diarization**

A production-ready system for automatically transcribing lecture recordings with speaker identification, built with WhisperX and designed for daily automated processing.

---

## 🌟 Features

- ✅ **Automated Daily Processing** - Runs at 20:00 every day
- ✅ **Polish Language Support** - Optimized for Polish transcription
- ✅ **Speaker Diarization** - Identifies different speakers (SPEAKER_00, SPEAKER_01, etc.)
- ✅ **GPU Acceleration** - Fast processing with NVIDIA GPUs (RTX 3060 optimized)
- ✅ **Date-Organized Archives** - Files stored in DD.MM.YYYY folders
- ✅ **Comprehensive Logging** - Detailed logs of all operations
- ✅ **Error Handling** - Continues processing if one file fails
- ✅ **Fully Offline** - Works without internet after initial setup

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- FFmpeg
- NVIDIA GPU with CUDA 11.8+ (optional, for speed)
- HuggingFace account (for diarization)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/kacper1910kociszewski/LectureArchive.git
cd LectureArchive
```

2. **Create virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/macOS
```

3. **Install dependencies:**

For GPU (NVIDIA):
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
```

For CPU only:
```bash
pip install -r requirements.txt
```

4. **Login to HuggingFace:**
```bash
huggingface-cli login
# Paste your token from https://huggingface.co/settings/tokens
```

5. **Test the system:**
```bash
# Place an MP3 file in recordings/ folder
python auto_transcribe.py
```

📖 **Full setup guide:** See [SETUP.md](SETUP.md) for detailed instructions.

---

## 📁 Project Structure

```
LectureArchive/
│
├── recordings/              # Input: Place MP3 files here
├── archive/                 # Output: Transcribed files by date
│   └── DD.MM.YYYY/         # Date folders (e.g., 16.02.2026/)
│       ├── lecture1.mp3    # Original audio
│       └── lecture1.txt    # Transcript with speakers
├── logs/                    # System logs
│   └── transcription_log.txt
├── auto_transcribe.py       # Main script
├── requirements.txt         # Python dependencies
└── SETUP.md                # Detailed setup guide
```

---

## 🎯 How It Works

1. **Record lectures** on your phone or device
2. **Copy MP3 files** to `recordings/` folder
3. **At 20:00 daily**, the system automatically:
   - Scans for new MP3 files
   - Creates archive folder for today's date
   - Transcribes each file with Polish language model
   - Adds speaker labels (SPEAKER_00, SPEAKER_01, etc.)
   - Moves MP3 and transcript to archive
   - Logs all operations

**Result:** Clean `recordings/` folder and organized archive with searchable transcripts!

---

## ⏰ Setting Up Automation

### Windows Task Scheduler

1. Open Task Scheduler
2. Create new task
3. Set trigger: Daily at 20:00
4. Set action: Run `python.exe auto_transcribe.py`
5. Set start path to project directory

**Detailed instructions:** See [SETUP.md](SETUP.md#setting-up-daily-automation)

### Linux/macOS (cron)

```bash
crontab -e
# Add: 0 20 * * * cd /path/to/LectureArchive && /path/to/venv/bin/python auto_transcribe.py
```

---

## 🔧 Configuration

Edit `auto_transcribe.py` to customize:

```python
RECORDINGS_FOLDER = "recordings"  # Input folder
ARCHIVE_FOLDER = "archive"        # Output folder
WHISPER_MODEL = "medium"          # Model: tiny/base/small/medium/large-v2
LANGUAGE = "pl"                   # Language code (pl = Polish)
```

---

## 📊 Performance

### With RTX 3060 (8GB):
- **1 hour audio** → 5-10 minutes processing
- **GPU memory** → 4-6GB usage
- **Fully offline** after initial setup

### With CPU (Ryzen):
- **1 hour audio** → 30-60 minutes processing
- **Works reliably** but slower

---

## 🛠️ Troubleshooting

### Common Issues

**"WhisperX not found"**
```bash
pip install whisperx
```

**"FFmpeg not found"**
- Install FFmpeg and add to PATH
- Verify: `ffmpeg -version`

**"CUDA out of memory"**
- Use smaller model: `WHISPER_MODEL = "small"`
- Close other GPU applications

**Diarization fails**
```bash
huggingface-cli login
# Paste your token
```

📖 **More solutions:** See [SETUP.md](SETUP.md#troubleshooting)

---

## 📝 Example Output

### Input:
```
recordings/
└── historia_19.02.2026.mp3
```

### After Processing:
```
archive/
└── 19.02.2026/
    ├── historia_19.02.2026.mp3
    └── historia_19.02.2026.txt

logs/
└── transcription_log.txt
```

### Sample Transcript (`historia_19.02.2026.txt`):
```
[SPEAKER_00]: Dzień dobry, dzisiaj omówimy historię Polski w XVI wieku...
[SPEAKER_01]: Czy możemy zadać pytanie o reformację?
[SPEAKER_00]: Oczywiście, reformacja była kluczowym wydarzeniem...
```

---

## 🎓 Use Cases

- **Students:** Record and transcribe lectures automatically
- **Teachers:** Create searchable lecture archives
- **Researchers:** Transcribe interviews with speaker labels
- **Professionals:** Archive meetings and presentations

---

## 🔒 Privacy & Security

- **Fully offline processing** after initial setup
- **No data sent to cloud services**
- **Local AI models** cached on your machine
- **Your data stays on your computer**

---

## 🚀 Future Enhancements

Potential additions:
- Automatic subject detection from transcripts
- Weekly ZIP export of archives
- Email notifications on completion
- Web dashboard for browsing transcripts
- Multi-language support
- Integration with note-taking apps

---

## 📜 License

MIT License - See LICENSE file for details

---

## 🤝 Contributing

Contributions welcome! Please feel free to submit issues and pull requests.

---

## 📧 Support

For issues or questions:
1. Check [SETUP.md](SETUP.md) for detailed documentation
2. Review logs in `logs/transcription_log.txt`
3. Open an issue on GitHub

---

## 🙏 Acknowledgments

Built with:
- [WhisperX](https://github.com/m-bain/whisperX) - Fast transcription with diarization
- [OpenAI Whisper](https://github.com/openai/whisper) - Speech recognition
- [PyAnnote](https://github.com/pyannote/pyannote-audio) - Speaker diarization
- [PyTorch](https://pytorch.org/) - Deep learning framework

---

**⭐ Star this repo if you find it useful!**