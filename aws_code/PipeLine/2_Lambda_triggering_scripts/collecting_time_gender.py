
import boto3

s3_client = boto3.client("s3")
bucket_name = "dumped-time-gender"
file_name = "TimeGender.csv"


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table("time-gender")

def trigger_time_gender(event , context ):
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
            if record[0].upper() != "RECORD_ID" :
                table.put_item(
                    Item = {
                            "RECORD_ID" : record[0],
                            'DATE': record[1],
                            'TIME': record[2],
                            'SEX': record[3],
                            'CONFIRMED': record[4],
                            'DECEASED': record[5]
                            }
                        )
    except :
        missed_records += 1