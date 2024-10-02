import boto3

client = boto3.resource('ec2')

vpc = client.create_vpc(CidrBlock = '10.0.0.0/16')

vpc.create_tags(Tags=[{"Key":"Name","Value":"My-VPC"}])
vpc.wait_until_available()

igw = client.create_internet_gateway()

vpc.attach_internet_gateway(InternetGatewayId=igw.id)

vpc.create_subnet(CidrBlock='10.0.1.0/24')