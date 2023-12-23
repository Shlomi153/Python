#Created by Shlomi Kiko
#Topic: Fun program that sends out random Motivational quotes on a specific day
#Linkedin: https://www.linkedin.com/in/shlomikiko/

import pandas as pd
from datetime import date
import random as rnd
import smtplib as mail

#Directory
folderDir = './Files/'
fileName = 'Quotes.txt'

#Create a DataFrame and read the CSV into it
dfQuotes = pd.read_csv(folderDir + fileName, header=None, names=['Quote'])

#Ensure you can read the entire text in the columns
pd.options.display.max_colwidth = 500

#Replace any problematic escape sequences with something easier to catch
badSubstr = "\r\n"
replaceWith = '""'
dfQuotes['Quote'] = dfQuotes['Quote'].str.replace(badSubstr, replaceWith)

#Split it into seperate columns so that you can quickly filter out the bad rows
dfQuotes[['Quote', 'Author', 'Extra']] = dfQuotes.Quote.str.split(' - ', expand=True)

#Contains the rows that had issues for further review
rowsWithProblems = dfQuotes[dfQuotes['Extra'].notnull()]
rowsWithProblems = rowsWithProblems.drop('Quote', axis=1)

#Filter out the rows which are problematic in the DataFrame
dfQuotes = dfQuotes.loc[dfQuotes.Extra.isnull()]
dfQuotes = dfQuotes.drop('Extra', axis=1)

#Set up the variables including random for the further steps
today = date.today()
totalRows = len(dfQuotes)
randNum = rnd.randint(0, totalRows)

#Smtp connection to send mail
server = 'smtp.gmail.com'
port = 587
senderEmail = ''
senderPassword = ''
recipientEmail = ''

#If it's Saturday, then send out the email with a random quote
if(today.weekday() == 5):
        author = dfQuotes.Author.iloc[randNum]
        quote = dfQuotes.Quote.iloc[randNum]
        message = f'Quote: {quote}\nAuthor: {author}'

        mailSubject = 'Motivational Quote'
        mailMessage = f'Subject:{mailSubject}\n\n{message}'

        with mail.SMTP(server,port) as connection:
            connection.starttls()
            connection.login(senderEmail, senderPassword)
            connection.sendmail(from_addr=senderEmail,to_addrs=recipientEmail, msg=mailMessage)
            print('Mail sent successfully!')