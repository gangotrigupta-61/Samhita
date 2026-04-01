# 🚀 Samhita Standard Start Guide

Welcome to Samhita! This guide will get you from zero to a fully running Clinical Intelligence platform in under 5 minutes.

---

## 📋 Prerequisites
Ensure you have the following installed:
- **Node.js** (v18 or higher)
- **Python** (3.9 or higher)
- **Git**

---

## 🛠️ Step 1: Environment Setup
You need API keys for the AI features to work. Open `samhita-backend/.env` and ensure these are filled:
- `GEMINI_API_KEY`: For Vision & Extraction.
- `GROQ_API_KEY`: For Clinical Chatbot.
- `SARVAM_API_KEY`: For Voice STT/TTS.
- `LIVEKIT_URL/KEY/SECRET`: For Live Voice Agent.

---

## 🖥️ Step 2: Launch the Backend
Open a terminal and run:
```bash
cd samhita-backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```
*Backend will be live at `http://localhost:8000`*

---

## 🎨 Step 3: Launch the Frontend
Open a **new** terminal and run:
```bash
cd samhita-ui
npm install
npm run dev
```
*Frontend will be live at `http://localhost:3000`*

---

## 🧬 Step 4: Seed Demo Data (Important for Hackathon)
To show the judges a "full" dashboard immediately, run this script to pre-populate patients and alerts:
```bash
# In the samhita-backend directory
python seed_demo.py
```

---

## 🏁 Step 5: Start the Demo!
1. Go to **[http://localhost:3000](http://localhost:3000)**.
2. Observe the **Premium Landing Page**.
3. Click **"Launch Intelligence"** to enter the **Doctor Dashboard**.
4. Use the **[Demo Guide](file:///c:/Users/aryan/Desktop/SAMHITA/demo_guide.md)** for a winning presentation script.

---

## 🛠️ Troubleshooting
- **Network Error?** Ensure the backend (port 8000) is running before opening the frontend.
- **Image Not Showing?** Refresh the page or check if `public/hero.png` exists.
- **AI Not Responding?** Check your `.env` keys in the backend terminal logs.
