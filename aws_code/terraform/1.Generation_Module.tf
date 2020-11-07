
# Creating S3 Bucket for Dumping CSV Data from different Data Sources

variable "list_of_buckets" {
default = ["dumped-hospital-record-cases" , 
                "dumped-patient-info" , 
                "dumped-region-south-korea", 
                "dumped-search-trend-south-korea",
                "dumped-time-reported" , 
                "dumped-time-age" , 
                "dumped-time-gender" , 
                "dumped-time-provience" , 
                "dumped-weather-south-korea",
                "schemaless-records"
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

