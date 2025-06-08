import boto3

client = boto3.client('s3')
bucket_name = "nikan-s3-test"

def multipart_upload(file_path, object_name):
    '''
    Upload large file using multipart upload
    '''
    transfer_config = boto3.s3.transfer.TransferConfig(multipart_threshold=1024*25, max_concurrency=10)
    client.upload_file(file_path, bucket_name, object_name, Config=transfer_config)
    print("Multipart upload completed.")