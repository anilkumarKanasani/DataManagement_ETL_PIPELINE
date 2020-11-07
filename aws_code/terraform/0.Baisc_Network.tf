# AWS crenditials will be fetched from Windows Environment variables.
# https://stackoverflow.com/questions/55052153/how-to-configure-environment-variables-in-hashicorp-terraform#:~:text=You%20can%20provide%20your%20credentials,and%20AWS%20Secret%20Key%2C%20respectively.&text=In%20the%20more%20general%20case,that%20are%20prefixed%20with%20TF_VAR_%20.

provider "aws" {
    region = "eu-central-1"
}

#############################################################################################################################

# Creating VPC and SUBNET resources using vpc module in tf_Module Folder.
module "ETL_VPC" {
    source = "./tf_Resources/vpc"

    # Even though we have default value, we can supply new CIDR_block IP address
    # Default is 10.0.0.0/16
    vpc_cidr_block = "192.168.0.0/16"

    # Default is dedicated
    vpc_tenancy = "default"

    # No default Values
    vpc_id = module.ETL_VPC.vpc_id

    # Default value is 10.0.1.0/24
    subnet_cidr_block = "192.168.1.0/24"
}