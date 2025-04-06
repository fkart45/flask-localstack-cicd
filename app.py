from flask import Flask
import boto3 #Part 2
import json #Part 2

app = Flask(__name__)

@app.route('/')
def hello():
    lambda_client = boto3.client( #Part 2
        'lambda', #Part 2
        endpoint_url='http://localhost:4566', #Part 2
        aws_access_key_id='test', #Part 2
        aws_secret_access_key='test', #Part 2
        region_name='us-east-1'
    )
    response = lambda_client.invoke(
        FunctionName='my_lambda_function', #Part 2
        InvocationType='RequestResponse' #Part 2
    )
    result = json.loads(response['Payload'].read().decode('utf-8')) #Part 2

    return f"Hello, World - I am app build using Flask library! Lambda response: {result['body']}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)