import streamlit as st
import ollama
from datetime import datetime

st.set_page_config(page_title="Meeting Minutes Generator", page_icon=None, layout="wide")

st.title("Meeting Minutes Generator")
st.caption("Generate structured meeting notes locally with Ollama. Your transcript is processed by the model running on your machine.")

with st.sidebar:
    st.header("Settings")
    model = st.selectbox("Ollama model", ["llama3.2:1b", "llama3.2:3b", "qwen2.5:1.5b", "qwen2.5:3b"], index=0)
    st.caption("The selected model must already be downloaded in Ollama.")
    temperature = st.slider("Creativity", 0.0, 1.0, 0.2, 0.1)
    st.markdown("---")
    st.write("Local runtime: Ollama")

sample_transcript = """Meeting: Speech Recognition Project Progress
Date: 8 November 2026

Aditi: We need to review the speech recognition project progress.
Rahul: I will complete the MFCC feature extraction module by Friday.
Priya: I will evaluate the CNN model and share the test results by Tuesday.
Aditi: We agreed to use the TIMIT dataset for the next round of experiments.
Rahul: The team should also compare inference speed between the two models.
Aditi: Our next meeting will be on Monday at 11 AM."""

if "transcript" not in st.session_state:
    st.session_state.transcript = sample_transcript

st.subheader("Meeting transcript")
transcript = st.text_area(
    "Paste the transcript below, or load the sample transcript.",
    key="transcript",
    height=260,
    placeholder="Paste meeting conversation here..."
)

col1, col2 = st.columns([1, 4])
with col1:
    generate = st.button("Generate minutes", type="primary", use_container_width=True)
with col2:
    st.caption("The model may take a little time depending on your computer and selected model.")

SYSTEM_PROMPT = """You are an expert Meeting Minutes (MoM) generation assistant.

Your task is to convert raw meeting transcripts into accurate, structured, concise, and professional meeting minutes.

STRICT RULES:

1. Use ONLY information explicitly stated in the transcript.
2. Do not invent facts, decisions, deadlines, meeting dates, attendees, or action items.
3. Distinguish between:
   - Decisions: Explicitly agreed upon by participants.
   - Suggestions: Ideas proposed but not approved.
   - Action Items: Tasks explicitly assigned to a person.
   - Unresolved Issues: Topics that require further discussion or confirmation.
4. Preserve the correct speaker attribution for every task and decision.
5. If a deadline is not explicitly stated, write "Not specified".
6. If an owner is not explicitly assigned, write "Unassigned".
7. If a decision is conditional, preserve the condition.
8. When participants correct earlier statements, use the final confirmed information.
9. Do not interpret a campaign launch date as a next meeting date.
10. Do not convert a performance target into a sales target.
11. Ignore background noise unless it affects the meaning of the discussion.
12. Do not assume that a suggestion was approved simply because nobody objected.
13. If information is ambiguous, explicitly mark it as "Unclear" instead of guessing.
14. Avoid duplicate action items.

Before generating the final output, internally verify:
- Every decision is supported by the transcript.
- Every action item has the correct owner.
- Every deadline is accurate.
- No unsupported facts have been introduced."""

if generate:
    if not transcript.strip():
        st.warning("Please enter a meeting transcript first.")
    else:
        with st.spinner(f"Generating minutes with {model} via Ollama..."):
            try:
                response = ollama.chat(
                    model=model,
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": "Create meeting minutes from this transcript:\n\n" + transcript}
                    ],
                    options={"temperature": temperature}
                )
                minutes = response["message"]["content"]
                st.session_state["generated_minutes"] = minutes
                st.session_state["generated_model"] = model
            except ollama.ResponseError as e:
                st.error(f"Ollama returned an error: {e}. Check that the model is downloaded using `ollama pull {model}`.")
            except Exception as e:
                st.error(f"Could not connect to Ollama. Make sure Ollama is running and the model is installed. Details: {e}")

if "generated_minutes" in st.session_state:
    st.markdown("---")
    st.subheader("Generated meeting minutes")
    st.markdown(st.session_state["generated_minutes"])
    st.caption(f"Generated using {st.session_state.get('generated_model', model)}")
    safe_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    st.download_button(
        "Download minutes as Markdown",
        data=st.session_state["generated_minutes"],
        file_name=f"meeting_minutes_{safe_timestamp}.md",
        mime="text/markdown"
    )
