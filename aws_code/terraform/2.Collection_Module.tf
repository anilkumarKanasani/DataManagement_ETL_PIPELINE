

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

default = [".python_scripts_bundled/collecting_cases.zip",
            ".python_scripts_bundled/collecting_patient_info.zip", 
            ".python_scripts_bundled/collecting_region_info.zip",
            ".python_scripts_bundled/collecting_searchtrend_info.zip", 
            ".python_scripts_bundled/collecting_time.zip", 
            ".python_scripts_bundled/collecting_time_age.zip",
            ".python_scripts_bundled/collecting_time_gender.zip", 
            ".python_scripts_bundled/collecting_time_provience.zip", 
            ".python_scripts_bundled/collecting_weather_info.zip", 
            ".python_scripts_bundled/collecting_schemeless_info.zip"
    
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
module "ETL_lambda" {
    source = "./tf_Resources/Lambda"
    count      = length(var.list_of_python_file_name)
    python_file_name = element(var.list_of_python_file_name, count.index)
    role = module.ETL_Lambda_role.lambda_arn
    zip_file_location = element(var.list_of_zip_file_location, count.index)
    function_name = element(var.list_of_functionNames, count.index)
    handler = element(var.list_of_handlers, count.index)

}
