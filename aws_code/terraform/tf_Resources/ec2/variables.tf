
# Defining Input Variables for ec2 instances module

variable "ec2_count" { }


variable "ec2_ami_id" { }


variable "ec2_instance_type" {
    type = string
    description = "Instacne type of EC2 Machine"
    default = "t2.micro"
}

variable "ec2_subnet_id" { }



