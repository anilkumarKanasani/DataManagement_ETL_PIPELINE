


# Creating Crawlers to create metadata catalog's from dynamoDB Tables
module "ETL_crawler" {
    source = "./tf_Resources/glue_crawler"

    role = module.ETL_glue_role.glue_arn
    crawler_name = "create_ds4c_meta_data"
    database_name = "ds4c_metadata"
    
    
}