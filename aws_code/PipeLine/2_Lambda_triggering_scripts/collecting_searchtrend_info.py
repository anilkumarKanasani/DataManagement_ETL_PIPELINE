
import boto3
import json
import time

s3_client = boto3.client("s3")
bucket_name = "dumped-search-trend-south-korea"
file_name = "SearchTrend.csv"


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table("search-trend-south-korea")

def trigger_searchtrend_info(event , context ):
    