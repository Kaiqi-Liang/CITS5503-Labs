import os
import sys
import boto3
import base64
from lab4 import ROOT_S3_DIR, key, decrypt_file

client = boto3.client('s3')
s3 = boto3.resource('s3')
kms = boto3.client('kms')

argv = sys.argv[1:]
for content in client.list_objects(Bucket=ROOT_S3_DIR)['Contents']:
    paths = content['Key'].split('/')
    file = paths[-1]
    # create the directories listed in the path
    for dir in paths[:-1]:
        if not os.path.isdir(dir):
            os.mkdir(dir)
        os.chdir(dir)
    # download the file from S3 to the deepest directory
    s3.meta.client.download_file(ROOT_S3_DIR, content['Key'], file)

    if len(argv) == 1:
        # using KMS data key to decrypt
        if argv[0] in ['-k', '--kms=True']:
            key = client.get_object(
                Bucket=ROOT_S3_DIR,
                Key=content['Key']
            )['Metadata']['encryption-key']
            # decrypt the encrypted data key from the meta data first
            decrypt_file(
                kms.decrypt(CiphertextBlob=base64.b64decode(key))['Plaintext'],
                file
            )
        # using a hash key to decrypt
        elif argv[0] in ['-c', '--crypto=True']:
            decrypt_file(key, file)

    # go back to the root directory
    for i in range(len(paths) - 1):
        os.chdir('..')
