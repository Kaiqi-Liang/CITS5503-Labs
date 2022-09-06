'''apply_policy.py'''
import boto3
from lab4 import ROOT_S3_DIR
client = boto3.client('s3')

with open('policy.json', 'r') as policy:
    client.put_bucket_policy(
        Bucket=ROOT_S3_DIR,
        Policy=policy.read(),
    )
    print(client.get_bucket_policy(Bucket=ROOT_S3_DIR)['Policy'])
