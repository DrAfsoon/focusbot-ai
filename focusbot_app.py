
import streamlit as st
import openai

# Set your OpenAI API key here or use environment variables
openai.api_key = st.secrets["openai_api_key"]

st.set_page_config(page_title="Dr. Afsoon’s FocusBot", layout="wide")

# Title and Branding
st.title("🤖 Dr. Afsoon’s FocusBot")
st.markdown("Your AI Tutor for *Pathophysiology* — powered by Dr-Afsoon.com")

# Sidebar with Mode Selection
mode = st.sidebar.radio(
    "Choose Mode:",
    ("🧾 Explanation Mode", "Concept Connections Mode", "🔬 Latest Research Mode", "🎯 Quiz Mode", "🧪 Clinical Case Mode")
)

st.sidebar.markdown("🔄 Switch modes to change how the bot responds!")

# User Input
user_input = st.text_input("Ask FocusBot a question:")

def get_focusbot_response(user_input, mode):
    if not user_input:
        return ""

    prompt_map = {
        "🧾 Robbins Standard Mode": "You are a tutor for PA students using Robbins Chapter 2 on Inflammation and Repair. Explain clearly and ask follow-up questions.",
        "🔬 Latest Research Mode": "You are a clinical researcher and AI tutor. Use recent research studies (2024–2025) to explain modern advances in inflammation and tissue repair. Provide sources if possible.",
        "🎯 Quiz Mode": "You are a quiz master for PA students. Generate a multiple-choice question (MCQ) with 4 options based on inflammation, followed by the correct answer and explanation.",
        "🧪 Clinical Case Mode": "You are a case-based tutor. Present a clinical case involving inflammation (acute or chronic), then ask the student what they would do next or what the mechanism is."
    }

    system_prompt = prompt_map.get(mode, "")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0.6
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"⚠️ Error: {e}"

# Generate and display response
if user_input:
    with st.spinner("FocusBot is thinking..."):
        answer = get_focusbot_response(user_input, mode)
        st.markdown(f"**FocusBot ({mode}):**")
        st.write(answer)
