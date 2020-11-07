
import boto3
import json
import time

s3_client = boto3.client("s3")
bucket_name = "dumped-time-gender"
file_name = "TimeGender.csv"


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table("time-gender")

def trigger_time_gender(event , context ):
    