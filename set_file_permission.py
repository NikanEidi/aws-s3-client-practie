import boto3

client = boto3.client('s3')
bucket_name = "nikan-s3-test"

def set_file_permission(object_name):
    '''
    Set individual file ACL to public-read
    '''
    client.put_object_acl(Bucket=bucket_name, Key=object_name, ACL='public-read')
    print(f"'{object_name}' permission set to public-read.")
