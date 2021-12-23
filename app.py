from flask import Flask
from flask_mail import Mail, Message
from flask_mail import smtplib
import spredsheet
from datetime import datetime
import time
app =Flask(__name__)
mail=Mail(app)
#connecting to my gmail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'chaymamchirgui@gmail.com'
app.config['MAIL_PASSWORD'] = 'chaymoucha'
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



#4
@app.route("/")  
def index(): 
 try:    
    for j in range(2,spredsheet.sheet.row_count):
     try: 
        for i in spredsheet.sheet.row_values(j):
            if(i=='Applied'):
                spredsheet.sheet.update_cell(j,4,'Online Test Sent')
                spredsheet.sheet.update_cell(j,5,datetime.now().isoformat())
                msg = Message("hi",sender = 'chaymamchirgui@gmail.com')
                a=spredsheet.sheet.cell(j,2).value.split('\n')[0]
                msg.add_recipient(a)
                msg.body = "Thank you for applying to"+"  "+spredsheet.sheet.cell(j,3).value
                mail.send(msg)
                time.sleep(1) 
            elif (i=='Online Test Sent' and (datetime.now()-datetime.strptime(spredsheet.sheet.cell(4,5).value,'%m/%d/%Y %H:%M:%S')).days>=7 and spredsheet.sheet.cell(j,6).value==None):
                 spredsheet.sheet.update_cell(j,4,'Reminder Sent')
                 spredsheet.sheet.update_cell(j,5,datetime.now().isoformat())
                 msg = Message("hi",sender = 'chaymamchirgui@gmail.com')
                 a=spredsheet.sheet.cell(j,2).value.split('\n')[0]
                 msg.add_recipient(a)
                 msg.body = "You haven’t submitted your test. Everything okay?"
                 mail.send(msg)
                 time.sleep(1) 
            elif(i=='Submitted Test' and int(spredsheet.sheet.cell(j,6).value.split('/')[0])< int(spredsheet.sheet.cell(j,6).value.split('/')[1])/2 ) :  
                  spredsheet.sheet.update_cell(j,4,'Refusal Mail Sent')
                  spredsheet.sheet.update_cell(j,5,datetime.now().isoformat())
                  msg = Message("hi",sender = 'chaymamchirgui@gmail.com')
                  a=spredsheet.sheet.cell(j,2).value.split('\n')[0]
                  msg.add_recipient(a)
                  msg.body = "We are sorry to tell you that you did not pass the test"
                  mail.send(msg)
                  time.sleep(1) 
            elif(i=='Submitted Test' and int(spredsheet.sheet.cell(j,6).value.split('/')[0])>= int(spredsheet.sheet.cell(j,6).value.split('/')[1])/2 ) :  
                  spredsheet.sheet.update_cell(j,4,'Interview Mail Sent')
                  spredsheet.sheet.update_cell(j,5,datetime.now().isoformat())
                  msg = Message("hi",sender = 'chaymamchirgui@gmail.com')
                  a=spredsheet.sheet.cell(j,2).value.split('\n')[0]
                  msg.add_recipient(a)
                  msg.body = "Congratulations for passing the test. You’ll have an interview with _____"
                  mail.send(msg)
                  
                  
                
                
     except IndexError:
        break   
    #confirmation mail
    msg = Message("confirmation Mail",sender ='chaymamchirgui@gmail.com',recipients=['chaymamchirgui@gmail.com'])
    mail.send(msg)
    #return "message is sent to route"
    return ("message is sent")
 except:
    # error mail
    msg = Message("bug Mail",sender ='chaymamchirgui@gmail.com',recipients=['chaymamchirgui@gmail.com'])
    mail.send(msg) 

if __name__ == '__main__':
       app.run(debug = True)         
                         
