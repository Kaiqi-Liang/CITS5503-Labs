# Practical Worksheet 1

## AWS Accounts and Log In

### Search and open Identity Access Management

![IAM](images/iam.png)

## Virtual Box and Ubuntu VM

### Download and install the appropriate version of VirtualBox

![virtualbox](images/virtualbox.png)

### Download Ubuntu 20.04 LTS iso

![iso](images/iso.png)

### Setup VM

![ubuntu](images/ubuntu.png)

## AWSCLI, Boto and Python 3.8.x

### Install Python 3.8.x

![python version](images/python.png)

### Install awscli

![awscli](images/awscli.png)

### Install boto3

![boto3](images/boto3.png)

## Exploring and testing the environment

### Test the aws environment by running

![table](images/table.png)

### Test the python environment

![un-tabulated response](images/untabulated.png)

### Put this code into a python file and tabulate the print to have 2 columns with Endpoint and RegionName

```python
'''lab1.py'''
import boto3
import pandas

ec2 = boto3.client('ec2')
response = ec2.describe_regions()
df = pandas.DataFrame(response['Regions'])
print(df.drop('OptInStatus', axis=1).to_string(index=False))
```

Running `lab1.py`.

![tabulated response](images/tabulated.png)
