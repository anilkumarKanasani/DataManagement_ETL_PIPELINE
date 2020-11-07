# AWS crenditials will be fetched from Windows Environment variables.
# https://stackoverflow.com/questions/55052153/how-to-configure-environment-variables-in-hashicorp-terraform#:~:text=You%20can%20provide%20your%20credentials,and%20AWS%20Secret%20Key%2C%20respectively.&text=In%20the%20more%20general%20case,that%20are%20prefixed%20with%20TF_VAR_%20.


#############################################################################################################################
variable "list_of_tables" {
default = ["hospital-record-cases" , 
                "patient-info" , 
                "region-south-korea", 
                "search-trend-south-korea",
                "time-reported" , 
                "time-age" , 
                "time-gender" , 
                "time-provience" , 
                "weather-south-korea"
                ]


type = list(string)
}


variable "Primary_Keys" {
default = ["CASE_ID" , 
                "PATIENT_ID" , 
                "PROVINCE_CODE",
                "RECORDED_DATE",
                "RECORDED_DATE" , 
                "RECORDED_DATE" , 
                "RECORDED_DATE" , 
                "RECORDED_DATE" , 
                "PROVINCE_CODE" 
                ]

type = list(string)
}
# Creating DynamoDB Tables for data injecting from dumped-data-lake S3 Bucket through lambda function
module "ETL_Nosql_table" {
    source = "./tf_Resources/dynamoDB"

    # No Default Value
    nosql_table_name = element(var.list_of_tables, count.index)

    # No Default value
    primary_key_name = element(var.Primary_Keys, count.index)

    # Default is "S"
    primary_key_type = "S"

    count      = length(var.list_of_tables)
    
}


