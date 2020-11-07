
# Defining Input Variables for Lambda Function instances module


variable "python_file_name" {
    type = string
    description = "The python script file to be exec in lambda"
}


variable "zip_file_location" {
    type = string
    description = "The location where the zip file of python file is saved to be use in lambda function execution"
}


variable "function_name" {
    type = string
    description = "The Function Name to be reflect in AWS lambda console"
}

variable "handler" {
    type = string
    description = "The python function to be exec in lambda"
}