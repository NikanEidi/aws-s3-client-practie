import boto3 #Bridge between AWS and Our code
import os
import pathlib #provides convenient shorthand methods for reading files as either text or raw bytes
from botocore.exceptions import ClientError

'''
In this practice we install s3 server and now we want to connect to our server so we need to create Bucket 
We have 2 types of Buckets -> client which is low level API (we use this type in this practice)
                           -> resource which is High level oop and it is easier to use -> easy resource
'''

#* crate client
client = boto3.client('s3', region_name='ca-central-1')

#declare variable
bucket_name = ''

#* Declare Bucket function
def bucket():
    '''
    This function will create Bucket and If it was already exist or has error shows in output
    '''
    try: 
        client.head_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' already exists and is accessible.")
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            response = client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': 'ca-central-1'
                }
            )
            print(f"Bucket '{bucket_name}' created successfully.")
        else:
            print(f"Error checking or creating bucket: {e}")

#* Declare Upload function 
def upload_file_to_s3(file_name, bucket = bucket_name, object_name=None):
    """
    Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    try:
        # Get the full path to the file in the same folder as this script
        file_name = os.path.join(pathlib.Path(__file__).parent.resolve(), "test.txt")
        
        # If the file doesn't exist, create it and write a test message
        if not os.path.exists(file_name):
            file = open(file_name, "a")
            file.write("This is an Upload Test by Nikan")
            file.close()

        # If no S3 object name is given, use the file name
        if object_name is None:
            object_name = "test.txt"

        # Upload the file to the specified S3 bucket
        client.upload_file(
            Filename=file_name,
            Bucket=bucket,
            Key=object_name
        )
        print(f"'{file_name}' uploaded to bucket '{bucket}' as '{object_name}'.")
    
    except Exception as e:
        # Print error if upload fails
        print(f"Failed to upload file: {e}")

upload_file_to_s3("test.txt")

    





