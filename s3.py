import boto3
import random
import logging
from botocore.exceptions import ClientError
import time

bucket_name = 'jbalderas-session1'       #insert bucket name following the AWS Bucket naming rules
s3 = boto3.resource('s3')
new_bucket = s3.Bucket(bucket_name)

def check_bucket():                #Function created to check if bucket has been previously made and if not to create a new one
    if new_bucket.creation_date:
        print("That bucket exists. Change the bucket name")
        exit()
    else:
        print("creating",bucket_name)
        s3_client = boto3.client('s3')
        s3_client.create_bucket(Bucket=bucket_name)
        print(bucket_name,"Created")
check_bucket()

def write_file():               #This function creates a text file and writes into that file and closes it 
    newFile = open("template.txt", "x")
    newFile.write("Welcome to your new file!")
    newFile.close()
write_file()    

def upload():                   #This function uploads the file into the S3 bucket in a folder named 'session3' and renaming the file to template followed by 5 random bytes
    rand = random.randbytes(5)
    s3key = 'session3/' + '-' + 'template' + str(rand)

    try:
        data = open('template.txt', "rb")
        s3.Bucket(bucket_name).put_object(Key=s3key, Body=data)
    except ClientError as e:
        logging.error(e)
        return False
    return True
upload()


#the command to terminate the s3 bucket
#aws s3 rb s3://<bucket_name> --force