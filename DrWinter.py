# -*- coding: utf-8 -*-
#########################################
#Created on Sat Jun 11 20:11:59 2016    #    
#@author: Lennard Epping                #
#@contact: lennard.epping@fu-berlin.de  #
#########################################

from flask import Flask, request, redirect
import twilio.twiml
import re
import data_predict
Disease=["No Inflammation of urinary","Inflammation of urinary"]

app = Flask(__name__)
# Try adding your own number to this list!

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    from_number = request.values.get('From', None)
    message=request.values.get('Body',None)
      
    x=validate(message)
    print x
    valid=x[0]
    char=x[1]
    if valid:
        query=prep_data(message, char)
        disease_class=data_predict.testData(query)
        message = " Thanks for the message! You probably have "+ Disease[int(disease_class[0])]
        
    else:
        message = "Hi and welcome,\n please indicate from which  of the following symptoms you are suffering"+ \
        "from by sending me a sms containing all the numbers associated with the symptoms you can observe seperated"+\
        "by only commas.\nSymptoms:\n Temperature of patient(number) Occurrence of nausea(yes,no) Lumbar pain(yes, no)"+\
        "Urine pushing (yes, no) Micturition pains(yes,no), Burning of urethra(yes,no), itch(yes,no), swelling of urethra outlet(yes, no)"+\
        "\nThank you for using my services!\nDr. Winter"
    resp = twilio.twiml.Response()
    resp.message(message)    
    return str(resp)

def validate(message_sent):	
	matchcom = re.search(r"[0-9]{2}(,yes|,no){5}", message_sent)		
	matchsem = re.search(r"[0-9]{2}(;yes|;no){5}", message_sent)
	matchbla= re.search(r"[0-9]{2}( yes| no){5}", message_sent)
	
	if matchcom:
		return [True, ","]
	elif matchsem:
		return [True, ";"]
	elif matchbla:
		return [True, " "]
	else:
		return [False, "u"]
  
def prep_data(message,char):
    symptoms=[0]*6
    message=message.split(char)
    symptoms[0]=message[0]
    for i in range(1,len(symptoms)):
        if message[i]=="yes":
            symptoms[i]=1
        elif message[i]=="no":
            symptoms[i]=0
        
    return symptoms
    
    
if __name__ == "__main__":
    app.run(debug=True)
    