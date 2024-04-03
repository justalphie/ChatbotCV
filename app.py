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
    response = co.chat_stream(
        message=message,
        chat_history=chat_history,
        model="command-nightly",
        temperature=0.25
    )
    text_so_far = ""
    for event in response:
        if event.event_type == 'text-generation':
            text_so_far += event.text
            yield text_so_far






description = """
<a href="https://www.linkedin.com/in/alfiya-khabibullina-7b13131b8/"><img src="https://media.licdn.com/dms/image/D4E35AQH3_TsZdDJqgQ/profile-framedphoto-shrink_400_400/0/1700140203397?e=1712768400&v=beta&t=zHg5UKxtG4sKD3tvV-0ojW-gsG8-QoJK672NklxdEBk" width="100" style="
    float: right;
    position: relative;
    top: -65px;
    right: 0px;
    width: 100px;
    border-radius: 100%;
"/></a>
Hello! 
💬 Use the text box below to ask questions about me and my work experience.
<nobr> 🗣️ Talk to me in English, Dutch, or French. </nobr>
<nobr> 🔗 [Check my LinkedIn profile!](https://www.linkedin.com/in/alfiya-khabibullina-7b13131b8/) </nobr>
"""

gr.ChatInterface(reply,
    title="Alfiya's Curriculum Vitae",
    description=description
).launch()