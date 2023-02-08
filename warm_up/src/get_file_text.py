import boto3
s3 = boto3.client('s3')


def get_file_text(bucket_name, file_name):
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    file_text = response['Body'].read().decode('utf-8')
    return file_text
