
import boto3

glue_client = boto3.client('glue', region_name='eu-central-1')

try:
    response = glue_client.start_crawler( Name = "transformed_data_crawler" )
    print('TRANSFORMED Catalog table is created in Glue Database named "transformed-data".. SCANNING INPROGRESS  Please wait for some time to get the catalog tables')
except:
    response = glue_client.update_crawler( Name = "transformed_data_crawler" )
    print("transformed-data - Catalog tables are updating.. SCANNING INPROGRESS  Please wait for some time to get latest catalog tables")



