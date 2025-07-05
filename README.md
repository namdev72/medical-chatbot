# 🩺 Medical Chatbot with Emergency Detection

An intelligent AI-powered medical chatbot built with **Flask** and **IBM Watsonx AI** that provides helpful medical information and includes an emergency detection system for critical health situations.

---

## ✨ Features

- 🧠 **AI-Powered Responses**: Processes user queries using IBM Watsonx for medical advice
- 🆘 **Emergency Detection**: Scans messages for urgent medical terms like _"can't breathe"_, _"seizure"_, or _"choking"_
- 💬 **Real-time Chat Interface**: Provides interactive, human-like responses
- 🔍 **Keyword Monitoring**: Recognizes high-risk symptoms for instant alerts
- 🌐 **Web-Based UI**: Built using Flask and HTML for easy browser interaction
- ⚡ **Emergency Protocol Trigger**: Responds quickly when critical conditions are detected

---

## 📁 Project Structure


```bash
medical-chatbot/
├── app.py # Flask backend
├── templates/
│ └── index.html # Frontend UI
├── .env # API key storage (excluded from repo)
├── requirements.txt # Python dependencies
└── README.md # Documentation file
```

---

## 🎯 How It Works

### 🚨 Emergency Detection System

The chatbot includes a built-in system that:

1. **Monitors user input** for specific emergency keywords
2. **Triggers alerts** if dangerous symptoms are detected
3. **Provides safety guidance** and shifts priority to emergency over general queries

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/medical-chatbot.git
cd medical-chatbot
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3.Install Dependencies
```bash
Copy
Edit
```

### 4. Add Environment Variables(.env)
```bash
API_KEY=your_ibm_watsonx_api_key
MODEL_ID=your_model_id
```

### 5.Run the App
```bash
python app.py
```

Visit: http://localhost:5000

---

## 🧪 Sample Inputs to Try


1. **"I have a fever and headache, what should I do?"

2. **"My friend is having a seizure!"

3. **"Can I take paracetamol with ibuprofen?"


## 📄 License

This project is licensed under the MIT License.

Use at your own risk. This chatbot does not replace professional medical advice.

## 👨‍💻 Author

Developed by [namdev72](https://github.com/namdev72)


