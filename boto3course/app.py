import boto3
from dotenv import load_dotenv
import os

load_dotenv()

Access_key_id = os.getenv('Access_key')
Secret_access_key = os.getenv('Secret_access_key')

# Connect to S3
s3 = boto3.resource(
    's3',
    aws_access_key_id=Access_key_id,
    aws_secret_access_key=Secret_access_key
)

# Display all existing buckets
for bucket in s3.buckets.all():
    print(bucket.name)

# Create a new bucket
#BUCKET_NAME = 'swarna-tute-2026-unique'

# s3.create_bucket(
#     Bucket=BUCKET_NAME
# )
#delete the bucket
#s3.Bucket(BUCKET_NAME).delete()
BUCKET_NAME='test-tute'
#read a file
s3.Bucket(BUCKET_NAME).download_file(
    'data.json',
    'test.txt'
)