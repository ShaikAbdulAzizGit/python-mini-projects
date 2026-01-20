# 🔳 QR Code Generator (Customizable CLI Tool)

A Python-based QR Code Generator that allows users to create **fully customizable QR codes** directly from the command line.  
This project demonstrates real-world utility development, third‑party library usage, file handling, and user-driven customization.

---

## 📌 Project Overview

The **QR Code Generator** enables users to:
- Generate QR codes for URLs or text  
- Customize size, border, colors, and background  
- Preview the QR code instantly  
- Save generated QR codes locally  

It is designed as a **practical automation tool** that can be used in daily workflows, marketing, sharing links, and more.

---

## 🎯 Problem Statement

Creating QR codes often requires:
- Online tools (privacy concerns)  
- Limited customization  
- Manual downloading  

From a developer perspective, learning how to:
- Work with external libraries  
- Handle images and files  
- Build reusable utilities  

is essential.  
This project solves both problems with a **local, customizable QR code generator**.

---

## ✨ Key Features

- 🔗 Generate QR codes for text or URLs  
- 🎨 Custom fill and background colors  
- 📏 Adjustable box size and border  
- 🖼️ Instant QR code preview  
- 💾 Optional saving to local directory  
- 🧼 Clean, reusable function design  
- ❌ Graceful error handling  

---

## 🧠 How It Works (High-Level)

1. User provides text or URL  
2. User customizes QR code appearance  
3. QR code is generated using high error correction  
4. Image is previewed on screen  
5. User chooses whether to save the QR code  

---

## 🧰 Tech Stack

- **Language:** Python  
- **Libraries Used:**  
  - `qrcode`  
  - `Pillow (PIL)`  
  - `os`  

---

## 📁 Project Structure

```
qr-code-generator/
│
├── main.py                # QR code generation logic
├── Generated_qrcodes/     # Saved QR codes (auto-created)
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ShaikAbdulAzizGit/python-mini-projects.git
cd python-mini-projects/qr-code-generator
```

### 2️⃣ Install Dependencies
```bash
pip install qrcode pillow
```

---

## ▶️ How to Run

```bash
python main.py
```

Follow the prompts to customize and generate your QR code.

---

## 🌍 Real-World Applications

- Sharing URLs quickly  
- Marketing materials  
- Event invitations  
- Digital business cards  
- Offline data sharing  
- Automation tools  

---

## 📚 Learning Outcomes

- Working with image generation libraries  
- File system operations in Python  
- Building customizable CLI tools  
- Writing reusable functions  
- Handling user input and defaults  

---

## 🚀 Future Improvements

- GUI or web-based interface  
- Batch QR code generation  
- Logo embedding inside QR codes  
- Export formats (SVG, PDF)  
- Configuration file support  

---

## 👨‍💻 Author

**Shaik Abdul Aziz**  
Python Developer | Automation & Utility Tool Builder  

🔗 GitHub: https://github.com/ShaikAbdulAzizGit  

---

⭐ If you found this project useful, explore the code and try extending it further!
