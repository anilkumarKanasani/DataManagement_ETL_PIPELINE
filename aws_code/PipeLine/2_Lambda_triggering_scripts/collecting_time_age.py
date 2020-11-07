
import boto3
import json
import time

s3_client = boto3.client("s3")
bucket_name = "dumped-time-age"
file_name = "TimeAge.csv"


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table("time-age")

def trigger_time_age(event , context ):
    