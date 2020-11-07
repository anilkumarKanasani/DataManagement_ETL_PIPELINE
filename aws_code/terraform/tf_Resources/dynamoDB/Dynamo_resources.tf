
# Defining all resource specifications for dynamoDB instances module


resource "aws_dynamodb_table" "ETL_Nosql_table" {
  name           = "${var.nosql_table_name}"
  billing_mode   = "PAY_PER_REQUEST"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "${var.primary_key_name}"

  attribute {
    name = "${var.primary_key_name}"
    type = "${var.primary_key_type}"
  }

  tags = {
    Name        = "ETL_Dynamodb_Table"
    Environment = "DM_ETL_Project"
  }
}