tableName=CloudFiles
aws dynamodb delete-table --table-name $tableName --endpoint-url http://localhost:8000 > /dev/null
aws dynamodb create-table --cli-input-json file://create_table.json --endpoint-url=http://localhost:8000 > /dev/null
aws dynamodb list-tables --endpoint-url http://localhost:8000
aws dynamodb scan --table-name $tableName --endpoint-url=http://localhost:8000
for output in `aws s3 ls --recursive 23344153-cloudstorage`
do
	if echo $output | grep '/' > /dev/null
	then
		path=$output
		filename=`echo $output | sed -E 's/[a-z]+\/+//g'`
		output=`aws s3api get-object-acl --bucket 23344153-cloudstorage --key $output`
		owner=`echo $output | egrep -o '"Owner": { "DisplayName": "[a-z.]+"' | cut -d ' ' -f4`
		permission=`echo $output | egrep -o '"Permission": "[A-Z_]+"' | cut -d' ' -f2`
		echo $path
		echo $filename
		echo $owner
		echo $permission
	elif echo $output | grep '-' > /dev/null
	then
		lastUpdated=$output
		echo $lastUpdated
	fi
	aws dynamodb put-item \
	    --table-name $tableName \
	    --item '{ \
	        "userId": {"S": "0"}, \
	        "filename": {"S": "'$filename'"}, \
	        "path": {"S": "'$path'"}, \
	        "lastUpdated": {"S": "'$lastUpdated'"}, \
	        "owner": {"S": "'$owner'"}, \
	        "permissions": {"S": "'$permission'"} }' \
	    --return-consumed-capacity TOTAL --endpoint-url http://localhost:8000
done