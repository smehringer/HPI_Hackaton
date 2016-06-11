# -*- coding: utf-8 -*-
#########################################
#Created on Sat Jun 11 20:11:59 2016#    
#@author: Lennard Epping                #
#@contact: lennard.epping@fu-berlin.de  #
#########################################

from flask import Flask, request, redirect #sudo apt-get install python-virtualenv
import twilio.twiml
import re
import data_predict

app = Flask(__name__)
# Try adding your own number to this list!

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    from_number = request.values.get('From', None)
    message=request.values.get('Body',None)
    print message
    if valid:
        query=prep_data(message, char)
        testData(query) 
    message = " Thanks for the message!"+
    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)

def prep_data(message,char):
    symptoms=[0]*10
    message=message.split(char)
    for symp in message:
        symptoms[symp]=1
    return symtomps
    
    
if __name__ == "__main__":
    app.run(debug=True)
    