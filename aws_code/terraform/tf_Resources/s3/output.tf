
# All the variables this s3 module can send to dev (or) prod (or) any other Envs (or) Pipelines.

# Till now it is not used any where
output "bucket_arn" {
    value = aws_s3_bucket.ETL_bucket.arn
}