
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


variable "list_of_tranformed_s3_buckets" {
    type = list(string)
}

