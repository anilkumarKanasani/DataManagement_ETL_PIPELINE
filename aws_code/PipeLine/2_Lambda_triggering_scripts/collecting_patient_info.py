
import boto3
import json
import time

s3_client = boto3.client("s3")
bucket_name = "dumped-patient-info"
file_name = "PatientInfo.csv"


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table("patient-info")

def trigger_patient_info(event , context ):
    