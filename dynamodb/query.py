import boto3
from boto3.dynamodb.conditions import Key
db = boto3.resource("dynamodb")
table = db.Table("employees")
response = table.query(
    KeyConditionExpression=Key('emp_id').eq('0')
)

print(response["Items"])


