import os

def check_file_info(file_name):
    '''
    Check file size and extension before upload.
    '''
    if os.path.exists(file_name):
        size = os.path.getsize(file_name)
        ext = os.path.splitext(file_name)[1]
        print(f"File: {file_name}")
        print(f"Size: {size} bytes")
        print(f"Type: {ext}")
    else:
        print("File not found.")