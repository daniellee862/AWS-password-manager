import boto3
s3 = boto3.client('s3')


def delete_files(bucket_name, file_name):
    files_to_delete = [{'Key': file} for file in file_name]
    s3.delete_objects(Bucket=bucket_name, Delete={'Objects': files_to_delete})


#s3.delete_objects(Bucket=bucket_name, Delete={'Objects': [{'Key': 'northcoders.txt'},{'Key': 'methods.txt'}]})
