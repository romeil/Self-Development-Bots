import openai
import os
from dotenv import load_dotenv
from system_role import messages


load_dotenv("chatgpt_key.env")
openai.api_key = os.getenv("API_KEY")

def ChatBot(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages
    )
    chatbot_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": chatbot_reply})
    return chatbot_reply