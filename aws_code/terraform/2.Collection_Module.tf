


module "ETL_lambda" {
    source = "./tf_Resources/Lambda"
    count      = length(var.list_of_python_file_name)
    python_file_name = element(var.list_of_python_file_name, count.index)
    role = module.ETL_Lambda_role.lambda_arn
    zip_file_location = element(var.list_of_zip_file_location, count.index)
    function_name = element(var.list_of_functionNames, count.index)
    handler = element(var.list_of_handlers, count.index)

}
