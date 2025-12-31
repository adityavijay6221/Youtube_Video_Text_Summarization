# 📺 YouTube Text Summarization using LangChain & Groq LLM

A Streamlit-based application that generates concise summaries of YouTube videos by extracting transcripts and processing them through a LangChain summarization pipeline powered by Groq-hosted LLaMA models.

---

## 🔍 Project Overview

This project demonstrates an end-to-end **YouTube transcript summarization workflow**, combining:

- Transcript extraction from YouTube URLs  
- Prompt-driven summarization using LangChain  
- High-speed inference using Groq’s LLaMA-3.1-8B-Instant model  
- A lightweight and interactive Streamlit user interface  

The experimentation and validation of the summarization approach were carried out in `yt_experiments.ipynb` before being integrated into the Streamlit app (`app.py`).

---

## 🧠 How It Works

1. **User Input**
   - YouTube video URL
   - Groq API key (entered securely via the sidebar)

2. **Transcript Loading**
   - Transcripts are fetched using `YoutubeLoader`
   - Video metadata is excluded to keep the context text-only

3. **Prompt Engineering**
   - A simple, focused summarization prompt:
     ```
     Summarize the following text in a concise manner:
     {text}
     ```

4. **Summarization Chain**
   - LangChain’s `load_summarize_chain`
   - `stuff` chain type (entire transcript passed at once)
   - Backed by Groq LLM

5. **Output**
   - Final summary rendered directly in the Streamlit UI

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI layer  
- **LangChain (classic & community)** – prompts, chains, loaders  
- **Groq LLM** – fast LLaMA inference  
- **YouTube Transcript API / Pytube** – transcript access  

---

## 📂 Project Structure

```bash
.
├── app.py                 # Streamlit application
├── yt_experiments.ipynb   # Summarization experiments
├── requirements.txt       # Dependencies
└── README.md
