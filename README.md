---
title: ChatbotCV
short_description: Ask questions about my resume.
emoji: 📝
colorFrom: yellow
colorTo: yellow
sdk: gradio
sdk_version: 4.25.0
app_file: app.py
pinned: true
---

# ChatbotCV
You can ask this chatbot questions about my resume. Use this [link!](https://huggingface.co/spaces/justalphie/ChatbotCV)

The chatbot is built using Cohere Chat, and the data comes from the `prompt.md` file.

## Description
The chatbot uses [Cohere's Command model](https://cohere.com/command) and displays the results using [Gradio interface](https://www.gradio.app/guides/creating-a-chatbot-fast).

## Development steps
The chatbot uses the ```prompt.md``` file as a prompt. It contains the instructions to the model as well as the resume of the candidate.

The ```convert_history``` function takes a prompt and adds it to history. It also converts Gradio's input message and chat history structure into the structure accepted by Cohere's model.

The ```reply``` function takes the chat history and user's input as arguments, and streams the answer of the model. 

Finally, the chatbot is launched. 
```
gr.ChatInterface(reply,
    title="Alfiya's Curriculum Vitae",
    description=description
).launch()
``` 

To host the ChatbotCV [HuggingFace Spaces](https://huggingface.co/spaces) were used.


## Configuration
If you would like to create a similar chatbot for your own CV, you will need to make an account on Cohere and HuggingFace, define the Key for your Cohere Client as a system variable on your own computer. Please, do not forget to mention the author [Alfiya Khabibullina](https://github.com/justalphie).


## Contact
The author of the project is Alfiya Khabibullina.

To reach out for support or further information, ideas or suggestions, please contact [me on github](https://github.com/justalphie) or [find me on LinkedIn](https://www.linkedin.com/in/alfiya-khabibullina-7b13131b8/)
