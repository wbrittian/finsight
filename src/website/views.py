from flask import Blueprint, render_template, request, jsonify

import google.generativeai as genai

genai.configure(api_key="AIzaSyDtl9LY8u1PsjSWNC6DgO50Dp2DJCNKFoc")
model = genai.GenerativeModel('gemini-1.5-pro')
chat_session = model.start_chat()

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/chat')
def chat():
    return render_template("chat.html")  # This is the HTML page where you'll send/receive messages

@views.route("/chat", methods=["POST"])
def chat_route():
    user_message = request.json.get("message")
    
    if not user_message:
        return jsonify({"response": "No message received."}), 400

    try:
        response = chat_session.send_message(user_message)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500