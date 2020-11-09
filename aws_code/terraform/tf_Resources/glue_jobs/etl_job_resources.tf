



resource "aws_glue_job" "ETL_glue_job" {
  name     = var.glue_job_name
  role_arn = var.role

  command {
    script_location = "s3://dm2-etl-glue-jobs/Job_1.py"
  }
}