import boto3
import os

client = boto3.client('s3')
bucket_name = "nikan-s3-test"

def upload_to_folder(file_name, folder_name="uploads", bucket=bucket_name):
    '''
    Upload a file to a virtual folder (prefix) in S3.
    '''
    object_name = f"{folder_name}/{os.path.basename(file_name)}"
    try:
        client.upload_file(file_name, bucket, object_name)
        print(f"Uploaded to '{folder_name}' as '{object_name}'.")
    except Exception as e:
        print(f"Upload to folder failed: {e}")