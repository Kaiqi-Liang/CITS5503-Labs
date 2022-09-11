import boto3

ec2 = boto3.client('ec2')
elb = boto3.client('elbv2')

# get the availability zones from the region and get the first two
availability_zones = sorted(
    [
        (
            availability_zone['SubnetId'],
            availability_zone['AvailabilityZone']
        )
        for availability_zone in ec2.describe_subnets()['Subnets']
    ], key=lambda availability_zone: availability_zone[1]
)[:2]

# create security group for the instances and load balancer
security_group_id = ec2.create_security_group(
    GroupName='23344153-sg',
    Description='Security Group'
)['GroupId']
print(security_group_id)

# add inbound rule for the given security group ID
data = ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        },
        {
            'IpProtocol': 'tcp',
            'FromPort': 80,
            'ToPort': 80,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }
    ]
)

# create two EC2 instances in two different availability zones of a specific region
instances = []
for _, availability_zone in availability_zones:
    instance = boto3.resource('ec2').create_instances(
        ImageId='ami-d38a4ab1',
        MaxCount=1,
        MinCount=1,
        InstanceType='t2.micro',
        KeyName='23344153-key',
        SecurityGroupIds=[security_group_id],
        Placement={
            'AvailabilityZone': availability_zone
        }
    )[0]
    instances.append(instance.id)
    instance.wait_until_running()
    print(ec2.describe_instances(InstanceIds=[instance.id])['Reservations'][0]['Instances'][0]['PublicIpAddress'])

# create the Application Load Balancer
load_balancer = elb.create_load_balancer(
    Name='23344153-lb',
    SecurityGroups=[security_group_id],
    Subnets=[subnet for subnet, _ in availability_zones]
)['LoadBalancers'][0]['LoadBalancerArn']
print(load_balancer)

# create a target group using the same VPC that was used to create the instances
target_group = elb.create_target_group(
    Name='23344153-tg',
    Protocol='HTTP',
    Port=80,
    VpcId=ec2.describe_vpcs()['Vpcs'][0]['VpcId']
)['TargetGroups'][0]['TargetGroupArn']
print(target_group)

# register targets in the target group
elb.register_targets(
    TargetGroupArn=target_group,
    Targets=[{ 'Id': instance } for instance in instances]
)

# create a listener with a default rule Protocol: HTTP and Port 80 forwarding on to the target group
elb.create_listener(
    LoadBalancerArn=load_balancer,
    DefaultActions=[
        {
            'TargetGroupArn': target_group,
            'Type': 'forward',
        },
    ],
    Protocol='HTTP',
    Port=80,
)
