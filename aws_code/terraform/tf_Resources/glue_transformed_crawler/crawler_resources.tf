


resource "aws_glue_catalog_database" "ETL_transformed_catalog_database" {
  name = var.database_name
}


resource "aws_glue_crawler" "ETL_S3_crawler" {
  database_name = aws_glue_catalog_database.ETL_transformed_catalog_database.name
  name          = var.crawler_name
  role          = var.role

  s3_target {
    path = var.s3_bucket_path
  }
}


