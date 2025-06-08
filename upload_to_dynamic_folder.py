import boto3

client = boto3.client('s3')
bucket_name = "nikan-s3-test"

def upload_to_dynamic_folder(file_path, folder_name):
    '''
    Upload file to virtual folder (prefix) like images/file.jpg
    '''
    object_name = f"{folder_name}/{file_path}"
    client.upload_file(file_path, bucket_name, object_name)
    print(f"'{file_path}' uploaded to folder '{folder_name}/'")
