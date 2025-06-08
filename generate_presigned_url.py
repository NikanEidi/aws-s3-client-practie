import boto3

client = boto3.client('s3')
bucket_name = "nikan-s3-test"

def generate_presigned_url(bucket=bucket_name, object_name="test.txt", expiration=3600):
    '''
    Generate a secure temporary URL to access a file in S3.
    '''
    try:
        url = client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket, 'Key': object_name},
            ExpiresIn=expiration
        )
        print("Generated pre-signed URL:")
        print(url)
    except Exception as e:
        print(f"Error generating URL: {e}")