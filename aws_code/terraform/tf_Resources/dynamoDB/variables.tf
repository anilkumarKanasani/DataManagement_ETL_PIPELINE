
# Defining Input Variables for dynamoDB instances module

# No Default Value
variable "nosql_table_name" { 
    type = string
    description = "Name to give to the created DynamDB Table"
}


# There is No Default Value
variable "primary_key_name" {
    type = string
    description = "The attribute of record with which it can be reconize"
}



variable "primary_key_type" {
    type = string
    description = "The type of primary Key"
    default = "S"

}
