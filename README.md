# Local Meeting Minutes Generator

A beginner-friendly local LLM application that turns meeting transcripts into structured minutes using Ollama and Streamlit.

## Features

- Uses a locally running Ollama model (no cloud API key).
- Generates a meeting overview, summary, discussion points, decisions, action items, and next-meeting details.
- Allows the user to select among small local models.
- Provides a downloadable Markdown output.
- Prompt instructs the model not to invent missing details.

## Requirements

- Windows 10/11 (or macOS/Linux)
- Python 3.10+
- Ollama installed

## Setup on Windows

### 1. Install Ollama

Download and install from https://ollama.com/download

### 2. Download a model

Open PowerShell or the VS Code terminal:

```powershell
ollama pull llama3.2:1b
```

You can optionally try another supported model:

```powershell
ollama pull qwen2.5:1.5b
```

### 3. Set up Python
python -m pip install -r requirements.txt
```

### 4. Launch the app

```powershell
streamlit run app.py
```

Streamlit will open the app in your browser (typically at http://localhost:8501).

## How to use

1. Choose the model in the sidebar. It must be installed in Ollama.
2. Paste a transcript into the text area.
3. Click **Generate minutes**.
4. Review the result and download it as Markdown.

## Project architecture

```text
Transcript
   |
   v
Streamlit UI
   |
   v
Python prompt + Ollama Python client
   |
   v
Local Ollama model
   |
   v
Structured Markdown minutes
```

## Limitations

- The model may still make mistakes and hallucinate.
- Transcript speaker labels improve assignment of action-item owners.
- This version accepts text transcripts only; it does not transcribe audio.
- It does not fine-tune a model or use a vector database.

