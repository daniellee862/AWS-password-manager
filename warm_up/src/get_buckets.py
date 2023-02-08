import boto3
s3 = boto3.client('s3')


def get_buckets():
    s3_bucket_list = s3.list_buckets()
    # s3_bucket_list['Buckets'][0]['Name']
    return s3_bucket_list
