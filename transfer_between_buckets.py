import boto3

client = boto3.client('s3')
src_bucket = ""
dest_bucket = ""

def transfer_file(key):
    '''
    Copy object from one bucket to another
    '''
    copy_source = {
        'Bucket': src_bucket,
        'Key': key
    }
    client.copy_object(CopySource=copy_source, Bucket=dest_bucket, Key=key)
    print(f"'{key}' copied to '{dest_bucket}'")
