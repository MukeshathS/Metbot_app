# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 14:01:54 2020

@author: Mukeshnath S
"""

from flask import Flask
from tkinter import *
import threading
import random

root = Tk()
start_convo = False
met_item = ""
soeid = ""

app = Flask(__name__)


def flask_main():
    app.run()
    
@app.route("/")
def index():
    return "Hello"

# @app.route("/Metbot")
# def metbot():
#     Met_Chatbot()


def Met_Chatbot():
    
    bot_text = '\n\n' + "Say 'Hi' to start a new conversation!" + '\n\n'
    
    greetings = ["Hi! How are you doing today?","Hi! How are you?","Hello!","Good Day!",
                 "Hi! How may I help you?","Hello! How shall I help you"]

    global start_convo, met_item, soeid
    
    def metchat():

        global start_convo, met_item, soeid

        user_text = user_input.get()
        user_input.delete(0, END)
        bot_text = ""
        if user_text == "Hi":
            start_convo = True
            bot_text = '\n'.join([user_text, random.choice(greetings), 
                                  "The following are the list of items that I can help you with - ", "1. Execution Report", 
                                  "2. Defect Report", "3. Project Validation Report", "4. Release Report", " ", 
                                  "Please enter the respective item number - "]) + '\n\n'

        elif start_convo == True:
            if user_text == "1":
                met_item = "Execution Report"
                #print(met_item)
                bot_text = "Please enter your SOEID as: \n 'soeid - ab12345' " + '\n'
            elif user_text == "2":
                met_item = "Defect Report"
                #print(met_item)
                bot_text = "Please enter your SOEID as: \n 'soeid - ab12345' " + '\n'
            elif user_text == "3":
                met_item = "Project Validation Report"
                #print(met_item)
                bot_text = "Please enter your SOEID as: \n 'soeid - ab12345' " + '\n'
            elif user_text == "4":
                met_item = "Release Report"
                #print(met_item)
                bot_text = "Please enter your SOEID as: \n 'soeid - ab12345' " + '\n'
            elif user_text[:5] == "soeid":
                bot_text = '\n'.join([user_text, "Thank You! We will email you the requested report.", 
                                      " ", "Say 'Hi' to start a new conversation!"]) + '\n\n'
                soeid = user_text[-7:]
                #print(soeid)
                start_convo = False
            else:
                bot_text = '\n\n' + "Say 'Hi' to start a new conversation!" + '\n\n'
                start_convo = False

        else:
            bot_text = '\n\n' + "Say 'Hi' to start a new conversation!" + '\n\n'
            start_convo = False
    
        T.insert(END, bot_text)   
        T.see(END)
            

    def press(event):
        metchat()
        #if met_item != "" and soeid != "":
            #return met_item, soeid

    def click():
        metchat()
        #if met_item != "" and soeid != "":
         #   return met_item, soeid

    #root = Tk()
    root.title('Metbot')
    root.geometry('400x500')

    frame = Frame(root)
    frame.pack(fill="both", expand=True)

    user_input = Entry(frame)
    user_input.place(x=6,y=412,height=82,width=290)

    button = Button(frame, text="Enter", command=click)
    button.place(x=302,y=412,height=82,width=80)

    T = Text(frame, height=5, width=30)
    T.place(x=6,y=6,height=400,width=384)
    S = Scrollbar(frame)
    S.pack(side = RIGHT, fill = Y)

    S.config(command = T.yview)
    T.config(yscrollcommand = S.set)

    T.insert(END, bot_text)   
    T.see(END)
    
    root.bind("<Return>",press)

    root.mainloop()
    
    return met_item, soeid


if __name__ == "__main__":
    fm = threading.Thread(target=flask_main)
    fm.daemon = True
    fm.start()
    
    met_item, soeid = Met_Chatbot()
    
    print(met_item, soeid)
    
