import boto3
from boto3.dynamodb.conditions import Key, Attr
db = boto3.resource("dynamodb")
table = db.Table("employees")
response = table.scan(
    FilterExpression=Attr('emp_id').gte('0')
)

for x in response["Items"]:
    print(x)