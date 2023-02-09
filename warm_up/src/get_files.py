import boto3
s3 = boto3.client('s3')


def get_files(bucket_name):
    # try:
    #    response = s3.list_objects(Bucket=bucket_name)
    # except ClientError as c:
    #    raise c

    response = s3.list_objects(Bucket=bucket_name)

    uploaded_files = response['Contents']
    file_name_list = []

    for file in uploaded_files:
        file_name_list.append(file['Key'])

    return file_name_list
