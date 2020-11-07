
import boto3
import json
import time

s3_client = boto3.client("s3")
bucket_name = "dumped-time-reported"
file_name = "Time.csv"


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table("time-reported")

def trigger_time(event , context ):
    