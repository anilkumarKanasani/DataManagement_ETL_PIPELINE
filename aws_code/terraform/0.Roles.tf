
module "ETL_Lambda_role" {
    source = "./tf_Resources/lambda_policies"
}


module "ETL_glue_role" {
    source = "./tf_Resources/glue_policies"
}
