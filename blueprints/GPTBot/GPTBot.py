import google.generativeai as genai
import os
from flask import Blueprint, jsonify, render_template, request
import requests



chatbot_bp = Blueprint('chatbot_api', __name__, template_folder='Templates')
@chatbot_bp.route("/chatbot", methods=['GET', 'POST'])
def route_chatbot():
    if request.method == 'POST':
        chat = request.form['prompt']
        mensagens_user = chat
        mensagens_bot = GPT_Generate(chat)
        return render_template("chatbot.html", mensagens_bot=mensagens_bot, mensagens_user=mensagens_user)
    else:
        return render_template("chatbot.html")


def GPT_Generate(prompt):
    genai.configure(api_key="AIzaSyCOS8abrrK3XqAeGwYXcjlWwxODjp2Hhu0")

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text