import boto3

client = boto3.client('s3')
bucket_name = ""

def search_file_by_prefix(prefix):
    '''
    List all objects that start with given prefix
    '''
    response = client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    if 'Contents' in response:
        for item in response['Contents']:
            print(f"Found: {item['Key']}")
    else:
        print("No files found with given prefix.")
