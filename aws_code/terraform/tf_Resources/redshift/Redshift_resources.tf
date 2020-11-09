
# Defining all resource specifications for Redshift instances module


resource "aws_redshift_cluster" "ETL_Redshift_cluster" {
  cluster_identifier = var.cluster_identifier
  database_name      = var.db_name
  master_username    = var.db_username
  master_password    = var.db_password
  node_type          = "dc1.large"
  cluster_type       = "single-node"
  skip_final_snapshot = true
}


