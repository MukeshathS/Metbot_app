
from flask import Flask, render_template, request, redirect, url_for
import random
import smtplib

sender = 'no_reply@mydomain.com'


files = ["Execution Report", "Project Report", "Defect Report", "Release Report", "Validation Report"]

start_convo = False
met_item = ""
soeid = ""

bot_text = '\n\n' + "Say 'Hi' to start a new conversation!" + '\n\n'

greetings = ["Hi! How are you doing today?","Hi! How are you?","Hello!","Good Day!",
             "Hi! How may I help you?","Hello! How shall I help you"]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    
    global start_convo, met_item, soeid
    
    bot_text = ""
    if user_text == "Hi":
        start_convo = True
        bot_text = '<br>'.join([random.choice(greetings), 
                              "The following are the list of items that I can help you with - ", "1. Project Report", 
                              "2. Release Report", "3. Validation Report", " ", 
                              "Please enter the respective item number - "]) + '\n\n'

    elif start_convo == True:
        if user_text == "1":
            met_item = "Project Report"
            bot_text = "Please enter your SOEID as: \n 'soeid - ab12345' " + '\n'
        elif user_text == "2":
            met_item = "Release Report"
            bot_text = "Please enter your SOEID as: \n 'soeid - ab12345' " + '\n'
        elif user_text == "3":
            met_item = "Validation Report"
            bot_text = "Please enter your SOEID as: \n 'soeid - ab12345' " + '\n'
        elif user_text == "4":
            met_item = "Release Report"
            bot_text = "Please enter your SOEID as: \n 'soeid - ab12345' " + '\n'
        elif user_text[:5] == "soeid":
            bot_text = '<br>'.join(["Thank You! We will email you the requested report.", 
                                  " ", "Say 'Hi' to start a new conversation!"]) + '\n\n'
            soeid = user_text[-7:]
            start_convo = False
        else:
            bot_text = '\n\n' + "Say 'Hi' to start a new conversation!" + '\n\n'
            start_convo = False

    else:
        bot_text = '\n\n' + "Say 'Hi' to start a new conversation!" + '\n\n'
        start_convo = False
    
    if met_item != "" and soeid != "":
        m = met_item
        s = soeid
        soeid = ""
        met_item = ""
        met_sid(m,s)
    
    return bot_text

def met_sid(m,s):
    
    if m in files:
        print(m, " in files." )
        receivers = ['mukeshnath.s93@gmail.com']
        message = """From: No Reply <no_reply@mydomain.com>
        To: Person <mukeshnath.s93@gmail.com>
        Subject: Test Email
        
        This is a test e-mail message.
        """
        
        try:
           smtpObj = smtplib.SMTP('localhost')
           smtpObj.sendmail(sender, receivers, message)         
           print("Successfully sent email")
        except smtplib.SMTPException:
           print("Error: unable to send email")
        
    else:
        print(m, " not in files.")


if __name__ == "__main__":
    app.run()
