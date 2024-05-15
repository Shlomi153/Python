#Created by Shlomi Kiko
#Goal: This program sends out attachments to a list of contacts from a file.
#Linkedin: https://www.linkedin.com/in/shlomikiko/

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

#Main program
try:
    with open('./Templates/Template', encoding='utf-8') as template:
        template = template.read()

    df_contacts = pd.read_excel('./Recipients/SourceFileWithContacts.xlsx')

    print('\nColumns in the DataFrame:')
    print(df_contacts.dtypes)

    df_contacts = df_contacts[df_contacts['Email'].notnull()]

    #DataFrame of contacts
    print('\nDataFrame of contacts we are sending an email to:')
    print(df_contacts)

    print('\n\nList of files sent out:')

    #Overwrite the entire file so that only the current missing files will be registered
    with open('./Errors/MissingFiles.txt', 'w') as missingFiles:
        missingFiles.write('')

    countMissingFiles = 0

    #Admin confirmation before sending out the emails
    confirmation = input('Enter: "approve" if you are satisfied with the list to be sent out.\n')
    print('\n')

    listInserted = []
    with open('./Errors/InsertedItems.text', 'w') as insertedItems:
        insertedItems.write('')
    with open('./Errors/InvalidEmails.txt', 'w') as invalidEmails:
        invalidEmails.write('')

    totalSentcontacts = 0
    totalInvalidEmails = 0

    if confirmation == 'approve':
        for index, row in df_contacts.iterrows():
            recipient = row['Email']
            testID = row['seller_id']
            testFile = glob(f'./Attachments/single_contacts_files/{testID}_*')
            #If file does not exist for the sellerID, it will not be considered in the SendMail function
            if not testFile:
                countMissingFiles += 1
                print(f'File does not exist for SellerID: {testID}')
                #Append any additional missing files
                with open('./Errors/MissingFiles.txt', 'a') as missingFiles:
                    missingFiles.write(f'File missing for SellerID: {testID}\n')
                continue
            if not('@' in recipient and '.' in recipient):
                print(f'{testID} does not have a valid email, check the Errors folder.')
                with open('./Errors/InvalidEmails.txt', 'a') as invalidEmails:
                    invalidEmails.write(f'Invalid email for SellerID: {testID}\n')
                totalInvalidEmails += 1
                continue
            #Full path without list
            listInserted.append(testID)
            print(testFile[0])
            SendEmail(recipient=recipient, template=template, testFile=testFile[0])
            totalSentcontacts += 1
    else:
        print('Program cancelled: list not approved!')
        raise('Program terminated!')

    totalMissingFiles = f'\nTotal missing files: {countMissingFiles}, for more information check the Errors folder.'
    print(totalMissingFiles)

    totalInvalidEmails = f'\nTotal invalid Emails: {totalInvalidEmails}, for more information check the Errors folder.'
    print(totalInvalidEmails)

    print(f'\nTotal contacts mailed: {totalSentcontacts}, full list in the Completed folder.')
    
    currentDatetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    completedExcel = f'CompletedListcontacts_{currentDatetime}.xlsx'
    completedExcel = rf'{completedExcel}'
    pathForExcel = 'C:/Python/Emailstest/Completed/' + completedExcel
 
    df_contacts.to_excel(f'{pathForExcel}')

    programCompletion = """
    ######################################################
    Program completed successfully!
    ######################################################
    """

    print(programCompletion)

except Exception as e:
    programFailure = """
    ######################################################
    Program failed!
    ######################################################
    """

    print(programFailure)
    if e is None:
        raise('\nJob failed due to unknown error.')
    else:
        print('\nJob failed due to error: ' + str(e))
        raise(e)
finally:
    with open('./Errors/InsertedItems.text', 'a') as insertedItems:
        for i in listInserted:
            insertedItems.write('Inserted SellerID: ' + str(i) + '\n')
    gc.collect()