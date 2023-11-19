--Created by Shlomi Kiko
--Topic: Simple script to automate moving files with Python
--Linkedin: https://www.linkedin.com/in/shlomikiko/

from zipfile import ZipFile
from datetime import datetime
from glob import glob
import shutil
import os

timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")

zipFileName = 'PP_Backup_' + str(timestamp)

sourceFolder = 'D:/Test/'
sourcePath = sourceFolder + zipFileName

destinationFolder = 'D:/Test/Previous/'
destinationPath = destinationFolder + zipFileName

with ZipFile(sourcePath, 'w') as archive:
    for name in glob(sourceFolder + 'PP*.txt'):
        archive.write(name)

#Moves zip file
shutil.move(sourcePath, destinationPath)

#Gets all files in destination and sorts descending
listOfFiles = os.listdir(destinationFolder)
listOfFiles.sort(reverse = True)

#Remove the two last files from the list to be deleted
del listOfFiles[0:2]

#Deletes all files save for the 2 last ones
for i in listOfFiles:
    os.remove(destinationFolder + i)
