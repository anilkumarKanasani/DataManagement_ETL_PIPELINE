resource "aws_iam_role" "lambda_role" {
  name = "lambda_role"

  assume_role_policy = file("./tf_Resources/policies/lambda_assume_policy.json")

}


resource "aws_iam_role_policy" "lambda_policy" {
  name = "lambda_policy"
  role = aws_iam_role.lambda_role.id

  policy = file("./tf_Resources/policies/open_to_all_policy.json")
}