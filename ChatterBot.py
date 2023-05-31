#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install ChatterBot==1.0.4
pip install spacy 
python3
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli.download import download
download(model ="en_core_web_sm")

chatbot = ChatBot('Google')
trainer  = ListTrainer(chatbot)
custom_data = [
    'How are you?',
    'I am good, thank you!',
    'What is your favorite color?',
    'I don\'t have preferences as an AI',
    'Tell me a fun fact',
    'Did you know that honey never spoils?',
    'What do you like to do in your free time?',
    'As an AI, I don\'t have free time, but I enjoy helping and interacting with people!',
    'Do you have any pets?',
    'Since I am a virtual assistant, I don\'t have any pets.',
]
chatbot.storage.drop()
trainer.train(custom_data)
while True:
    user_data = input("You: ")
    if user_data == 'exit':
        break
    response = chatbot.get_response(user_data)
    print("ChatBot: ", response)


# In[ ]:




