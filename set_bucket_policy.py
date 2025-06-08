import boto3
import json

client = boto3.client('s3')
bucket_name = ""

def set_bucket_policy():
    '''
    Set public-read policy to bucket
    '''
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AddPerm",
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:GetObject"],
                "Resource": f"arn:aws:s3:::{bucket_name}/*"
            }
        ]
    }

    client.put_bucket_policy(
        Bucket=bucket_name,
        Policy=json.dumps(policy)
    )
    print("Bucket policy set to public-read.")
