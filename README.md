🧠 AI-Powered Medical Responses: Uses IBM Watson AI for intelligent medical query processing 🆘 Emergency Detection: Automatically detects medical emergencies and provides immediate guidance 💬 Interactive Chat Interface: ...


# 🩺 Medical Chatbot with Emergency Detection

An intelligent medical chatbot application built with Flask and IBM Watson AI that provides medical information and includes emergency detection capabilities for critical medical situations.

---

## 🎯 Key Features

- 🧠 **AI-Powered Medical Responses**: Uses IBM Watson AI for intelligent medical query processing  
- 🆘 **Emergency Detection**: Automatically detects medical emergencies and provides immediate guidance  
- 💬 **Interactive Chat Interface**: Real-time conversational medical assistance  
- 🔍 **Smart Keyword Recognition**: Identifies emergency keywords like _"can't move"_, _"seizure"_, _"choking"_  
- 🌐 **Web-Based Application**: Responsive Flask web interface  
- ⚡ **Instant Emergency Response**: Triggers emergency protocols when critical terms are detected

---

## 📁 Project Structure
--- bash

medical-chatbot/
├── app.py
├── templates/
│ └── index.html
├── .env # Not shared in repo
├── requirements.txt
└── README.md



---

## 🔍 How It Works

### Emergency Detection System

The chatbot includes a sophisticated emergency detection system that:

1. **Monitors User Input**: Scans all user messages for emergency keywords  
2. **Instant Alerts**: Detects critical terms like _"can't move"_, _"seizure"_, _"choking"_  
3. **Immediate Response**: Provides emergency guidance and prioritizes responses over general medical queries  

---

## 🚀 Installation & Setup

--- bash
git clone https://github.com/yourusername/medical-chatbot.git
cd medical-chatbot
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt


Create a .env file:
API_KEY=your_watsonx_api_key
MODEL_ID=your_model_id


Run the app:

---bash
Copy
Edit
python app.py
Open http://localhost:5000 in your browser.


⚠️ Disclaimer
This chatbot is not a substitute for medical professionals. Always consult a doctor for serious concerns.

📄 License
MIT License



🏥 Medical Chatbot with Emergency Detection
An intelligent medical chatbot application built with Flask and IBM Watson AI that provides medical information and includes emergency detection capabilities for critical medical situations.





🚨 Key Features

🤖 AI-Powered Medical Responses: Uses IBM Watson AI for intelligent medical query processing
🆘 Emergency Detection: Automatically detects medical emergencies and provides immediate guidance
💬 Interactive Chat Interface: Real-time conversational medical assistance
🔍 Smart Keyword Recognition: Identifies emergency keywords like "can't move", "seizure", "choking"
🌐 Web-Based Application: Responsive Flask web interface
⚡ Instant Emergency Response: Immediate emergency protocols when critical situations are detected






📋 Project Structure
medical-chatbot/
│
├── app.py 
├── templates/
│ └── index.html 
├── .env (not shared in repo)
├── requirements.txt
└── README.md






🎯 How It Works
Emergency Detection System
The chatbot includes a sophisticated emergency detection system that:



1. Monitors User Input: Scans all user messages for emergency keywords
2. Instant Alert: Detects critical terms like:
   "can't move"  
   "seizure"
   "choking"
Other emergency indicators
3. Immediate Response: Provides emergency guidance and contact information
Safety First: Prioritizes emergency responses over regular medical queries




🚀 Installation & Setup

Prerequisites
Python 3.11+
IBM Watson AI account
Flask web framework knowledge


Quick Start
1.Clone the repository
bashgit clone https://github.com/namdev72/medical-chatbot.git
cd medical-chatbot

2.Install dependencies
bashpip install -r requirements.txt

3.Configure environment variables
Create .env file:
envWATSON_API_KEY=your_watson_api_key
WATSON_URL=your_watson_service_url
WATSON_PROJECT_ID=your_watson_project_id

4.Run the application
bashpython app.py

5.Access the chat interface

Open browser: http://localhost:5000
Start chatting with the medical bot




Important Note
⚠️ Disclaimer: This chatbot is for informational purposes only and should not replace professional medical advice. Always consult with qualified healthcare professionals for medical concerns.


License
MIT License


Contact
For questions or support, please create an issue in the GitHub repository.
____________________________________________________________________________________________________________________________________________________________________________________________________________________
Project created by: https://github.com/namdev72
