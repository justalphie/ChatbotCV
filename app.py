import os
import gradio as gr
import cohere  



COHERE_KEY = os.getenv('COHERE_KEY')
co = cohere.Client(COHERE_KEY)

#list_history = [["question", "answer"], ["how", "how what..."]]
def convert_history(list_history):
    chat_history = [
        {"role": "SYSTEM", "text": open("prompt.md","r",encoding="UTF-8").read()}
    ]
    for item in list_history:
        dict_chat = {"role": "USER", "text": item[0]}
        chat_history.append(dict_chat)
        dict_chat = {"role": "CHATBOT", "text": item[1]}
        chat_history.append(dict_chat)
    return chat_history
        



def reply(message:str, history:list):
    chat_history = convert_history(history)
    response = co.chat(
        message=message,
        chat_history=chat_history,
        model="command-nightly",
        temperature=0.25
    )
    answer = response.text
    return answer






gr.ChatInterface(reply).launch()