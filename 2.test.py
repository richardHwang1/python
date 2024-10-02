import boto3

client = boto3.client('iam')

response = client.create_user(
    UserName = 'test',
)

print(response)