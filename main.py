import boto3
ec2 = boto3.client('ec2', region_name='eu-north-1')

reservations = ec2.describe_instances()
for reservation in reservations['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance State {instance['InstanceId']}: {instance['State']['Name']}")