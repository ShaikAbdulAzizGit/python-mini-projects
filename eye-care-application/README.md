# 👁️ Eye Care Application (Desktop Health Reminder)

A Python-based desktop application designed to protect eye health during long screen sessions.  
This project uses system notifications, voice alerts, and multithreading to remind users to rest their eyes and blink regularly.

---

## 📌 Project Overview

The **Eye Care Application** is a lightweight background program that runs continuously and reminds users to:
- Take eye breaks every 20 minutes
- Look away from the screen to relax eye muscles
- Blink frequently to reduce eye strain

It is especially useful for **developers, students, and office professionals** who spend long hours in front of screens.

---

## 🎯 Problem Statement

Prolonged screen usage can cause:
- Eye strain and dryness  
- Headaches  
- Reduced blinking rate  
- Long-term vision problems  

Most users forget to take breaks while working.  
This application solves that problem by acting as an **automated eye-care assistant**.

---

## ✨ Key Features

- 🔔 Desktop notifications for eye care reminders  
- 🗣️ Voice alerts using text-to-speech  
- ⏱️ 20-minute eye break reminder (20-20-20 rule inspired)  
- 👀 Frequent blink reminders  
- 🧵 Multithreading for parallel reminders  
- ⚡ Lightweight and runs in the background  

---

## 🧠 How It Works (High-Level)

- One background thread reminds the user every 20 minutes to rest their eyes  
- Another background thread reminds the user every 60 seconds to blink  
- Voice alerts reinforce important reminders  
- The application runs continuously until manually stopped  

---

## 🧰 Tech Stack

- **Language:** Python  
- **Libraries Used:**  
  - `plyer` (Desktop notifications)  
  - `pyttsx3` (Text-to-speech)  
  - `threading` (Concurrent execution)  
  - `time`  

---

## 📁 Project Structure

```
eye-care-application/
│
├── main.py          # Core application logic
└── README.md        # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ShaikAbdulAzizGit/python-mini-projects.git
cd python-mini-projects/eye-care-application
```

### 2️⃣ Install Dependencies
```bash
pip install plyer pyttsx3
```

---

## ▶️ How to Run

```bash
python main.py
```

The application will start running in the background and send reminders automatically.

---

## 🌍 Real-World Use Cases

- Developers working long coding sessions  
- Students attending online classes  
- Office professionals using screens all day  
- Freelancers and remote workers  
- Anyone concerned about digital eye strain  

---

## 📚 Learning Outcomes

- Understanding multithreading in Python  
- Using desktop notification systems  
- Implementing text-to-speech functionality  
- Designing long-running background applications  
- Writing practical health-focused utilities  

---

## 🚀 Future Improvements

- Configurable reminder intervals  
- GUI interface (Tkinter / PyQt)  
- System tray support  
- Pause / resume functionality  
- Cross-platform optimization  

---

## 👨‍💻 Author

**Shaik Abdul Aziz**  
Python Developer | Automation & Utility App Enthusiast  

🔗 GitHub: https://github.com/ShaikAbdulAzizGit  

---

⭐ If you care about productivity and health, feel free to explore the code and try the application!
