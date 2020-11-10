
# Defining Input Variables for Crawler &  its dependicies instances module


variable "role" {
    type = string
}


variable "crawler_name" {
    type = string
}




variable "database_name" {
    type = string
}

variable "list_of_dynamo_table_names" {
    type = list(string)
}

variable "s3_bucket_path" {
    type = list(string)
}


