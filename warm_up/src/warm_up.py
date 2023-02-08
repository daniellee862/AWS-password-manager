import boto3
import json

s3 = boto3.client('s3')

BUCKET = 'warm-up-bucket-cl'

s3.create_bucket(Bucket=BUCKET)

s3_bucket_list = s3.list_buckets()
s3_bucket_list['Buckets'][0]['Name']

with open('northcoders.txt', 'rb') as file:
    s3.put_object(Body=file, Bucket=BUCKET, Key='northcoders.txt')

with open('methods.txt', 'rb') as file:
    s3.put_object(Body=file, Bucket=BUCKET, Key='methods.txt')

uploaded_files = s3.list_objects(Bucket=BUCKET)
# print(uploaded_files)

uploaded_file_names = uploaded_files['Contents']

file_list = []

for dictionary in uploaded_file_names:
    file_list.append(dictionary['Key'])

# print(file_list)

file_text = s3.get_object(Bucket=BUCKET, Key='northcoders.txt')['Body'].read()

# print(file_text.decode('utf-8'))

s3.delete_objects(Bucket=BUCKET, Delete={'Objects': [
    {'Key': 'northcoders.txt'},
    {'Key': 'methods.txt'}
]})

# print(s3.list_objects(Bucket=BUCKET))

s3.delete_bucket(Bucket=BUCKET)

print(s3.list_buckets()['Buckets'])

# def create_S3_Bucket(bucket_name):
#    BUCKET = bucket_name
#    s3.create_bucket(Bucket=BUCKET)
#    s3_bucket_list = s3.list_buckets()
#    return s3_bucket_list['Buckets'][0]['Name']


# [{'Name': 'warm-up-bucket-cl', 'CreationDate': datetime.datetime(2023, 2, 8, 14, 45, 33, tzinfo=tzutc())}]

# print(s3_bucket_list['Buckets'])
