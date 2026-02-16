# Configuration Example

## Customizing the Transcription System

You can customize the behavior by editing `auto_transcribe.py`:

### Model Selection

Choose the right model for your needs:

```python
WHISPER_MODEL = "medium"  # Change this line
```

**Available options:**

| Model | Speed | Accuracy | VRAM | Use Case |
|-------|-------|----------|------|----------|
| `tiny` | Fastest | Lowest | ~1GB | Quick tests |
| `base` | Fast | Good | ~1.5GB | Fast processing |
| `small` | Medium | Better | ~2GB | Balanced |
| `medium` | Slower | Great | ~5GB | **Recommended for Polish** |
| `large-v2` | Slowest | Best | ~10GB | Maximum accuracy |

### Language Support

Change the language code:

```python
LANGUAGE = "pl"  # Polish
```

**Other common codes:**
- `en` - English
- `de` - German
- `es` - Spanish
- `fr` - French
- `it` - Italian

### Folder Paths

Customize folder locations:

```python
RECORDINGS_FOLDER = "recordings"  # Input folder
ARCHIVE_FOLDER = "archive"        # Output folder  
LOG_FOLDER = "logs"               # Logs folder
```

**Example for custom structure:**
```python
RECORDINGS_FOLDER = "input/audio"
ARCHIVE_FOLDER = "output/transcripts"
LOG_FOLDER = "output/logs"
```

### Advanced WhisperX Options

For advanced users, you can modify the command in `auto_transcribe.py`:

```python
cmd = [
    "whisperx",
    mp3,
    "--model", WHISPER_MODEL,
    "--language", LANGUAGE,
    "--diarize",                    # Speaker identification
    "--output_format", "txt",       # Output format (txt, srt, vtt, json)
    "--output_dir", date_folder,
    # Add more options here:
    # "--min_speakers", "2",        # Minimum speakers
    # "--max_speakers", "4",        # Maximum speakers
    # "--compute_type", "float16",  # Precision (float16, int8)
]
```

## Output Formats

Change output format by modifying:

```python
"--output_format", "txt"
```

**Available formats:**
- `txt` - Plain text (default)
- `srt` - Subtitle format with timestamps
- `vtt` - WebVTT subtitles
- `json` - JSON format with metadata

## Scheduling Times

To change the daily run time, modify your scheduler:

### Windows Task Scheduler
1. Open Task Scheduler
2. Find "Lecture Transcription" task
3. Edit trigger → Change time

### Linux/macOS cron
Edit crontab:
```bash
crontab -e

# Change hour (0-23) and minute (0-59)
# Format: MIN HOUR DAY MONTH DAYOFWEEK COMMAND
0 20 * * * /path/to/command  # 20:00 (8:00 PM)
30 18 * * * /path/to/command # 18:30 (6:30 PM)
```

## Performance Tuning

### For Faster Processing (Less Accuracy)
```python
WHISPER_MODEL = "small"
```

### For Better Accuracy (Slower)
```python
WHISPER_MODEL = "large-v2"
```

### For Lower Memory Usage
Use compute type in the command:
```python
"--compute_type", "int8"  # Uses less memory, slightly lower accuracy
```

## Multiple Languages

To support multiple languages, you can:

1. Remove language parameter (auto-detect):
```python
# Remove this line from cmd:
# "--language", LANGUAGE,
```

2. Or create separate configurations for different folders

## Logging Verbosity

To adjust logging detail, modify the `log()` function:

```python
def log(message):
    # Add/remove console output
    print(f"[{timestamp}] {message}")  # Remove this line for quiet mode
    
    # Keep file logging
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")
```

## Example: Multi-Language Setup

For processing multiple languages:

```python
# Detect language automatically
cmd = [
    "whisperx",
    mp3,
    "--model", "medium",
    # No --language parameter = auto-detect
    "--diarize",
    "--output_format", "txt",
    "--output_dir", date_folder
]
```

## Example: Custom Archive Naming

To change date format in archive folders:

```python
# Current: DD.MM.YYYY (16.02.2026)
today = datetime.now().strftime("%d.%m.%Y")

# Alternative formats:
today = datetime.now().strftime("%Y-%m-%d")      # 2026-02-16 (ISO format)
today = datetime.now().strftime("%Y%m%d")        # 20260216 (compact)
today = datetime.now().strftime("%B_%d_%Y")     # February_16_2026
```

## Testing Configuration

After making changes, test with:

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/macOS

# Place a test MP3 in recordings/
# Run script
python auto_transcribe.py

# Check results in archive/ and logs/
```
