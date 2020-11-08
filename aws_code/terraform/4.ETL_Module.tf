
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


# Creating Crawlers to create metadata catalog's from dynamoDB Tables
module "ETL_crawler" {
    source = "./tf_Resources/glue_crawler"

    role = module.ETL_glue_role.glue_arn
    crawler_name = "create_ds4c_meta_data"
    database_name = "ds4c_metadata"
    list_of_dynamo_table_names = var.list_of_tables
    
    
}