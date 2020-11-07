# SDK Client for AWS
import boto3
import os

# Getting the path for all local CSV Files
data_set_local_path = 'D:/DataManagement-2/DS4C_DataSet_testing/'
list_of_dumped_files = os.listdir(data_set_local_path) # List of all files in that local folder

# S3 client to interact with AWS S3 resources
s3_client = boto3.resource('s3')

# Now we are uploading files into dumped-data-lake buckets (which is created by Terraform)
LIST_OF_BUCKETS = ["dumped-hospital-record-cases" , 
                "dumped-patient-info" , 
                "dumped-region-south-korea", 
                "dumped-search-trend-south-korea",
                "dumped-time-reported" , 
                "dumped-time-age" , 
                "dumped-time-gender" , 
                "dumped-time-provience" , 
                "dumped-weather-south-korea",
                ]


# Looping overall local files and uploading into dumped-data-lake file by file into the same bucket ( lake )
for file , BUCKET in zip(list_of_dumped_files , LIST_OF_BUCKETS):
    local_file = data_set_local_path + file
    s3_client.Bucket(BUCKET).upload_file(local_file, file)

print("The Present Set is uploaded in DataLake")



