
import boto3

glue_client = boto3.client('glue', region_name='eu-central-1')


list_of_raw_crawlers = ["raw-data-crawler-hospital-record-cases" , 
                "raw-data-crawler-patient-info" , 
                "raw-data-crawler-region-south-korea", 
                "raw-data-crawler-search-trend-south-korea",
                "raw-data-crawler-time-reported" , 
                "raw-data-crawler-time-age" , 
                "raw-data-crawler-time-gender" , 
                "raw-data-crawler-time-provience" , 
                "raw-data-crawler-weather-south-korea",
                ]
for crawler in list_of_raw_crawlers:
    try:
        response = glue_client.start_crawler( Name = crawler )
        print(crawler + ' Catalog table is created in Glue Database named "raw-data".. SCANNING INPROGRESS Please wait for some time to get the catalog tables')
    except:
        response = glue_client.update_crawler( Name = crawler)
        print(crawler + ' Catalog tables are updating..SCANNING INPROGRESS  Please wait for some time to get latest catalog tables")



