
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


