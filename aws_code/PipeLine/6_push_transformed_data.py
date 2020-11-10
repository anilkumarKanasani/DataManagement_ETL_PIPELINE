# SDK Client for AWS
import boto3
import os

# Getting the path for all local CSV Files
data_set_local_path = 'D:/DataManagement-2/Transfomed_files/'
list_of_transformed_files = os.listdir(data_set_local_path) # List of all files in that local folder

# S3 client to interact with AWS S3 resources
s3_client = boto3.resource('s3')

# Capturing our transformed bucket name
BUCKET = "transformed-data"


# Looping overall local files and uploading into transformed-data-lake file by file into the same bucket ( lake )
for file in list_of_transformed_files:
    local_file = data_set_local_path + file
    s3_client.Bucket(BUCKET).upload_file(local_file, file)

print("The Transfomed data is pushed into DataWareHouse")



