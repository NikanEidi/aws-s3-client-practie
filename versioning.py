import boto3

client = boto3.client('s3')
bucket_name = "nikan-s3-test"

def enable_bucket_versioning():
    '''
    Enable versioning for the bucket
    '''
    client.put_bucket_versioning(
        Bucket=bucket_name,
        VersioningConfiguration={
            'Status': 'Enabled'
        }
    )
    print("Versioning enabled.")
