import boto3
import schedule
import time

ec2 = boto3.client('ec2', region_name='eu-north-1')


def check_instance_status():
    statuses = ec2.describe_instance_status(IncludeAllInstances=True)
    for status in statuses['InstanceStatuses']:
        ins_status=status['InstanceStatus']['Status']
        sys_status=status['SystemStatus']['Status']
        state = status['InstanceState']['Name']
        InstanceId = status['InstanceId']
        print(f"Instance {InstanceId} State: {state}, Instance Status: {ins_status}, System Status: {sys_status}")
    print("####################################\n")
schedule.every(3).minutes.do(check_instance_status)

while True:
    schedule.run_pending()
    time.sleep(1)