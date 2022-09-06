'''kms.py'''
import boto3
client = boto3.client('kms')

with open('key_policy.json', 'r') as policy:
    # create a key with a KMS policy
    response = client.create_key(
        Policy=policy.read(),
    )
    key_id = response['KeyMetadata']['KeyId']
    key_region = response['KeyMetadata']['Arn']
    print(f'{key_id = }\n{key_region = }')

    # add an alias
    try:
        client.create_alias(
            AliasName='alias/23344153',
            TargetKeyId=key_id
        )
    except:
        pass

    # output the policy
    print(client.get_key_policy(
        KeyId=key_id,
        PolicyName='default'
    )['Policy'])

    # generate a data key for encryption
    data_key = client.generate_data_key(
        KeyId=key_id,
        KeySpec='AES_256'
    )
    data_key_encrypted = data_key['CiphertextBlob']
    data_key = data_key['Plaintext']
    print(f"{data_key_encrypted = }\n{data_key = }")
