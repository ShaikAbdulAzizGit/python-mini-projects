# 📰 News Application (Real-Time CLI News Fetcher)

A Python-based command-line application that fetches and displays real-time news articles based on user-selected topics.  
This project demonstrates API integration, JSON parsing, and dynamic content retrieval from an external service.

---

## 📌 Project Overview

The **News Application** allows users to:
- Enter a topic of interest  
- Fetch the latest related news articles  
- View titles, descriptions, and source links directly in the terminal  

It uses the **NewsAPI** service to retrieve up-to-date information, making it a practical example of real-world API usage.

---

## 🎯 Problem Statement

Staying updated with current news usually requires browsing multiple websites or apps.  
From a developer’s perspective, consuming third-party APIs and handling real-time data is a critical skill.

This project solves both by:
- Providing instant news access via CLI  
- Demonstrating how to integrate external APIs in Python  

---

## ✨ Key Features

- 🔍 Topic-based news search  
- 🌐 Real-time data from NewsAPI  
- 📄 Clean display of article title, description, and URL  
- 🔐 Secure API key handling  
- 🧼 Simple and readable code structure  

---

## 🧠 How It Works (High-Level)

1. User enters a topic of interest  
2. Application sends a request to NewsAPI  
3. API returns a JSON response with articles  
4. Relevant information is extracted  
5. News articles are displayed in an organized format  

---

## 🧰 Tech Stack

- **Language:** Python  
- **API:** NewsAPI  
- **Libraries:**  
  - `requests`  

---

## 📁 Project Structure

```
news-application/
│
├── main.py          # News fetching and display logic
├── secret_key.py    # Stores API key securely
└── README.md        # Project documentation
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ShaikAbdulAzizGit/python-mini-projects.git
cd python-mini-projects/news-application
```

### 2️⃣ Install Dependencies
```bash
pip install requests
```

### 3️⃣ Add API Key

Create a file named `secret_key.py`:
```python
api_key = "YOUR_NEWSAPI_KEY"
```

---

## ▶️ How to Run

```bash
python main.py
```

Enter a topic when prompted to view the latest news.

---

## 🌍 Real-World Applications

- News aggregation platforms  
- Research and trend analysis tools  
- Content monitoring systems  
- Data collection pipelines  
- API-driven backend services  

---

## 📚 Learning Outcomes

- Working with REST APIs  
- Handling JSON responses  
- Query parameter construction  
- Secure API key usage  
- Building data-driven CLI applications  

---

## 🚀 Future Improvements

- Date range selection  
- Category-based filtering  
- Save articles to file or database  
- Web or GUI interface  
- Error handling for API limits  

---

## 👨‍💻 Author

**Shaik Abdul Aziz**  
Python Developer | API Integration Enthusiast  

🔗 GitHub: https://github.com/ShaikAbdulAzizGit  

---

⭐ If you enjoy working with real-world data, explore the code and try extending the application!
