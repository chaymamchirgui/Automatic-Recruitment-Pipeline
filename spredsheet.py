
import gspread
from gspread.models import Spreadsheet
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import pandas as pd
import re

# use creds to create a client to interact with the Google Drive API

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet

sheet = client.open("flasksheet").sheet1

# Extract and print all of the values
#list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)


#assert status is in list L
L=['Applied','Online Test Sent','Submitted Test','Reminder Sent','Interview Mail Sent','Refusal Mail Sent']
l=['name_1', 'name_2', 'name_3']
for i in sheet.col_values(4)[1:]:
    assert(i in L),i+'is not in list '
#assert id,email,project 
for j in sheet.get_all_records():
    assert(bool(re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",j['Email']))),j['Email']+'is not a valid Email'
    assert (j['Project'] in l),j['Project']+ 'is not a valid project'
    assert(j['ID']!=''),"ID shouldn't be left empty"
    nid=sheet.findall(str(j['ID']))
    nem=sheet.findall(j['Email'])
    for k in range(len(nid)):
       
           assert (nid[k].row==nem[k].row and len(nid)==len(nem)),"the email doesn't have a unique id" #to make sure the email has a unique id
        
    if(j['Status']!='Applied' and j['Status']!='Online Test Sent'and j['Status']!='Reminder Sent'):  
        #test score format score/total
        assert(bool(re.match(r"\d{2}\/\d{2}",str(j['Test_score'])))),'test_score doesnt match format score/total'   
        # Mail sent is a datetime
    if(j['Status']!='Applied'):
        assert(datetime.strptime(j['Mail_sent'],'%m/%d/%Y %H:%M:%S')),'Mail_sent is not type datetime'
   



   