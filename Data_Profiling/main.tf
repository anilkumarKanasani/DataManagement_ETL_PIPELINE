
    

# Creating S3 Bucket for Dumping CSV Data from different Data Sources
module "ETL_bucket" {
    source = "./tf_Modules/s3"

    # No Default Value
    bucket_name = "Dumped_Data"

    # No Default value

    bucket_tag = "Dumped_Data" 
    
}
    