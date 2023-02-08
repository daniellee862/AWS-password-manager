# module imports
from create_bucket import create_bucket
from delete_files import delete_files
from get_buckets import get_buckets
from get_files import get_files
from get_file_text import get_file_text
from load_files import load_files
# libaries
import boto3
import json

import sys
print(sys.path)

s3 = boto3.client('s3')

# /home/daniel/Desktop/northcoders/data-engineering/week4-integration/#de-password-manager-two/warm_up/src/utils/create_bucket.py

b = 'daniels-bucket-northcoders'
f1 = '../data/northcoders.txt'
f2 = '../data/methods.txt'

# create bucket - takes bucket_name
create_bucket(b)
# list buckets
print(get_buckets())
# load_files - takes file_name and bucket_name
load_files(f1, b, 'northcoders.txt')
load_files(f2, b, 'methods.txt')
# print list of file names
print(get_files(b))
# print file text
print(get_file_text(b, 'northcoders.txt'))
# delete files - takes bucket name and list of files to delete
delete_files(b, ['methods.txt', 'northcoders.txt'])


# check files are deleted
print(s3.list_objects(Bucket=b))
# delete bucket
s3.delete_bucket(Bucket=b)
# list buckets
print(s3.list_buckets()['Buckets'])


# RESPONSE OBJECT
#    s3.create_bucket(Bucket=BUCKET)
#    s3_bucket_list = s3.list_buckets()
#    return s3_bucket_list['Buckets'][0]['Name']
# [{'Name': 'warm-up-bucket-cl', 'CreationDate': datetime.datetime(2023, 2, 8, 14, 45, 33, tzinfo=tzutc())}]
# print(s3_bucket_list['Buckets'])
