import boto3

ec2 = boto3.client('ec2')

vpc = ec2.create_vpc(
    CidrBlock = '172.16.0.0/16',
    TagSpecifications = [
        {
            'ResourceType': 'vpc',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'python-vpc'
                },
            ]
        },
    ]
)

igw = ec2.create_internet_gateway(
    TagSpecifications = [
        {
            'ResourceType': 'internet-gateway',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'python-igw'
                },
            ]
        },
    ]
)

ec2.attach_internet_gateway(
    InternetGatewayId=igw['InternetGateway']['InternetGatewayId'],
    VpcId=vpc['Vpc']['VpcId'],
    )

pub_rt12 = ec2.create_route_table(
    VpcId=vpc['Vpc']['VpcId'],
    TagSpecifications = [
        {
            'ResourceType': 'route-table',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'python-pub-rt12'
                },
            ]
        },
    ]
)

pri_rt34 = ec2.create_route_table(
    VpcId=vpc['Vpc']['VpcId'],
    TagSpecifications = [
        {
            'ResourceType': 'route-table',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'python-pri-rt34'
                },
            ]
        },
    ]
)

pub_sn1 = ec2.create_subnet(
    VpcId=vpc['Vpc']['VpcId'],
    AvailabilityZone='ap-northeast-2a',
    CidrBlock='172.16.1.0/24',
    TagSpecifications = [
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'python-pub-sn1'
                },
            ]
        },
    ]
)

pub_sn2 = ec2.create_subnet(
    VpcId=vpc['Vpc']['VpcId'],
    AvailabilityZone='ap-northeast-2c',
    CidrBlock='172.16.2.0/24',
    TagSpecifications = [
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'python-pub-sn2'
                },
            ]
        },
    ]
)

pri_sn3 = ec2.create_subnet(
    VpcId=vpc['Vpc']['VpcId'],
    AvailabilityZone='ap-northeast-2a',
    CidrBlock='172.16.3.0/24',
    TagSpecifications = [
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'python-pri-sn3'
                },
            ]
        },
    ]
)

pri_sn4 = ec2.create_subnet(
    VpcId=vpc['Vpc']['VpcId'],
    AvailabilityZone='ap-northeast-2c',
    CidrBlock='172.16.4.0/24',
    TagSpecifications = [
        {
            'ResourceType': 'subnet',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'python-pri-sn4'
                },
            ]
        },
    ]
)

ec2.associate_route_table(
    RouteTableId=pub_rt12['RouteTable']['RouteTableId'],
    SubnetId=pub_sn1['Subnet']['SubnetId']
)

ec2.associate_route_table(
    RouteTableId=pub_rt12['RouteTable']['RouteTableId'],
    SubnetId=pub_sn2['Subnet']['SubnetId']
)

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=igw['InternetGateway']['InternetGatewayId'],
    RouteTableId=pub_rt12['RouteTable']['RouteTableId']
)

ec2.associate_route_table(
    RouteTableId=pri_rt34['RouteTable']['RouteTableId'],
    SubnetId=pri_sn3['Subnet']['SubnetId']
)

ec2.associate_route_table(
    RouteTableId=pri_rt34['RouteTable']['RouteTableId'],
    SubnetId=pri_sn4['Subnet']['SubnetId']
)

ec2.create_nat_gateway(
    AllocationId='',
    SubnetId=pub_sn1['Subnet']['SubnetId']
)