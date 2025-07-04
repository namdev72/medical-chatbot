import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models import Model

load_dotenv()

app = Flask(__name__)

class MedicalChatbot:
    def __init__(self):
        self.credentials = {
            "url": "https://us-south.ml.cloud.ibm.com",
            "apikey": os.getenv("IBM_CLOUD_API_KEY")
        }
        
        self.project_id = os.getenv("WATSONX_PROJECT_ID")
        
        try:
            self.client = APIClient(self.credentials)
            self.model = Model(
                model_id="ibm/granite-3-3-8b-instruct",
                params={
                    "decoding_method": "greedy",
                    "max_new_tokens": 400,
                    "temperature": 0.3,
                    "repetition_penalty": 1.1
                },
                credentials=self.credentials,
                project_id=self.project_id
            )
            print("✅ Successfully connected to IBM watsonx!")
        except Exception as e:
            print(f"❌ Connection failed: {e}")
            self.model = None
    
    def detect_emergency(self, user_input):
        emergency_keywords = [
            "chest pain", "can't breathe", "unconscious", "severe bleeding",
            "heart attack", "stroke", "suicide", "overdose", "severe pain",
            "can't move", "seizure", "choking"
        ]
        
        user_lower = user_input.lower()
        if any(keyword in user_lower for keyword in emergency_keywords):
            return """🚨 MEDICAL EMERGENCY DETECTED 🚨
            
This sounds like a medical emergency. Please:
• Call emergency services immediately (911/108/999)
• Go to the nearest emergency room
• Don't delay seeking immediate medical attention

This chatbot cannot help with emergencies."""
        
        return None
    
    def get_medical_response(self, user_query):
        if not self.model:
            return "Sorry, I'm currently unable to connect to the medical information service. Please try again later."
        
        # Check for emergency first
        emergency_response = self.detect_emergency(user_query)
        if emergency_response:
            return emergency_response
        
        # Create medical-focused prompt
        prompt = f"""You are a helpful medical information assistant. Provide accurate, helpful information while being responsible.

Guidelines:
- Provide general medical information and education
- Always recommend consulting healthcare professionals
- Never provide specific diagnoses
- Be empathetic and supportive
- Include relevant disclaimers

User question: {user_query}

Helpful response:"""
        
        try:
            response = self.model.generate_text(prompt)
            
            # Add disclaimer
            disclaimer = """

⚠️ MEDICAL DISCLAIMER: This information is for educational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment. Always consult your healthcare provider for medical concerns."""
            
            return response + disclaimer
            
        except Exception as e:
            return f"I apologize, but I'm having trouble processing your request right now. Please try again or consult a healthcare professional for medical concerns. Error: {str(e)}"

# Initialize chatbot
chatbot = MedicalChatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Please enter a message'})
        
        # Get response from chatbot
        response = chatbot.get_medical_response(user_message)
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
        
    except Exception as e:
        return jsonify({
            'error': 'An error occurred while processing your request.',
            'status': 'error'
        })

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'watsonx_connected': chatbot.model is not None
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)