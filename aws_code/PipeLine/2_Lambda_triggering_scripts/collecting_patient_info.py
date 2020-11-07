
import boto3

s3_client = boto3.client("s3")
bucket_name = "dumped-patient-info"
file_name = "PatientInfo.csv"


dynamo_client = boto3.resource('dynamodb')
table = dynamo_client.Table("patient-info")

def trigger_patient_info(event , context ):
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
                Item = {'PATIENT_ID': record[0],
                        'SEX': record[1],
                        'AGE': record[2],
                        'COUNTRY': record[3],
                        'PROVINCE': record[4],
                        'CITY': record[5],
                        'INFECTION_CASE': record[6],
                        'INFECTED_BY': record[7],
                        'CONTACT_NUMBER': record[8],
                        'SYMPTOM_ONSET_DATE': record[9],
                        'CONFIRMED_DATE': record[10],
                        'RELEASED_DATE': record[11],
                        'DECEASED_DATE': record[12],
                        'STATE': record[13]}
                    )
    except :
        missed_records += 1