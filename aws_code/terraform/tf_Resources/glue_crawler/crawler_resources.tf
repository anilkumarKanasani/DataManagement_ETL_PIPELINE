


resource "aws_glue_catalog_database" "ETL_catalog_database" {
  name = var.database_name
}


resource "aws_glue_crawler" "ETL_crawler" {
  database_name = aws_glue_catalog_database.ETL_catalog_database.name
  name          = var.crawler_name
  role          = var.role

  dynamodb_target {
    path = "hospital-record-cases"
  }
}

/*
resource "aws_glue_catalog_table" "example_catalog_table" {
  name          = "example_catalog_table"
  database_name = aws_glue_catalog_database.example_catalog_database.name
}
*/