import boto3
s3_client = boto3.client('s3')

def my_handler(event, context):
    message = 'Hello' + event['first_name'] + event['last_name']
    return { 
        'message' : message
    }  