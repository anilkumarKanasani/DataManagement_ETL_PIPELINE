
import boto3

s3_client = boto3.client("s3")
bucket_name = "dumped-region-south-korea"
file_name = "Region.csv"


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table("region-south-korea")

def trigger_region_info(event , context ):
    missed_records = 0
    try:
        # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_object
        response = s3_client.get_object(Bucket = bucket_name, Key = file_name)

        # response is a dict, with a stream body under "Body" key
        # from straming body, we can extract the data as follows
        data = response["Body"].read().decode("utf-8")
        records = data.split("\n")
        for record in records:
            record = record.split(",")
            if record[0].upper() != "CODE" :
                table.put_item(
                    Item = {
                            'CODE': record[0],
                            'PROVINCE': record[1],
                            'CITY': record[2],
                            'LATITUDE': record[3],
                            'LONGITUDE': record[4],
                            'ELEMENTARY_SCHOOL_COUNT': record[5],
                            'KINDERGARTEN_COUNT': record[6],
                            'UNIVERSITY_COUNT': record[7],
                            'ACADEMY_RATIO': record[8],
                            'ELDERLY_POPULATION_RATIO': record[9],
                            'ELDERLY_ALONE_RATIO': record[10],
                            'NURSING_HOME_COUNT': record[11]
                            }
                        )
    except :
        missed_records += 1