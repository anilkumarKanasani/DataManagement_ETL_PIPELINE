


# Creating Crawlers to create metadata catalog's from dynamoDB Tables
module "ETL_crawler" {
    source = "./tf_Resources/glue_crawler"

    role = module.ETL_glue_role.glue_arn
    crawler_name = "Create_ds4c_meta_data"
    database_name = "DS4C_METADATA"
    
    
}