
# Defining Input Variables for Lambda Function instances module


variable "python_file_name" {
    type = string
    description = "The python script file to be exec in lambda"
    default = "collection.py"
}


variable "zip_file_location" {
    type = string
    description = "The location where the zip file of python file is saved to be use in lambda function execution"
    default = "python_scripts_bundled/collection.zip"
}


variable "handler" {
    type = string
    description = "The python function to be exec in lambda"
    default = "collection.hello"
}