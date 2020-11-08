resource "aws_iam_role" "glue_role" {
  name = "glue_role"

  assume_role_policy = file("./tf_Resources/glue_policies/glue_assume_policy.json")

}


resource "aws_iam_role_policy" "glue_admin_policy" {
  name = "glue_policy"
  role = aws_iam_role.glue_role.id

  policy = file("./tf_Resources/glue_policies/glue_open_to_all_policy.json")
}