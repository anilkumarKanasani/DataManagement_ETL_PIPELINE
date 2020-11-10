


resource "aws_glue_catalog_database" "ETL_transformed_catalog_database" {
  name = var.database_name
}


resource "aws_glue_crawler" "ETL_transform_crawler" {
  database_name = aws_glue_catalog_database.ETL_transformed_catalog_database.name
  name          = var.crawler_name
  role          = var.role

dynamic "s3_target" {
    for_each = var.list_of_tranformed_s3_buckets

    content {
      path = s3_target.value
    }
  }
}

