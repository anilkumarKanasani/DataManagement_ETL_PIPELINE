
# Defining all resource specifications for Lambda Function instances module



data "archive_file" "Collection" {
  type        = "zip"
  source_file = var.python_file_name
  output_path = var.zip_file_location
}


resource "aws_lambda_function" "ETL_lambda" {
  filename      = var.zip_file_location
  function_name = var.function_name
  role          = var.role
  handler       = var.handler


 # source_code_hash = filebase64sha256("lambda_function_payload.zip")

  runtime = "python3.7"
}