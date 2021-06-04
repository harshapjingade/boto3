import boto3
db = boto3.resource("dynamodb")
table = db.Table("employees")

response = table.delete_item(
    Key={
        "emp_id":"1"
    }
)

print(response)