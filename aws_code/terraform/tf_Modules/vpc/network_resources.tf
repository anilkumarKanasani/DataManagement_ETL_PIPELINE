

# The only one Private network in our project
resource "aws_vpc" "ETL_VPC" {
  cidr_block       = "${var.vpc_cidr_block}"
  instance_tenancy = "${var.vpc_tenancy}"

  tags = {
    Name = "ETL_VPC"
  }
}


# First subnet in out project
resource "aws_subnet" "ETL_subnet" {
  vpc_id     = "${var.vpc_id}"
  cidr_block = "${var.subnet_cidr_block}"
  availability_zone = "eu-central-1a"

  tags = {
    Name = "ETL_subnet"
  }
}