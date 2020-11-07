
import boto3
import json
import time

s3_client = boto3.client("s3")
bucket_name = "dumped-region-south-korea"
file_name = "Region.csv"


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table("region-south-korea")

def trigger_region_info(event , context ):
    