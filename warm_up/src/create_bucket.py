import boto3
s3 = boto3.client('s3')


def create_bucket(bucket_name='default_bucket'):
    s3.create_bucket(Bucket=bucket_name)
