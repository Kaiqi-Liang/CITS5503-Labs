import boto3
import iso639
client = boto3.client('comprehend')

while True:
	text = input()
	print()

	response = client.detect_dominant_language(Text=text)['Languages'][0]
	code = response['LanguageCode']
	language = iso639.languages.get(part1 = code).name
	confidence = round(response['Score'] * 100)
	print(f'{language} detected with {confidence}% confidence', end='\n\n')

	response = client.detect_sentiment(Text=text, LanguageCode=code)
	sentiment = response['Sentiment'].capitalize()
	confidence = round(response['SentimentScore'][sentiment] * 100)
	print(f'{sentiment} detected with {confidence}% confidence', end='\n\n')

	response = client.detect_entities(Text=text, LanguageCode=code)['Entities']
	print([f"{entity['Type']}: {entity['Text']}" for entity in response], end='\n\n')

	response = client.detect_key_phrases(Text=text, LanguageCode=code)['KeyPhrases']
	print([keyphrase['Text'] for keyphrase in response], end='\n\n')

	response = client.detect_syntax(Text=text, LanguageCode=code)['SyntaxTokens']
	print([syntax['Text'] for syntax in response], end='\n\n')
