
#########################################Variables for Generation Module#########################################
variable "list_of_buckets" {
default = ["dumped-hospital-record-cases" , 
                "dumped-patient-info" , 
                "dumped-region-south-korea", 
                "dumped-search-trend-south-korea",
                "dumped-time-reported" , 
                "dumped-time-age" , 
                "dumped-time-gender" , 
                "dumped-time-provience" , 
                "dumped-weather-south-korea",
                "raw-schemaless-records",
                "raw-rejected-records"
                ]

type = list(string)
}


######################################### Variables for Collection Module#########################################

variable "list_of_python_file_name" {

default = ["../PipeLine/2_Lambda_triggering_scripts/collecting_cases.py",
            "../PipeLine/2_Lambda_triggering_scripts/collecting_patient_info.py", 
            "../PipeLine/2_Lambda_triggering_scripts/collecting_region_info.py",
            "../PipeLine/2_Lambda_triggering_scripts/collecting_searchtrend_info.py", 
            "../PipeLine/2_Lambda_triggering_scripts/collecting_time.py", 
            "../PipeLine/2_Lambda_triggering_scripts/collecting_time_age.py",
            "../PipeLine/2_Lambda_triggering_scripts/collecting_time_gender.py", 
            "../PipeLine/2_Lambda_triggering_scripts/collecting_time_provience.py", 
            "../PipeLine/2_Lambda_triggering_scripts/collecting_weather_info.py", 
            "../PipeLine/2_Lambda_triggering_scripts/collecting_schemeless_info.py"
    
        ]

type = list(string)
}

variable "list_of_zip_file_location" {

default = [".lambda_python_scripts_bundled/collecting_cases.zip",
            ".lambda_python_scripts_bundled/collecting_patient_info.zip", 
            ".lambda_python_scripts_bundled/collecting_region_info.zip",
            ".lambda_python_scripts_bundled/collecting_searchtrend_info.zip", 
            ".lambda_python_scripts_bundled/collecting_time.zip", 
            ".lambda_python_scripts_bundled/collecting_time_age.zip",
            ".lambda_python_scripts_bundled/collecting_time_gender.zip", 
            ".lambda_python_scripts_bundled/collecting_time_provience.zip", 
            ".lambda_python_scripts_bundled/collecting_weather_info.zip", 
            ".lambda_python_scripts_bundled/collecting_schemeless_info.zip"
    
        ]

type = list(string)
}


variable "list_of_functionNames" {

default = ["collecting_cases",
            "collecting_patient_info", 
            "collecting_region_info",
            "collecting_searchtrend_info", 
            "collecting_time", 
            "collecting_time_age",
            "collecting_time_gender", 
            "collecting_time_provience", 
            "collecting_weather_info", 
            "collecting_schemeless_info"
    
        ]

type = list(string)
}


variable "list_of_handlers" {


default = ["collecting_cases.trigger_hospital_record_cases",
            "collecting_patient_info.trigger_patient_info", 
            "collecting_region_info.trigger_region_info",
            "collecting_searchtrend_info.trigger_searchtrend_info", 
            "collecting_time.trigger_time", 
            "collecting_time_age.trigger_time_age",
            "collecting_time_gender.trigger_time_gender", 
            "collecting_time_provience.trigger_time_provience", 
            "collecting_weather_info.trigger_weather_info", 
            "collecting_schemeless_info.trigger_schemeless_info"
    
        ]

type = list(string)
}



######################################### Variables for Storing Module#########################################

variable "list_of_dynamo_tables" {
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
                "CODE" ,
                "RECORD_ID" ,
                "RECORD_ID" ,
                "RECORD_ID" ,
                "RECORD_ID" ,
                "RECORD_ID" ,
                "RECORD_ID" 
                ]

type = list(string)
}


######################################### Variables for ETL Module #########################################


variable "list_of_tranformed_s3_buckets" {
default = ["tranformed-hospital-record-cases" , 
                "tranformed-patient-info" , 
                "tranformed-region-south-korea", 
                "tranformed-search-trend-south-korea",
                "tranformed-time-reported" , 
                "tranformed-time-age" , 
                "tranformed-time-gender" , 
                "tranformed-time-provience" , 
                "tranformed-weather-south-korea",
                ]

type = list(string)
}







variable "list_of_tranformed_s3_buckets_names" {
default = ["s3://tranformed-hospital-record-cases" , 
                "s3://tranformed-patient-info" , 
                "s3://tranformed-region-south-korea", 
                "s3://tranformed-search-trend-south-korea",
                "s3://tranformed-time-reported" , 
                "s3://tranformed-time-age" , 
                "s3://tranformed-time-gender" , 
                "s3://tranformed-time-provience" , 
                "s3://tranformed-weather-south-korea",
                ]

type = list(string)
}


variable "list_of_tranformed_crawlers" {
default = ["tranformed-data-crawler-hospital-record-cases" , 
                "tranformed-data-crawler-patient-info" , 
                "tranformed-data-crawler--region-south-korea", 
                "tranformed-data-crawler-search-trend-south-korea",
                "tranformed-data-crawler-time-reported" , 
                "tranformed-data-crawler-time-age" , 
                "tranformed-data-crawler-time-gender" , 
                "tranformed-data-crawler-time-provience" , 
                "tranformed-data-crawler-weather-south-korea",
                ]

type = list(string)
}


variable "list_of_raw_s3_buckets_names" {
default = ["s3://dumped-hospital-record-cases" , 
                "s3://dumped-patient-info" , 
                "s3://dumped-region-south-korea", 
                "s3://dumped-search-trend-south-korea",
                "s3://dumped-time-reported" , 
                "s3://dumped-time-age" , 
                "s3://dumped-time-gender" , 
                "s3://dumped-time-provience" , 
                "s3://dumped-weather-south-korea",
                ]

type = list(string)
}


variable "list_of_raw_crawlers" {
default = ["raw-data-crawler-hospital-record-cases" , 
                "raw-data-crawler-patient-info" , 
                "raw-data-crawler-region-south-korea", 
                "raw-data-crawler-search-trend-south-korea",
                "raw-data-crawler-time-reported" , 
                "raw-data-crawler-time-age" , 
                "raw-data-crawler-time-gender" , 
                "raw-data-crawler-time-provience" , 
                "raw-data-crawler-weather-south-korea",
                ]

type = list(string)
}




