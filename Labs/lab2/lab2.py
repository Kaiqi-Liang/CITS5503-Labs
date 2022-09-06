import boto3

client = boto3.client('ec2')
ec2 = boto3.resource('ec2')

# create a security group given the group name and description
security_group_id = client.create_security_group(
    GroupName='23344153-sg',
    Description='Security Group'
)['GroupId']

# print out security group ID and Vpc ID
vpc_id = client.describe_vpcs().get('Vpcs', [{}])[0].get('VpcId', '')
print(f'Security Group Created {security_group_id} in vpc {vpc_id}.', end='\n\n')

# add inbound rule for the given security group ID
data = client.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[{
        'IpProtocol': 'tcp',
        'FromPort': 22,
        'ToPort': 22,
        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
    }]
)
print(f'Ingress Successfully Set {data}', end='\n\n')

# create key pair given a key name
keyname = '23344153-key'
print(client.create_key_pair(KeyName=keyname), end='\n\n')

# create an ec2 instance given ami, the number of instances, type, key and security group
instance = ec2.create_instances(
    ImageId='ami-d38a4ab1',
    MaxCount=1,
    MinCount=1,
    InstanceType='t2.micro',
    KeyName=keyname,
    SecurityGroupIds=[security_group_id]
)[0]
print(instance.id, end='\n\n')

# wait for the instance to launch
instance.wait_until_running()
response = client.describe_instances(InstanceIds=[instance.id])

# once its running print out the public IP address
print(response['Reservations'][0]['Instances'][0]['PublicIpAddress'])
