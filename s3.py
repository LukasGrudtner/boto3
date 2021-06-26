import os
import boto3
import dotenv

dotenv.load_dotenv()

ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
REGION_NAME = os.getenv('REGION_NAME')
BUCKET = os.getenv('BUCKET')
PREFIX = os.getenv('PREFIX')

s3 = boto3.client(
    service_name='s3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name=REGION_NAME
)

paginator = s3.get_paginator('list_objects')
parameters = {
    'Bucket': BUCKET,
    'Prefix': PREFIX
}

page_iterator = paginator.paginate(**parameters)

for page in page_iterator:
    for object in page['Contents']:
        print(object['Key'])
