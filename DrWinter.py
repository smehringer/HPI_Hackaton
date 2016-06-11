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
Deseases=["Herpes genitalis","Herpes labialis","Syphilis","Chlamydia","HPV,Gonorrhea","Crabs,Scabies",\
"Hepatitis B","Herpes genitalis","Herpes labialis","Syphilis","Chlamydia","HPV","Gonorrhea","Crabs Scabies",\
"Hepatitis B","Hepatitis C","Mycoplasma hominis infection","Trichomoniasis","Ureaplasma infection",\
"Candidiasis","Bacterial vaginosis","Pregnant","Hepatitis C","Mycoplasma hominis infection","Trichomoniasis",\
"Ureaplasma infection", "Candidiasis","Bacterial vaginosis"]

app = Flask(__name__)
# Try adding your own number to this list!

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    from_number = request.values.get('From', None)
    message=request.values.get('Body',None)
    x= validate(message)
    valid=x[0]
    char=x[1]
    if valid:
        query=prep_data(message, char)
        desease_class=data_predict.testData(query)
        message = " Thanks for the message! You probably have "+ Deseases[int(desease_class[0])]
        
    else:
        message = "Hi and welcome,\n please indicate from which  of the following symptoms you are suffering from by sending me a sms containing all the numbers associated with the symptoms you can observe seperated by only commas.\nSymptoms:\n   \nThank you for using my services!\nDr. Winter"
    resp = twilio.twiml.Response()
    resp.message(message)    
    return str(resp)

def validate(message_sent):
	matchcom = re.search(r"[0-9,]+", message_sent)
	validcom = ((matchcom.start()==0) and (matchcom.end()==len(message_sent)))
	matchsem = re.search(r"[0-9;]+", message_sent)
	validsem = ((matchsem.start()==0) and (matchsem.end()==len(message_sent)))
	matchbla = re.search(r"[0-9' ']+", message_sent)
	validbla = ((matchbla.start()==0) and (matchbla.end()==len(message_sent)))
	
	if validcom:
		return [validcom, ","]
	elif validsem:
		return [validsem, ";"]
	elif validbla:
		return [validbla, " "]
	else:
		return [False, "u"]
def prep_data(message,char):
    symptoms=[0]*16
    message=message.split(char)
    for symp in message:
        symptoms[int(symp)]=1
    return symptoms
    
    
if __name__ == "__main__":
    app.run(debug=True)
    