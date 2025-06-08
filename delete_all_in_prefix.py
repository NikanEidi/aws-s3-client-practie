import boto3

client = boto3.client('s3')
bucket_name = ""

def delete_all_in_prefix(prefix):
    '''
    Delete all objects inside a given prefix (folder)
    '''
    response = client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    if 'Contents' in response:
        for item in response['Contents']:
            client.delete_object(Bucket=bucket_name, Key=item['Key'])
            print(f"Deleted: {item['Key']}")
