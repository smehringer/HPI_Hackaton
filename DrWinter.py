# -*- coding: utf-8 -*-
#########################################
#Created on Sat Jun 11 20:11:59 2016#    
#@author: Lennard Epping                #
#@contact: lennard.epping@fu-berlin.de  #
#########################################

from flask import Flask, request, redirect #sudo apt-get install python-virtualenv
import twilio.twiml

app = Flask(__name__)
# Try adding your own number to this list!
callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil"}
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    from_number = request.values.get('From', None)
    message=request.values.get('Body',None)
    print message
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Monkey, thanks for the message!"
    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp), str(message)

if __name__ == "__main__":
    app.run(debug=True)
    