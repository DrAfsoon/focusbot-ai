
# 🧠 Dr. Afsoon’s FocusBot

Welcome to **Dr. Afsoon’s FocusBot** — an AI-powered tutoring assistant designed for Physician Assistant (PA) students studying **Pathophysiology**, with a special focus on *inflammation and repair* based on Robbins Chapter 2 and the latest clinical research.

## 🌐 Live App
Hosted on [Streamlit Cloud](https://share.streamlit.io/) — or deploy it locally.

## 🧰 Features
- 🔘 **Mode Toggle**:
  - 🧾 Robbins Standard Mode – textbook-style explanations
  - 🔬 Latest Research Mode – cites 2024–2025 clinical findings
  - 🎯 Quiz Mode – generates MCQs with answers
  - 🧪 Clinical Case Mode – case-based learning for real-world thinking

- 💬 **Chat Interface**: Ask questions in natural language.
- 🎓 **Student-Friendly Design**: Accessible interface and simple UX.

## 🚀 How to Run Locally

### 1. Clone this Repository
```bash
git clone https://github.com/your-username/focusbot-ai.git
cd focusbot-ai
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Add Your OpenAI API Key
Create a `.streamlit/secrets.toml` file:
```toml
openai_api_key = "sk-YourOpenAIKeyHere"
```

### 4. Run the App
```bash
streamlit run focusbot_app.py
```

---

## 📁 Project Structure
```
focusbot-ai/
├── focusbot_app.py
├── requirements.txt
└── .streamlit/
    └── secrets.toml
```

---

## ✍️ Customization

- Replace logo or title in `focusbot_app.py` as needed.
- Update prompt logic for each mode in the `prompt_map` dictionary.

---

## 🧑‍⚕️ Credits

Created by Dr. Afsoon — powered by GPT-4 via ScholarGPT  
Course: *Pathophysiology in Focus* | Website: [Dr-Afsoon.com](https://Dr-Afsoon.com)

---

## 📜 License

MIT License — free for educational and non-commercial use.
