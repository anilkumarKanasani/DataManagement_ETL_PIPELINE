
import boto3
import json
import time

s3_client = boto3.client("s3")
bucket_name = "dumped-time-provience"
file_name = "TimeProvince.csv"


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table("time-provience")

def trigger_time_provience(event , context ):
    