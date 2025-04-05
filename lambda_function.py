import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3', endpoint_url='http://localhost:4566')
    bucker_name ='my-local-bucket'
    s3.put_object(Bucket=bucket_name, Key='test.txt', Body='Hello from Lambda!')
    return {'statusCode': 200, 'body': 'File uploaded to S3'}
