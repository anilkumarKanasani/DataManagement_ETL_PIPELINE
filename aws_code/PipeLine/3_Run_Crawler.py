
import boto3

glue_client = boto3.client('glue', region_name='eu-central-1')


response = glue_client.update_crawler( Name = "Create_ds4c_meta_data" )