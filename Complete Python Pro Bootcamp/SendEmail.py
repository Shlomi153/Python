#Created by Shlomi Kiko
#Topic: Simple program for sending emails
#Linkedin: https://www.linkedin.com/in/shlomikiko/

import smtplib as smtp

email = 'SenderEmail'
password = 'SenderPassword'
smtpDomain = 'smtp.gmail.com'
port = 587

subject = 'Test Email'
body = 'This lovely email is meant as a test :)'
message = f'Subject:{subject}\n\n{body}'#The two \n are important for the body text to be displayed properly

with smtp.SMTP(smtpDomain, port=port) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs='RecipientEmail', msg=message)
    print('Message sent successfully!')
