<h1 align="center">🚀 AI Resume Analyzer</h1>
<p align="center">
  Smart Resume Analysis & ATS Matching System
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue" />
  <img src="https://img.shields.io/badge/Flask-Web%20App-green" />
  <img src="https://img.shields.io/badge/Deployment-Render-purple" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen" />
</p>

---

## 📌 Overview

An AI-powered web application that analyzes resumes, extracts key skills, matches them with job descriptions, and provides intelligent suggestions to improve ATS score.

---

## ✨ Features

* 📄 Upload Resume (PDF/DOCX)
* 🧠 Automatic Skill Extraction
* 🎯 Resume vs Job Description Matching
* 📊 ATS Score Calculation
* ✨ Missing Skills Suggestions
* 🔐 User Authentication (Login / Signup)
* 📧 Forgot Password via Email
* 📥 Resume Builder & Download Feature

---

## ⚙️ How It Works

1. Upload your resume (PDF/DOCX)
2. Enter the job description
3. System extracts skills from resume
4. Matches with job requirements
5. Calculates match score
6. Displays missing skills & suggestions

---

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite

**Libraries Used:**

* PyMuPDF --> pip install pyMuPDF
* Flask-Mail --> pip install Flask-Mail
* Authlib --> pip install authlib
* Flask --> pip install flask
* python-docx --> pip install python-docx
* reportlab --> pip install reportlab

---

## 📂 Project Structure

```
ai-resume-analyzer-/
│
├── app.py
├── utils.py
├── requirements.txt
├── runtime.txt
├── .python-version
├── templates/
├── static/
└── users.db
```

---

## ⚙️ Installation (Local Setup)

### 1. Clone the repository

```
git clone https://github.com/Harshu3115/ai-resume-analyzer-.git
cd ai-resume-analyzer-
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the application

```
python app.py
```

---

## 🌐 Deployment

Deployed on **Render**

### Required Environment Variables:

```
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
SECRET_KEY=your_secret_key
GOOGLE_CLIENT_ID=your_client_id
GOOGLE_CLIENT_SECRET=your_client_secret
```

---

## 📸 Screenshots

<p align="center">
  <img src="https://github.com/user-attachments/assets/fe5d27dd-b729-4b8f-b2ff-73777cace1ee" width="45%" />
  <img src="https://github.com/user-attachments/assets/275d3372-a03f-4491-9f8d-0099a10adc29" width="45%" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/3a29d51b-4329-4edc-a8d6-70ff1cf2cada" width="45%" />
  <img src="https://github.com/user-attachments/assets/dd23fcc7-34e3-45d3-932d-9f95f3afa8d2" width="45%" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/2facecf0-2710-4d9e-85a1-001c17c35a51" width="45%" />
  <img src="https://github.com/user-attachments/assets/f7cd5e39-d841-4f74-8d3a-9021753a6858" width="45%" />
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/40b5c0d3-7b94-446a-8cb2-67915d5c7a92" width="45%" />
  <img src="https://github.com/user-attachments/assets/61c94b14-3585-4831-858c-843a3208269b" width="45%" />
</p>

---

## 🔗 Live Demo

👉 https://ai-resume-analyzer-xsvg.onrender.com

---

## 🎯 Future Improvements

* 🤖 Advanced AI-based skill extraction
* 📊 Improved ATS scoring system
* 📱 Fully responsive UI
* 🧾 Multiple resume templates

---

## 👨‍💻 Author

**Harshad Shinde**
FTC Sangola

* GitHub: https://github.com/Harshu3115
* LinkedIn: *https://www.linkedin.com/in/harshad-shinde3115b2ab/*

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
