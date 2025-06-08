import boto3
import os

client = boto3.client('s3')
bucket_name = "nikan-s3-test"

def upload_custom_file(file_name, bucket=bucket_name, object_name=None):
    '''
    Upload a custom file to S3 bucket.
    :param file_name: The local file path
    :param bucket: The S3 bucket name
    :param object_name: S3 object name (optional)
    '''
    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        client.upload_file(file_name, bucket, object_name)
        print(f"Uploaded '{file_name}' to '{bucket}' as '{object_name}'.")
    except Exception as e:
        print(f"Upload failed: {e}")