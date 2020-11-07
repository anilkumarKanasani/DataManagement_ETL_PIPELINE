

module "ETL_lambda" {
    source = "./tf_Resources/Lambda"
    python_file_name = "../PipeLine/2_Lambda_triggering_scripts/collection_cases.py"
    zip_file_location = "python_scripts_bundled/collection_cases.zip"
    function_name = "collection_cases"
    handler = "collection_cases.trigger_hospital_record_cases"

}