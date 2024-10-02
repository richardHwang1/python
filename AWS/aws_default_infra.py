import boto3

ec2 = boto3.client('ec2')

def create_vpc():
    vpc = ec2.create_vpc(CidrBlock='172.16.0.0/16')
    return vpc['Vpc']['VpcId']

def create_igw():
    igw = ec2.create_internet_gateway()