import boto3

#* create client
client = boto3.client('s3')

# declare bucket name
bucket_name = ""

def list_files_from_s3(Bucket=bucket_name):
    '''
    This function lists all files (objects) in the specified S3 bucket.
    :param Bucket: The name of the S3 bucket
    '''
    try:
        response = client.list_objects_v2(Bucket=Bucket)
        if 'Contents' in response:
            print(f"Files in '{Bucket}':")
            for obj in response['Contents']:
                print(f"- {obj['Key']}")
        else:
            print(f"No files found in bucket '{Bucket}'.")
    except Exception as e:
        print(f"Failed to list files: {e}")

list_files_from_s3()
