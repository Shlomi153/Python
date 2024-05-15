m#Created by Shlomi Kiko
#Goal: Simple script to send mails with Python
#Linkedin: https://www.linkedin.com/in/shlomikiko/

import smtplib as smtp
import gc
import pandas as pd
from email.message import EmailMessage
from glob import glob
from datetime import datetime

def SendMail():
   import smtplib, ssl
   smtpServer = ""
   port = 587  # For starttls

   senderEmail = ""
   senderUser = ""

   password = ""

   sendTo = ["", ""]

   subject = 'Test'
   body = 'This is a test'
      
   emailText = f"""Subject:{subject}\n\n
   {body}
   """

   # # Create a secure SSL context
   # context = ssl.create_default_context()

   # Try to log in to server and send email
   try:
      with smtplib.SMTP(smtpServer, port) as connection:
         connection = smtplib.SMTP(smtpServer,port)
         connection.starttls() # Secure the connection
         connection.login(senderUser, password)
         connection.sendmail(from_addr=senderEmail, to_addrs=sendTo, msg=emailText)
      print('Email sent successfully!')
   except Exception as e:
      #Display error message
      print(e)

SendMail()


Second approach, latest one:

import smtplib as smtp
import gc
import pandas as pd
from email.message import EmailMessage
from glob import glob
from datetime import datetime

def SendEmail(recipient, template, file):
   smtpServer = ""
   port = 587  # For starttls

   #senderEmail = ""
   senderUser = ""
   password = ""
   
   # Create email message
   msg = EmailMessage()
   msg['Subject'] = ''
   msg['From'] = ''
   msg['To'] = recipient
   msg.set_content(template)

   with open('./Attachments/pngTest.png', 'rb') as pngTest:
      pngTest = pngTest.read()
   msg.add_attachment(pngTest, maintype='image', subtype='png', filename='pngTest.png')

   with open('./Attachments/xlsxTest.xlsx', 'rb') as xlsxTest:
       msg.add_attachment(xlsxTest.read(), maintype='application', subtype='xlsx', filename=xlsxTest)

   with open('./Attachments/pdfTest1.pdf', 'rb') as pdfTest1:
       msg.add_attachment(pdfTest1.read(), maintype='application', subtype='pdf', filename='pdfTest1.pdf')

   with open('./Attachments/pdfTest2.pdf', 'rb') as pdfTest2:
       msg.add_attachment(pdfTest2.read(), maintype='application', subtype='pdf', filename='pdfTest2.pdf')

   # Send email message
   try:
      with smtp.SMTP(smtpServer, port) as connection:
         #Secure connection
         connection.starttls()
         connection.login(senderUser, password)
         connection.send_message(msg)
         print('Email sent successfully!')
   except Exception as e:
        if e is None:
            raise Exception('\nJob Failed due to unknown exception')
        else:
            print('\nJob failed due to error:')
            raise Exception('Job failed due to exception: ' + str(e))
