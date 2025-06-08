import boto3
import os
import pathlib

#* create client
client = boto3.client('s3')

# declare bucket name
bucket_name = ""

def download_file_from_s3(Bucket=bucket_name, object_name="test.txt", file_name="downloaded_test.txt"):
    """
    Download a file from an S3 bucket
    :param file_name: File to download
    :param bucket: Bucket to download from
    :param object_name: S3 object name. If not specified then file_name is used
    """
    client.download_file(
        Bucket=Bucket, 
        Key=object_name, 
        Filename=file_name
    )
    #!The download_fileobj method accepts a writeable file-like object. The file object must be opened in binary mode, not text mode.
    '''
    with open('FILE_NAME', 'wb') as f:
    s3.download_fileobj('amzn-s3-demo-bucket', 'OBJECT_NAME', f)
    '''

download_file_from_s3()
