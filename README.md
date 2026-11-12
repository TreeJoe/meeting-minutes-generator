# Local Meeting Minutes Generator

A beginner-friendly local LLM application that turns meeting transcripts into structured minutes using Ollama and Streamlit.
## Repository Overview

The repository contains the following files:

| File | Description |
|:---|:---|
| `app.py` | Main application source code implementing the local LLM-based meeting minutes generator using Python and Ollama. |
| `sample_transcript.txt` | A sample meeting transcript used for the initial testing and demonstration of the application. |
| `test_transcripts.txt` | Contains five test meeting transcripts created using Generative AI to evaluate the model's performance across different meeting scenarios and populate the evaluation template. |
| `evaluation_matrix.csv` | A structured evaluation matrix for assessing the quality and performance of the locally running LLM. Includes the following columns:<br><br> - `transcript_id`: Unique transcript identifier.<br> - `model`: Ollama model name.<br>  - `decision_capture_correct`: Correctness of decision extraction.<br> - `owner_capture_correct`: Correctness of action-item owner extraction.<br> - `deadline_capture_correct`: Correctness of deadline extraction.<br> - `unsupported_claims`: Count of unsupported or hallucinated claims.<br> - `quality_rating_1_to_5`: Overall quality rating on a scale of 1–5.<br> - `notes`: Additional evaluation observations.<br><br>Correctness fields use `1` for correct and `0` for incorrect. The template contains five evaluation entries (`T01`–`T05`). 

## Features

- Uses a locally running Ollama model.
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

### 2. Downloading a model

Open PowerShell or the VS Code terminal:

```powershell
ollama pull llama3.2:1b
```

Another supported model:

```powershell
ollama pull qwen2.5:1.5b
```

### 3. Setting up Python

```powershell
python -m pip install -r requirements.txt
```

### 4. Launching the app

```powershell
streamlit run app.py
```

Streamlit will open the app in the browser (typically at http://localhost:8501).

## User Manual

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

