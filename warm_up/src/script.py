import boto3

s3 = boto3.client('s3')

BUCKET = 'warm-up-bucket-cl'

s3.create_bucket(Bucket=BUCKET)
