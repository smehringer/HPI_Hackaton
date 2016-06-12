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
Disease=["Don't worry! So far there is no indication that you have a urinary inflammation =) Keep on being awesome!" ,
"Oh shit =( It seems you have several indication for a urinary inflammation. Please visit a doctor, drink a lot of water and get some rest."]
PS = ["PS: Help us improve our service! If you went to a doctor and got your diagnosis please tell us the result. If you do not agree to be reminded to do this in 2 weeks, reply with no Thank you very much and get well soon =)",
      "PS: Help us improve our service! If your symptoms disappear or you decide to consult a doctor please tell us the result. If you do not agree to be reminded to do this in 2 weeks, reply with no Thank you very much and get well soon =)"]
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
        message = Disease[int(disease_class[0])]
        message2 = PS[0]
        
    else:
        message = "Hi and welcome,\n please tell me from which symptoms you are suffering:\n\n Temperature of Patient (number)\n\n Occurrence of Nausea(yes,no)\n\n Lumbar pain(yes, no)\n\n"+\
    " Urine Pushing (yes, no)\n\n Micturition Pains (yes,no)\n\n Burning of Rrethra (yes,no)\n\n Itching (yes,no)\n\n Swelling of Urethra Outlet (yes, no)\n\n"+\
        "For example: 39,yes,no,yes,yes,no \nThank you for using my app!\nDr. Winter"
        message2 = PS[1]
    resp = twilio.twiml.Response()
    resp.message(message)    
    return str(resp)
    resp.message(message2)    
    return str(resp)

def validate(message_sent):	
	matchcom = re.search(r"[0-9]{2}(\.[0-9])?(,yes|,no){5}", message_sent)		
	matchsem = re.search(r"[0-9]{2}(\.[0-9])?(;yes|;no){5}", message_sent)
	matchbla= re.search(r"[0-9]{2}(\.[0-9])?( yes| no){5}", message_sent)
	
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
    