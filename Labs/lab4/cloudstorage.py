'''
Skeleton application to copy local files to S3

Given a root local directory, will return files in each level and
copy to same path on S3
'''
import os
import sys
import boto3
import base64
from lab4 import ROOT_S3_DIR, key, encrypt_file

client = boto3.client('s3')
s3 = boto3.resource('s3')

# create bucket if not there
argv = sys.argv[1:]
if len(argv) > 0 and '-i' in argv:
    try:
        response = client.create_bucket(
            Bucket=ROOT_S3_DIR,
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-southeast-2'
            },
        )
        print(response)
    except Exception as error:
        print(error)

def upload_file(file):
    out_filename = f'{file}.enc'
    if '-k' in argv:
        # KMS
        from kms import data_key, data_key_encrypted
        encrypt_file(data_key, file)
        client.put_object(
            Body=open(out_filename, 'rb'),
            Bucket=ROOT_S3_DIR,
            # enable SSE-KMS
            ServerSideEncryption='aws:kms',
            Key=file,
            # put encrypted data key in the metadata so the data key can
            # be obtained by decrypting the encrypted data key
            Metadata={
                'encryption-key': base64.b64encode(data_key_encrypted).decode()
            }
        )
        print("Uploading %s" % out_filename)
    elif '-c' in argv:
        # using a hash key to encrypt
        encrypt_file(key, file)
        s3.meta.client.upload_file(out_filename, ROOT_S3_DIR, file)
        print("Uploading %s" % out_filename)
    else:
        # upload files unencrypted
        s3.meta.client.upload_file(file, ROOT_S3_DIR, file)
        print("Uploading %s" % file)

# parse the current directory and upload all the text files
for dir_name, subdir_list, file_list in os.walk('.', topdown=True):
    for fname in file_list:
        # only upload files with a txt extension
        if fname.endswith('.txt'):
            upload_file(f'{dir_name}/{fname}')

print("done")
