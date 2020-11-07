
import boto3

s3_client = boto3.client("s3")
bucket_name = "dumped-weather-south-korea"
file_name = "Weather.csv"


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table("weather-south-korea")

def trigger_weather_info(event , context ):
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
                            'CODE': record[1],
                            'PROVINCE': record[2],
                            'DATE': record[3],
                            'AVG_TEMP': record[4],
                            'MIN_TEMP': record[5],
                            'MAX_TEMP': record[6],
                            'PRECIPITATION': record[7],
                            'MAX_WIND_SPEED': record[8],
                            'MOST_WIND_DIRECTION': record[9],
                            'AVG_RELATIVE_HUMIDITY': record[10]
                            }
                        )
    except :
        missed_records += 1
   