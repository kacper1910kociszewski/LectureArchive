# 📚 Example Workflow

Real-world usage examples for the Lecture Archive system.

---

## 🎓 Student Use Case

**Scenario:** University student recording 4 lectures per day

### Daily Routine

**Morning-Afternoon:**
1. Attend lectures
2. Record with phone voice recorder app
3. Save files with descriptive names:
   - `matematyka_16.02.2026.mp3`
   - `fizyka_16.02.2026.mp3`
   - `chemia_16.02.2026.mp3`
   - `historia_16.02.2026.mp3`

**Evening (before 20:00):**
1. Connect phone to computer
2. Copy MP3 files to `recordings/` folder
3. Disconnect phone

**At 20:00:**
- System runs automatically
- Transcribes all 4 files
- Creates `archive/16.02.2026/` folder

**Next Morning:**
```
archive/16.02.2026/
├── matematyka_16.02.2026.mp3
├── matematyka_16.02.2026.txt
├── fizyka_16.02.2026.mp3
├── fizyka_16.02.2026.txt
├── chemia_16.02.2026.mp3
├── chemia_16.02.2026.txt
├── historia_16.02.2026.mp3
└── historia_16.02.2026.txt
```

**Benefits:**
- Searchable text transcripts for studying
- Speaker labels help identify professor vs. students
- Organized by date for easy retrieval
- Can search all transcripts for specific topics

---

## 👨‍🏫 Teacher Use Case

**Scenario:** Teacher creating lecture archive

### Weekly Routine

**Monday-Friday:**
1. Record each lecture during class
2. Name files by subject and topic:
   - `biology_cell_division_15.02.2026.mp3`
   - `biology_genetics_16.02.2026.mp3`

**Evening:**
1. Transfer recordings to `recordings/` folder
2. Let system process overnight

**End of Week:**
```
archive/
├── 15.02.2026/
│   ├── biology_cell_division_15.02.2026.mp3
│   └── biology_cell_division_15.02.2026.txt
├── 16.02.2026/
│   ├── biology_genetics_16.02.2026.mp3
│   └── biology_genetics_16.02.2026.txt
├── 17.02.2026/
│   ├── biology_evolution_17.02.2026.mp3
│   └── biology_evolution_17.02.2026.txt
└── ...
```

**Benefits:**
- Reusable lecture content year-to-year
- Students can request specific lecture transcripts
- Easy to review what was covered
- Helps with lesson planning

---

## 🔬 Researcher Use Case

**Scenario:** Researcher conducting interviews

### Project Workflow

**Interview Phase:**
1. Record 2-3 interviews per week
2. Name with participant codes:
   - `interview_P001_10.02.2026.mp3`
   - `interview_P002_11.02.2026.mp3`

**Processing:**
- System transcribes with speaker labels
- SPEAKER_00 = Interviewer
- SPEAKER_01 = Participant

**Analysis Phase:**
```bash
# Search all transcripts for specific topics
grep -r "climate change" archive/
grep -r "social impact" archive/
```

**Benefits:**
- Exact quotes with speaker attribution
- Searchable corpus of interviews
- Time-stamped references
- Privacy-preserving (all local processing)

---

## 🏢 Professional Use Case

**Scenario:** Small team weekly meetings

### Meeting Routine

**During Meeting:**
1. Record with laptop/phone
2. Name: `team_meeting_16.02.2026.mp3`

**After Meeting:**
1. Move recording to `recordings/`
2. Run immediately or wait for daily processing

**Result:**
```
archive/16.02.2026/
├── team_meeting_16.02.2026.mp3
└── team_meeting_16.02.2026.txt
```

Sample transcript:
```
[SPEAKER_00]: Let's review last week's progress.
[SPEAKER_01]: I completed the frontend updates.
[SPEAKER_02]: Backend API is deployed to staging.
[SPEAKER_00]: Great! What about testing?
[SPEAKER_01]: QA starts Monday.
```

**Benefits:**
- Meeting minutes without manual note-taking
- Reference for action items
- Resolve disputes about who said what
- Onboarding new team members (review past meetings)

---

## 📊 Example File Naming Conventions

### By Subject and Date
```
mathematics_16.02.2026.mp3
physics_17.02.2026.mp3
chemistry_18.02.2026.mp3
```

### By Subject and Topic
```
math_calculus_derivatives.mp3
math_linear_algebra_matrices.mp3
physics_mechanics_forces.mp3
```

### By Course and Week
```
CS101_week01_introduction.mp3
CS101_week02_variables.mp3
CS101_week03_functions.mp3
```

