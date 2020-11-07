
import boto3

s3_client = boto3.client("s3")
bucket_name = "dumped-time-reported"
file_name = "Time.csv"


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table("time-reported")

def trigger_time(event , context ):
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
            table.put_item(
                Item = {
                        "RECORD_ID" : record[0],
                        'DATE': record[1],
                        'TIME': record[2],
                        'TEST': record[3],
                        'NEGATIVE': record[4],
                        'CONFIRMED': record[5],
                        'RELEASED': record[6],
                        'DECEASED': record[7]
                        }
                    )
    except :
        missed_records += 1
    