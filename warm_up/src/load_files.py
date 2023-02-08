import boto3
s3 = boto3.client('s3')


def load_files(file_name, bucket_name, key_value):
    with open(file_name, 'rb') as file:
        s3.put_object(Body=file, Bucket=bucket_name, Key=key_value)
