 Here's a brief breakdown:

Functionality: The Flask application connects to Gmail and checks a Google Sheet ("flasksheet"). It iterates through the rows in the sheet, updating the status and sending different email responses based on certain conditions.

Email Responses: It sends different emails like "Online Test Sent," "Reminder Sent," "Refusal Mail Sent," and "Interview Mail Sent" based on the status and other criteria in the spreadsheet.

Handling Exceptions: It handles exceptions and sends appropriate emails like "bug Mail" in case of an error and a "confirmation Mail" after processing the spreadsheet.

Assertions and Validations: The other file conducts various validations and assertions on the Google Sheet data, ensuring the correctness of information, email formats, and unique IDs for emails.

Status can be one of the following (Ordered): 
Applied
Online Test Sent
Submitted Test
Reminder Sent
Interview Mail Sent
Refusal Mail Sent

Your flask app will then do the following once the route has been pinged: 



If Status is Online Test Sent & Mail sent is at least 7 days old & Test Score is empty
→ Send an email saying “You haven’t submitted your test. Everything okay?”
→ Change Status to Reminder Sent
→ Change Mail sent to today’s datetime.



If Status is Submitted Test & Test Score is less than half the total 
→ Send an email saying “We are sorry to tell you that you did not pass the test”
→ Change Status to Refusal Mail Sent
→ Change Mail sent to today’s datetime.

If Status is Submitted Test & Test Score is more than half the total 
→ Send an email saying “Congratulations for passing the test. You’ll have an interview with _____” **
→ Change Status to Interview Mail Sent
→ Change Mail sent to today’s datetime.

5- Once the above was done, the app should send an error email if anything went wrong and a confirmation message if everything went well. The End.



 useful links:
 Sending Automated Emails in Flask: https://www.youtube.com/watch?v=ejLGwHiyqGU
 Python Google Sheets API Tutorial - 2019: https://www.youtube.com/watch?v=cnPlKLEGR7E



