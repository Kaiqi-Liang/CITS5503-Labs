import boto3

ROOT_S3_DIR = '23344153-cloudstorage'
TABLE_NAME='CloudFiles'

dynamodb = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
s3 = boto3.client("s3")

if __name__ == '__main__':
    # create table if not exists
    try:
        dynamodb.create_table(
            TableName=TABLE_NAME,
            AttributeDefinitions=[
                {
                    'AttributeName': 'userId',
                    'AttributeType': 'S'
                },
            ],
            KeySchema=[
                {
                    'AttributeName': 'userId',
                    'KeyType': 'HASH',
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            },
        )
    except Exception as error:
        print(error)

    # scan table to find the number of items
    items = dynamodb.scan(TableName=TABLE_NAME)['Items']
    # set the userId to be 0 if there is no items otherwise the last item's userId
    userId = int(items[-1]['userId']['S']) if len(items) > 0 else 0

    for content in s3.list_objects(Bucket=ROOT_S3_DIR)['Contents']:
        # the userId key will be the last item's userId + 1
        userId += 1
        path = content['Key']
        filename = path.split('/')[-1]
        # get all the attributes from S3
        response = s3.get_object(
            Bucket=ROOT_S3_DIR,
            Key=path,
        )
        lastUpdated = response['LastModified']
        response = s3.get_object_acl(
            Bucket=ROOT_S3_DIR,
            Key=path,
        )
        owner = response['Owner']['DisplayName']
        permissions = [{ 'S': grant['Permission'] } for grant in response['Grants']]

        # put the file item in the table
        dynamodb.put_item(
            Item={
                'userId': {
                    'S': str(userId),
                },
                'fileName': {
                    'S': filename,
                },
                'path': {
                    'S': path,
                },
                'lastUpdated': {
                    'S': str(lastUpdated),
                },
                'owner': {
                    'S': owner,
                },
                'permissions': {
                    'L': permissions,
                },
            },
            ReturnConsumedCapacity='TOTAL',
            TableName=TABLE_NAME,
        )
