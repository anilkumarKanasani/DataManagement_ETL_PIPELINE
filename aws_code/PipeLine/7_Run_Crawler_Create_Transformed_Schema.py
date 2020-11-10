
import boto3

glue_client = boto3.client('glue', region_name='eu-central-1')


list_of_transformed_crawlers =["tranformed-data-crawler-hospital-record-cases" , 
                "tranformed-data-crawler-patient-info" , 
                "tranformed-data-crawler--region-south-korea", 
                "tranformed-data-crawler-search-trend-south-korea",
                "tranformed-data-crawler-time-reported" , 
                "tranformed-data-crawler-time-age" , 
                "tranformed-data-crawler-time-gender" , 
                "tranformed-data-crawler-time-provience" , 
                "tranformed-data-crawler-weather-south-korea",
                ]


for crawler in list_of_transformed_crawlers:
    try:
        response = glue_client.start_crawler( Name = crawler )
        print(crawler + ' Catalog table is created in Glue Database named "transformed-data".. SCANNING INPROGRESS Please wait for some time to get the catalog tables')
    except:
        response = glue_client.update_crawler( Name = crawler)
        print(crawler + ' Catalog tables are updating..SCANNING INPROGRESS  Please wait for some time to get latest catalog tables')
    print('----------------------------------------------------------------------------------------')
