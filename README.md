# VoxSentiment — Applied Speech Analytics for Contact-Centre Intelligence

VoxSentiment is an end-to-end speech analytics system that transforms raw call-centre audio into speaker-attributed transcripts, concise summaries, and sentiment signals. It is designed to support quality assurance, escalation triage, and insight-led agent coaching by reducing manual call review effort and surfacing high-risk interactions quickly.

---

## Why This Exists

Contact-centre teams handle high volumes of calls, but manual listening does not scale. Important signals (customer dissatisfaction, repeated complaints, escalation risk) are often missed or detected too late. VoxSentiment automates first-pass review by extracting structured intelligence from audio and producing outputs that are ready for downstream analytics.

---

## What It Produces

For each call, VoxSentiment generates:

- **Speaker-attributed transcript** (who said what)
- **Concise call summary** (key points, outcomes, next actions)
- **Sentiment signals** (customer / agent tone indicators)
- **Searchable structured outputs** (CSV / JSON and optional database storage)

---

## System Overview

**Pipeline (high level):**
1. Audio ingestion and preprocessing  
2. Automatic Speech Recognition (ASR)  
3. Speaker diarisation  
4. Text summarisation  
5. Sentiment analysis  
6. Persist outputs for analytics (CSV/JSON + optional database)

---

## Tech Stack

- **Language:** Python  
- **ASR:** Faster-Whisper (Whisper-based ASR)  
- **Diarisation:** Speaker diarisation component (pyannote-based pipeline)  
- **Summarisation:** Transformer summariser (BART/CNN-style)  
- **Sentiment:** RoBERTa-based sentiment model  
- **Storage (optional):** MongoDB for transcripts/metadata  
- **UI (optional):** Streamlit application for review and exploration  

---

## How to Run

### Clone and install dependencies
```bash
git clone https://github.com/rashidkhan-python/voxsentiment-speech-analytics.git
cd voxsentiment-speech-analytics
pip install -r requirements.txt


python main.py --input "data/sample_call.wav" --output "outputs/"

streamlit run app.py
Data

Supports anonymised call-centre style audio and publicly available conversational audio datasets.

If university-provided audio is used, it must remain anonymised and stored securely.

Evaluation Approach

VoxSentiment is evaluated using a combination of quantitative and qualitative checks:

ASR quality: word/phrase error patterns on representative calls

Diarisation quality: speaker turn consistency and segmentation accuracy

Summarisation quality: factual alignment and coverage of key issues

Sentiment quality: stability across noise levels, speaker overlap, and long calls

Operational value: reduction in manual review time and improved triage speed

Results (example outcomes)

Reduced manual call review effort by surfacing transcripts, summaries, and sentiment signals for rapid scanning

Enabled QA/management workflows to prioritise calls likely to require escalation or coaching

Produced structured outputs suitable for dashboards and trend analysis

Replace this section with your actual metrics/screenshots when available (even 2–3 examples helps a lot).

.
├─ README.md
├─ requirements.txt
├─ data/                 # optional sample audio (or document source)
├─ src/                  # pipeline modules
├─ outputs/              # transcripts, summaries, sentiment
├─ app.py                # Streamlit UI (optional)
└─ main.py               # entry point


Limitations & Next Steps

Improve robustness on noisy calls and strong accents

Add confidence scoring and uncertainty-aware flags

Extend to intent detection and escalation classification

Support multi-lingual processing and domain adaptation

Add monitoring and evaluation reports for production deployment

License : MIT License
