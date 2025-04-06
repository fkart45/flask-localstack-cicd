import boto3

def lambda_handler(event, context):
    try:
        s3 = boto3.client(
        's3', 
        endpoint_url='http://localhost:4566', #Use this for local testing 'http://host.docker.internal:4566'
        aws_access_key_id='test',
        aws_secret_access_key='test',
        )
        bucket_name = 'my-local-bucket'
        s3.put_object(Bucket=bucket_name, Key='test.txt', Body='Hello from Lambda!')
        return {
        'statusCode': 200, 
        'body': 'File uploaded to S3 successfully'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
