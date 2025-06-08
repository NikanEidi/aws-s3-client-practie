import boto3
from botocore.exceptions import ClientError

#* create client
client = boto3.client('s3')

# declare bucket name
bucket_name = "nikan-s3-test"

def delete_file_from_s3(Bucket=bucket_name, object_name= None):
    '''
    This function checks if a file exists in an S3 bucket and deletes it if found.
    :param Bucket: The name of the S3 bucket
    :param object_name: The name of the object (file) to delete
    '''
    try:
        client.head_object(Bucket=Bucket, Key=object_name)
        response = client.delete_object(Bucket=Bucket, Key=object_name)
        print(f"Deleted '{object_name}' from '{Bucket}'.")
    except ClientError as e:
        if e.response['Error']['Code'] == "404":
            print(f"File '{object_name}' does not exist in bucket '{Bucket}'.")
        else:
            print(f"Error occurred: {e}")

delete_file_from_s3(object_name = "Nikan")
