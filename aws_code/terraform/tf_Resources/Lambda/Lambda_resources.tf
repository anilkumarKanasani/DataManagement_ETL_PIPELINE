
# Defining all resource specifications for Lambda Function instances module

resource "aws_iam_role" "lambda_role" {
  name = "lambda_role"

  assume_role_policy = file("lambda_assume_policy.json")
}



resource "aws_iam_role_policy" "lambda_policy" {
  name = "lambda_policy"
  role = aws_iam_role.lambda_role.id

  policy = file("lambda_policy.json")
}


data "archive_file" "Collection" {
  type        = "zip"
  source_file = var.python_file_name
  output_path = var.zip_file_location
}


resource "aws_lambda_function" "test_lambda" {
  filename      = var.zip_file_location
  function_name = "collection"
  role          = aws_iam_role.lambda_role.arn
  handler       = var.handler


 # source_code_hash = filebase64sha256("lambda_function_payload.zip")

  runtime = "python3.7"
}