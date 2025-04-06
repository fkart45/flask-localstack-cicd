provider "aws" {
    region = "us-east-1"
    access_key = "test"
    secret_key = "test"
    endpoints {
        s3 = "http://localhost:4566"
        lambda = "http://localhost:4566"
    }
    s3_use_path_style = true
    skip_credentials_validation = true
    skip_metadata_api_check = true
    skip_requesting_account_id = true
}

resource "aws_s3_bucket" "my_bucket" {
    bucket = "my-local-bucket"
}


resource "aws_lambda_function" "my_lambda" {
    filename = "lambda_function.zip"
    function_name = "my_lambda_function"
    role = "arn:aws:iam::000000000000:role/lambda-role"
    handler = "lambda_function.lambda_handler"
    runtime = "python3.9"
}