
import boto3
import json
import time

s3_client = boto3.client("s3")
bucket_name = "dumped-weather-south-korea"
file_name = "Weather.csv"


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table("weather-south-korea")

def trigger_weather_info(event , context ):
   