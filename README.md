# 🤖 AI Chatbot with Personality Modes

An interactive AI chatbot that adapts its behavior based on selected personality modes such as **Angry**, **Funny**, and **Sad**. Built using **LangChain**, **Mistral AI**, and **Streamlit**, this project demonstrates conversational AI with dynamic system prompts and persistent chat state.

---

## 🚀 Features

* 🔁 Multiple personality modes (Angry, Funny, Sad, Default)
* 💬 Real-time conversational interface
* 🧠 Context-aware responses using message history
* 🔄 Reset chat functionality
* 🌐 Deployable via Streamlit Cloud

---

## 🛠️ Tech Stack

* **LangChain** – LLM orchestration
* **Mistral AI** – Language model
* **Streamlit** – UI framework
* **Python** – Core logic

---

## 📂 Project Structure

```
genai/
│
├── chatmodels/
│   ├── app.py        # Streamlit UI
│   ├── chat.py       # CLI chatbot
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-chatbot-modes.git
cd ai-chatbot-modes
```

### 2. Create virtual environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API Key

Create a `.env` file (for local use):

```
MISTRAL_API_KEY=your_api_key_here
```

---

## ▶️ Run Locally

```bash
python3 -m streamlit run chatmodels/app.py
```

---

## 🌍 Deployment

Deployed using **Streamlit Cloud**.

> Add your API key in **Secrets**:

```
MISTRAL_API_KEY="your_api_key"
```

---

## 🧠 How It Works

* Uses **SystemMessage** to control chatbot personality
* Maintains conversation history using session state
* Dynamically updates behavior based on selected mode
* Sends full message history to LLM for contextual responses

---

## 📌 Future Improvements

* Streaming responses
* Chat history export
* Multi-user sessions
* LLM provider switching (OpenAI/Mistral)

---

## 📄 License

This project is for learning and demonstration purposes.
