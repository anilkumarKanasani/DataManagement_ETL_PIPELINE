
import boto3

s3_client = boto3.client("s3")
bucket_name = "dumped-search-trend-south-korea"
file_name = "SearchTrend.csv"


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table("search-trend-south-korea")

def trigger_searchtrend_info(event , context ):
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
                            'RECORD_ID' : record[0],
                            'DATE': record[1],
                            'COLD': record[2],
                            'FLU': record[3],
                            'PNEUMONIA': record[4],
                            'CORONAVIRUS': record[5]
                            }
                        )
    except :
        missed_records += 1