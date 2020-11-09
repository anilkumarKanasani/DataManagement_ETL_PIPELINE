


resource "aws_glue_catalog_database" "ETL_catalog_database" {
  name = var.database_name
}


resource "aws_glue_crawler" "ETL_crawler" {
  database_name = aws_glue_catalog_database.ETL_catalog_database.name
  name          = var.crawler_name
  role          = var.role

dynamic "dynamodb_target" {
    for_each = var.list_of_dynamo_table_names

    content {
      path = dynamodb_target.value
    }
  }
}
