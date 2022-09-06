import boto3
import pandas

ec2 = boto3.client('ec2')
response = ec2.describe_regions()
df = pandas.DataFrame(response['Regions'])
print(df.drop('OptInStatus', axis=1).to_string(index=False))
