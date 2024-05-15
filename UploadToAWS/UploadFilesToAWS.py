#Created by Shlomi Kiko
#Goal: This program uploads files to AWS using an API
#Linkedin: https://www.linkedin.com/in/shlomikiko/


import boto3
from aws_error_utils import errors
import os


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


#Testing purposes:
# fileName = 'C:/Python/Backup/PreviousBackups/BackupTest.zip'
# bucketName = 'TestBucket'

# UploadFile(fileName, bucketName)


