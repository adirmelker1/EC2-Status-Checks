import boto3
ec2 = boto3.client('ec2', region_name='eu-north-1')
statuses = ec2.describe_instance_status()
for status in statuses['InstanceStatuses']:
    ins_status=status['InstanceStatus']['Status']
    sys_status=status['SystemStatus']['Status']
    state = status['InstanceState']['Name']
    InstanceId = status['InstanceId']
    print(f"Instance {InstanceId} State: {state}, Instance Status: {ins_status}, System Status: {sys_status}")

