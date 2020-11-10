


resource "aws_glue_catalog_database" "ETL_catalog_raw_database" {
  name = var.database_name
}


resource "aws_glue_crawler" "ETL_raw_crawler" {
  database_name = aws_glue_catalog_database.ETL_catalog_raw_database.name
  name          = var.crawler_name
  role          = var.role
  s3_target  = var.raw_s3_bucket
}
