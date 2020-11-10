


resource "aws_glue_catalog_database" "ETL_catalog_raw_database" {
  name = var.database_name
}


resource "aws_glue_crawler" "ETL_raw_crawler" {
  database_name = aws_glue_catalog_database.ETL_catalog_raw_database.name
  name          = var.crawler_name
  role          = var.role

dynamic "s3_target" {
    for_each = var.list_of_raw_s3_buckets

    content {
      path = s3_target.value
    }
  }
}

