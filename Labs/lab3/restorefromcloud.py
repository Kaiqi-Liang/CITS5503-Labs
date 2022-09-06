import os
import boto3
from lab3 import ROOT_S3_DIR

client = boto3.client("s3")
s3 = boto3.resource('s3')

for content in client.list_objects(Bucket=ROOT_S3_DIR)['Contents']:
    paths = content['Key'].split('/')
    # create the directories listed in the path
    for dir in paths[:-1]:
        if not os.path.isdir(dir):
            os.mkdir(dir)
        os.chdir(dir)
    # download the file from S3 to the deepest directory
    s3.meta.client.download_file(ROOT_S3_DIR, content['Key'], paths[-1])
    # go back to the root directory
    for i in range(len(paths) - 1):
        os.chdir('..')
