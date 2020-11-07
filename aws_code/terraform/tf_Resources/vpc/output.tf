
# All the variables this VPC module can send to dev (or) prod (or) any other Envs.


output "vpc_id" {
    value = aws_vpc.ETL_VPC.id
}

output "subnet_id" {
    value = aws_subnet.ETL_subnet.id
}