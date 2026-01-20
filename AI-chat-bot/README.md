# 🤖 AI Chat Bot (OpenRouter Powered)

An intelligent command-line AI chatbot built using Python and OpenRouter's free LLM APIs.  
This project demonstrates real-world API integration, clean Python architecture, and practical AI usage.

---

## 📌 Project Overview

The **AI Chat Bot** is a terminal-based conversational assistant that communicates with a large language model using the OpenRouter API.  
It accepts user input, sends it to an AI model, and returns intelligent responses in real time.

The chatbot is designed to simulate a personalized conversational agent and can communicate in **English and Hindi**, showcasing multilingual support and prompt engineering.

---

## 🎯 Problem Statement

Building AI-powered applications often feels complex due to:
- API authentication handling  
- Request/response parsing  
- Error handling  
- Maintaining clean and readable code  

This project solves that by providing a **simple yet production-style implementation** of an AI chatbot using Python.

---

## ✨ Key Features

- 🔗 Integration with OpenRouter AI API  
- 🧠 Uses Meta LLaMA 3.3 (70B) instruct model  
- 💬 Real-time conversational interaction  
- 🌐 Multilingual capability (English & Hindi)  
- 🛡️ Secure API key handling  
- ❌ Graceful error handling  
- 🧼 Clean, modular Python code  

---

## 🧠 How It Works (High-Level)

1. User enters a message in the terminal  
2. The message is sent to OpenRouter's Chat Completion API  
3. The AI model processes the input  
4. A meaningful response is returned and displayed  
5. The conversation continues until the user exits  

---

## 🧰 Tech Stack

- **Language:** Python  
- **API:** OpenRouter AI  
- **Model:** Meta LLaMA 3.3 (70B Instruct)  
- **Libraries:** `requests`  

---

## 📁 Project Structure

```
AI-chat-bot/
│
├── main.py          # Core chatbot logic
├── secret_key.py    # Stores API key securely
└── README.md        # Project documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ShaikAbdulAzizGit/python-mini-projects.git
cd python-mini-projects/AI-chat-bot
```

### 2️⃣ Install Dependencies
```bash
pip install requests
```

### 3️⃣ Add API Key

Create a file named `secret_key.py`:
```python
api_key = "YOUR_OPENROUTER_API_KEY"
```

---

## ▶️ How to Run

```bash
python main.py
```

Type your message and start chatting.  
Use `exit` or `quit` to stop the program.

---

## 🌍 Real-World Applications

- AI-powered customer support bots  
- Personal AI assistants  
- CLI-based automation helpers  
- Prototyping AI products  
- Learning API-based AI integration  

---

## 📚 What I Learned

- Working with third-party AI APIs  
- Structuring production-style Python scripts  
- Handling JSON responses and exceptions  
- Prompt engineering fundamentals  
- Secure credential management  

---

## 🚀 Future Improvements

- Conversation history memory  
- Web-based UI (Flask / FastAPI)  
- Streaming responses  
- Logging and analytics  
- Model selection options  

---

## 👨‍💻 Author

**Shaik Abdul Aziz**  
Aspiring Software Engineer | Python & AI Enthusiast  

🔗 GitHub: https://github.com/ShaikAbdulAzizGit  

---

⭐ If you found this project interesting, feel free to explore the code and give it a star!
