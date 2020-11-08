

# Creating Crawlers to create metadata catalog's from dynamoDB Tables
module "ETL_crawler" {
    source = "./tf_Resources/glue_crawler"

    role = module.ETL_glue_role.glue_arn
    crawler_name = "create_ds4c_meta_data"
    database_name = "ds4c_metadata"
    list_of_dynamo_table_names = var.list_of_dynamo_tables
    
    
}


module "ETL_Redshift_cluster" {
    
    source = "./tf_Resources/redshift"
    cluster_identifier = "dm-2-etl-cluster"
    db_name = "dm-2-etl"

    db_username = "dm-2-etl"
    db_password = "12345678"

}