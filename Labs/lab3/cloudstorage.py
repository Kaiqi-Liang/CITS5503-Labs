'''
Skeleton application to copy local files to S3

Given a root local directory, will return files in each level and
copy to same path on S3
'''
import os
import sys
import boto3
from lab3 import ROOT_S3_DIR

s3 = boto3.resource("s3")
bucket_config = {'LocationConstraint': 'ap-southeast-2'}

def upload_file(file):
    s3.meta.client.upload_file(file, ROOT_S3_DIR, file)
    print("Uploading %s" % file)

# create bucket if not there
argv = sys.argv[1:]
if len(argv) == 1 and argv[0] in ['-i', '--initialise=True']:
    try:
        response = boto3.client("s3").create_bucket(
            Bucket=ROOT_S3_DIR,
            CreateBucketConfiguration=bucket_config,
        )
        print(response)
    except Exception as error:
        print(error)

# parse directory and upload files
for dir_name, subdir_list, file_list in os.walk('rootdir', topdown=True):
    for fname in file_list:
        upload_file(f'{dir_name}/{fname}')

print("done")
