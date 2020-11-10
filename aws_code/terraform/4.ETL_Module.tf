

# Creating Crawlers to create metadata catalog's from dynamoDB Tables
module "ETL_dynamo_crawler" {
    source = "./tf_Resources/glue_crawler"

    role = module.ETL_glue_role.glue_arn
    crawler_name = "raw_data_crawler"
    database_name = "RAW_DATA"
    list_of_dynamo_table_names = var.list_of_dynamo_tables
    
    
}

/*
module "ETL_Redshift_cluster" {
    source = "./tf_Resources/redshift"
    cluster_identifier = "dm-2-etl-cluster"
    db_name = "dm_2_etl_db"
    db_username = "dm"
    db_password = "Dm2$4444"

}

module "ETL_Glue_job_1" {
    source = "./tf_Resources/glue_jobs"
    glue_job_name = "Job_1"
    role = module.ETL_glue_role.glue_arn

}
*/


module "ETL_bucket" {
    source = "./tf_Resources/s3"

    # No Default Value
    bucket_name = "transformed-data"
    # No Default value
    bucket_tag = "transformed-data-lake" 
}


module "ETL_S3_crawler" {
    source = "./tf_Resources/glue_crawler"

    role = module.ETL_glue_role.glue_arn
    crawler_name = "transformed_data_crawler" 
    database_name = "TRANSFORMED_DATA"
    s3_bucket_path = module.ETL_bucket.arn

}

