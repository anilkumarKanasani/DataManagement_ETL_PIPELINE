
/*
# Creating VPC and SUBNET resources using vpc module in tf_Module Folder.
module "ETL_machine" {
    source = "./tf_Resources/ec2"

    # No Default Value
    ec2_count = 1

    # No Default value
    # ami IDs are specific to region.. Please check that
    ec2_ami_id = "ami-00a205cb8e06c3c4e"

    # Default is t2.micro
    ec2_instance_type = "t2.micro"

    # No Default value
    ec2_subnet_id = module.ETL_VPC.subnet_id
}
*/