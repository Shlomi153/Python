#Created by Shlomi Kiko
#Goal: Simple script to automate moving files with Python
#Linkedin: https://www.linkedin.com/in/shlomikiko/

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