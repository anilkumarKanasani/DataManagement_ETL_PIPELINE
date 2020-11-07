
# Defining all resource specifications for s3 instances module


resource "aws_s3_bucket" "ETL_bucket" {
  bucket = var.bucket_name
  acl    = "private"
  force_destroy = true

  tags = {
    Name        = var.bucket_tag
    Environment = "DM_ETL_Project"
  }
}