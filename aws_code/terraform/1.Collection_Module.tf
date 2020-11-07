# AWS crenditials will be fetched from Windows Environment variables.
# https://stackoverflow.com/questions/55052153/how-to-configure-environment-variables-in-hashicorp-terraform#:~:text=You%20can%20provide%20your%20credentials,and%20AWS%20Secret%20Key%2C%20respectively.&text=In%20the%20more%20general%20case,that%20are%20prefixed%20with%20TF_VAR_%20.


#############################################################################################################################

# Creating S3 Bucket for Dumping CSV Data from different Data Sources
module "ETL_bucket" {
    source = "./tf_Resources/s3"

    # No Default Value
    bucket_name = "dumped-data-lake"

    # No Default value

    bucket_tag = "dumped-data-lake" 
    
}