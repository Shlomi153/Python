#Created by Shlomi Kiko
#Goal: This program uploads databases to AWS using an API
#Linkedin: https://www.linkedin.com/in/shlomikiko/

#Import libraries
import os
import gc
from datetime import datetime
from zipfile import ZipFile, ZIP_DEFLATED

#List of Databases to back up
databasesToBackup = ['Staging', 'Presentation']
currentTime = datetime.now().strftime('%Y%m%d_%H%M%S')

#Define where to Backup the databases and their names
backupDir = "C:/Python/BackupDWH/"
DWHDir = backupDir + 'PreviousBackups/BackupDWH'

#Zip the 2 Backup files together and compress them to save space
zipFileName = DWHDir + '/' +'Backup_DWH' + '_' + str(currentTime) + '.zip'
tempFolder = backupDir + 'Temp'
filesInTemp = os.listdir(tempFolder)

print('The following files have been included in the zip file:')
with ZipFile(zipFileName, 'w', compression=ZIP_DEFLATED) as zip:
    for file in filesInTemp:
        zip.write(tempFolder + '/' + file)
        print(file)

print('\n')

#Delete .bak files
for file in filesInTemp:
    os.remove(tempFolder + '/' + file)

#Keep only last 2 zip files in DWH folder

listDWHFiles = os.listdir(DWHDir)

#Reverse items so that the  ones are in the beginning, then delete them from the original list which are the zip files we want to keep
listDWHFiles.sort(reverse=True)
#File we will upload to AWS
awsFile = listDWHFiles[0]
#Delete the two est files from the list
del listDWHFiles[0:2]

#Remove all the files that are not in the original list, meaning only the 2 est ones will be kept
for file in listDWHFiles:
    filePath = DWHDir + '/' + file
    os.remove(filePath)
    print(filePath)

print('Backups successful for  DWH!\n')

###########################################################################################################################################

awsPart = """
#######################################################
Upload to AWS Bucket
#######################################################
"""
print(awsPart)

import boto3
from aws_error_utils import errors
import os
import shutil as sh

def UploadFile(file, bucket, objectName=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if objectName is None:
        objectName = os.path.basename(file)

    # Upload the file
    s3Client = boto3.client('s3')
    try:
        response = s3Client.upload_file(file, bucket, objectName)
    except errors.NoSuchBucket as error:
        print(error.message)
        return False
    return True

#Upload file to AWS Bucket
fileNameTill = '_20' #It's essentially a substring to ensure we don't take up too much storage in AWS
fileName = DWHDir + '/' + awsFile

#Target path for final file we want to upload, need to remove the timestamp to allow versioning in AWS
awsFileToUpload = 'C:/Python/BackupDWH/AWSUpload/' + awsFile
awsFileToUpload = awsFileToUpload.split(fileNameTill)[0] + '.zip'
bucketName = 'TestBackupBucket'

sh.move(fileName, awsFileToUpload)

UploadFile(file=awsFileToUpload, bucket=bucketName)

print(f'Completed upload for file: {awsFile} to AWS Bucket: {bucketName}')

#Garbage collector to free up memory quicker
gc.collect()