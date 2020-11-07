
# Creating S3 Bucket for Dumping CSV Data from different Data Sources

variable "list_of_buckets" {
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

module "ETL_bucket" {
    source = "./tf_Resources/s3"

    # No Default Value
    bucket_name = element(var.list_of_buckets, count.index)
    count      = length(var.list_of_buckets)
    # No Default value
    bucket_tag = "dumped-data-lake" 
}

