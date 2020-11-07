
# Defining Input Variables for VPC module


# https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing
variable "vpc_cidr_block" {
    type = string
    description = "Classless Inter-Domain Routing (CIDR) is a method for allocating IP addresses and for IP routing"
    default = "10.0.0.0/16"
}


# For more information about tenancy attribute and its different types .. visit https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html
variable "vpc_tenancy" {
    type = string
    description = "Each instance that you launch into a VPC has a tenancy attribute."
    default = "dedicated"
}


# VPC_ID need to be specify in subnet resource
# There is no default value to this attribute
# End user will specify in his request
variable "vpc_id" { }


# CIDR Block for Subnet
variable "subnet_cidr_block" {
    type = string
    description = "CIDR_Block for subnet"
    default = "10.0.1.0/24"
}