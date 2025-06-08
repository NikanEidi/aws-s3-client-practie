import boto3

client = boto3.client('s3')
bucket_name = ""

def upload_with_storage_class(file_name, object_name=None):
    '''
    Upload file with specific storage class (e.g., STANDARD_IA, GLACIER)
    '''
    if object_name is None:
        object_name = file_name

    client.upload_file(
        Filename=file_name,
        Bucket=bucket_name,
        Key=object_name,
        ExtraArgs={
            'StorageClass': 'STANDARD_IA'
        }
    )
    print(f"'{file_name}' uploaded with STANDARD_IA storage class.")