### With Time Slot
```
lecture_09_00_mathematics.mp3
lecture_11_00_physics.mp3
lecture_14_00_chemistry.mp3
```

---

## 🔄 Advanced Workflows

### Batch Processing Old Recordings

**Scenario:** You have 50 old recordings to transcribe

**Process:**
1. Copy all files to `recordings/` at once
2. Run script manually: `python auto_transcribe.py`
3. Wait for batch completion (check logs)
4. All transcripts appear in today's date folder

**Time estimate:**
- With RTX 3060: 50 hours audio → ~4-8 hours processing
- With CPU: 50 hours audio → ~1-2 days processing

**Tip:** Process overnight or over a weekend

### Multi-Language Processing

**Scenario:** Lectures in different languages

**Option 1 - Auto-detect:**
```python
# Edit auto_transcribe.py
# Remove this from cmd:
# "--language", LANGUAGE,
```

**Option 2 - Separate folders:**
```
recordings_polish/
recordings_english/
recordings_german/
```

Create separate scripts for each, or modify script to handle multiple folders.

### Weekly Archive Export

**Manual approach:**
```bash
# At end of week, create ZIP
zip -r lectures_week06.zip archive/10.02.2026/ archive/11.02.2026/ ... archive/14.02.2026/
```

**Automated approach:** Add to weekend cron job or Task Scheduler

---

## 🎯 Best Practices

### Recording Quality

**For best transcription results:**
- Use external microphone if possible
- Record in quiet environment
- Speak clearly, not too fast
- Position microphone 15-30cm from speaker
- Check levels before recording
- Use lossless or high-quality MP3 (192kbps+)

### File Organization

**Recommended naming:**
- Include date: `subject_DD.MM.YYYY.mp3`
- Use descriptive names: `physics_quantum_mechanics.mp3`
- Avoid special characters: Use `_` instead of spaces
- Keep consistent format across all files

### Archive Management

**Regular maintenance:**
- Review transcripts for accuracy
- Delete failed/corrupt transcriptions
- Back up archive folder monthly
- Consider compression for old archives

### Storage Estimates

**Typical sizes:**
- 1 hour MP3 (128kbps): ~56MB
- 1 hour transcript: ~50-100KB
- 1 semester (50 hours): ~3GB audio + 5MB text

**Plan accordingly:**
- Desktop: 100GB+ storage recommended
- External drive: For long-term archives

---

## 📈 Scaling Up

### Multiple Daily Runs

Instead of once at 20:00, run multiple times:

**Task Scheduler entries:**
- 08:00 - Morning lectures
- 14:00 - Afternoon lectures
- 20:00 - Evening recap

### Distributed Processing

For large batches:
1. Split recordings into multiple folders
2. Process on multiple machines simultaneously
3. Combine archives afterward

### Cloud Sync (Optional)

After processing:
```bash
# Sync archive to cloud (Dropbox, Google Drive, etc.)
rclone sync archive/ remote:LectureArchive/archive/
```

**Note:** Only sync after transcription (offline processing remains local)

---

## 🆘 Real-World Troubleshooting

### Scenario: Multiple speakers not detected

**Problem:** Transcript shows only SPEAKER_00

**Solutions:**
1. Check audio quality (may be too quiet for some speakers)
2. Adjust microphone position
3. Try different model: `--model large-v2`
4. Adjust speaker parameters in script

### Scenario: Polish characters garbled

**Problem:** Transcript has weird characters instead of ą, ę, ł, etc.

**Solutions:**
1. Ensure UTF-8 encoding (should be automatic)
2. View transcript with UTF-8 compatible editor
3. Check file was saved correctly

### Scenario: Transcription inaccurate

**Problem:** Wrong words, missing sentences

**Solutions:**
1. Use larger model: `medium` → `large-v2`
2. Improve audio quality
3. Re-record if possible with better setup
4. Manually correct transcript afterward

---

## ✅ Success Metrics

**How to know it's working well:**
- ✅ 95%+ transcription accuracy
- ✅ Speakers correctly differentiated
- ✅ Processing completes overnight
- ✅ No missed lectures
- ✅ Easy to find specific topics
- ✅ Time saved vs. manual note-taking

---

## 🎉 Real Success Story

**Before LectureArchive:**
- Manual note-taking during lectures
- Missing important points
- Reviewing recordings manually (time-consuming)
- Disorganized files

**After LectureArchive:**
- Focus on understanding, not writing
- Searchable archive of all lectures
- Quick reference for exam prep
- Professional organization
- Time saved: ~10 hours/week

---

**Start your journey to organized, searchable lecture archives today!**
