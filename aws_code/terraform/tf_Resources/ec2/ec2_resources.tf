
# Defining all resource specifications for ec2 instances module

# ec2 instacne resource
resource "aws_instance" "ETL_machine" {
    count           =   "${var.ec2_count}"
    ami             =   "${var.ec2_ami_id}"
    instance_type   =   "${var.ec2_instance_type}"
    subnet_id       =   "${var.ec2_subnet_id}"
    force_destroy = true

  tags = {
    Name = "ETL_ec2_machine"
    Environment = "DM_ETL_Project"
  }
}