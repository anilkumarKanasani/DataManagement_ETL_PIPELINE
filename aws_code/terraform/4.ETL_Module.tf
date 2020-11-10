

# Creating Crawlers to create metadata catalog's from dynamoDB Tables
module "ETL_dynamo_crawler" {
    source = "./tf_Resources/glue_raw_crawler"

    role = module.ETL_glue_role.glue_arn
    crawler_name = "raw_data_crawler"
    database_name = "raw-data"
    list_of_dynamo_table_names = var.list_of_dynamo_tables
    
    
}

/*
I tried with redshift and glue jobs. Redshift needs private subnet and to communicate with redshift , crawler need 
security group. This is going into very big work. So, I stoped using redshift and saving transformed data in S3 Bucket.


module "ETL_Redshift_cluster" {
    source = "./tf_Resources/redshift"
    cluster_identifier = "dm-2-etl-cluster"
    db_name = "dm_2_etl_db"
    db_username = "dm"
    db_password = "Dm2$4444"

}

Glue Jobs are written in pyspark language. AWS is proving very good interface to develop automatic script.
But as of now, I am not very strong in understanding spark content. I cannt do big custom transformations.

Glue Jobs are charging few dollers. So, I shifted to local python pandas transformations.

module "ETL_Glue_job_1" {
    source = "./tf_Resources/glue_jobs"
    glue_job_name = "Job_1"
    role = module.ETL_glue_role.glue_arn

}
*/


# This bucket is for stroring transformed data coming from pandas transformations.
module "ETL_transformed_bucket" {
    source = "./tf_Resources/transformed_s3"

    # No Default Value
    bucket_name = "transformed-dm2-etl-data"
    # No Default value
    bucket_tag = "transformed-data-lake" 
}


# This is another crawler to get meta data of transformed data from new S3 bucket.
module "ETL_S3_crawler" {
    source = "./tf_Resources/glue_transformed_crawler"

    role = module.ETL_glue_role.glue_arn
    crawler_name = "transformed_data_crawler" 
    database_name = "transformed-data"
    s3_bucket_path = "s3://transformed-dm2-etl-data"

}
