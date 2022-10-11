import boto3
rekognition = boto3.client('rekognition')
s3 = boto3.resource("s3")

BUCKET = '23344153'
URBAN = 'images/urban.jpeg'
BEACH = 'images/beach.jpeg'
PEOPLE = 'images/people.jpeg'
TEXT = 'images/text.jpeg'

try:
	s3.create_bucket(
		Bucket=BUCKET,
		CreateBucketConfiguration={'LocationConstraint': 'ap-southeast-2'},
	)

	for image in [URBAN, BEACH, PEOPLE, TEXT]:
		s3.meta.client.upload_file(image, BUCKET, image)
except:
	pass

response = rekognition.detect_labels(
	Image={
		'S3Object': {
			'Bucket': BUCKET,
			'Name': URBAN,
		}
	}
)['Labels']
print([
	{
		'Label': label['Name'],
		'Confidence': f"{round(label['Confidence'])}%"
	}
	for label in response], end='\n\n'
)

response = rekognition.detect_moderation_labels(
	Image={
		'S3Object': {
			'Bucket': BUCKET,
			'Name': BEACH,
		}
	}
)['ModerationLabels']
print([label['Name'] for label in response], end='\n\n')

response = rekognition.detect_faces(
	Image={
		'S3Object': {
			'Bucket': BUCKET,
			'Name': PEOPLE,
		}
	},
	Attributes=['ALL']
)['FaceDetails']
print([
	{
		'Gender': detail['Gender']['Value'],
		'AgeRange': ' ~ '.join(map(str, detail['AgeRange'].values())),
	}
	for detail in response], end='\n\n'
)

response = rekognition.detect_text(
	Image={
		'S3Object': {
			'Bucket': BUCKET,
			'Name': TEXT,
		}
	}
)['TextDetections']
print([text['DetectedText'] for text in response])
