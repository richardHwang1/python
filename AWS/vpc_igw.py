import boto3

ec2 = boto3.client('ec2')
elbv2 = boto3.client('elbv2')
autoscaling = boto3.client('autoscaling')

# VPC & IGW
vpc = ec2.create_vpc(
    CidrBlock='10.0.0.0/16',
)
vpc_id = vpc['Vpc']['VpcId']

igw = ec2.create_internet_gateway()
igw_id = igw['InternetGateway']['InternetGatewayId']

attach_igw = ec2.attach_internet_gateway(
    InternetGatewayId=igw_id,
    VpcId=vpc_id,
)

# Public Subnet & Route Table