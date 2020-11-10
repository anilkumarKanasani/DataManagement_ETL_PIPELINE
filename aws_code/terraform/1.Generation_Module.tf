
# Creating S3 Bucket for Dumping CSV Data from different Data Sources


module "ETL_raw_bucket" {
    source = "./tf_Resources/raw_s3"

    # No Default Value
    bucket_name = element(var.list_of_buckets, count.index)
    count      = length(var.list_of_buckets)
    # No Default value
    bucket_tag = "dumped-data-lake" 
}

