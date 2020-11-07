
import boto3
import json
import time

s3_client = boto3.client("s3")
bucket_name = "dumped-hospital-record-cases"
file_name = "Case.csv"


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table("hospital-record-cases")

def trigger_hospital_record_cases(event , context ):
    try:
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_object
        response = s3_client.get_object(Bucket = bucket_name, Key = file_name)

        # response is a dict, with a stream body under "Body" key
        # from straming body, we can extract the data as follows
        data = response["Body"].read().decode("utf-8")
        records = data.split("\n")
        for record in records:
            record = record.split(",")
            if len(record) == 8:
                table.put_item(
                    Item = {
                        "CASE_ID" : record[0] ,
                        "PROVINCE" : record[1] ,
                        "CITY" : record[2] ,
                        "GROUP" : record[3] ,
                        "INFECTION_CASE" : record[4] ,
                        "CONFIRMED" : record[5] ,
                        "LATITUDE" : record[6] ,
                        "LONGITUTDE" : record[7]
                        }
                        )
            else:
                pass
    except :
        pass