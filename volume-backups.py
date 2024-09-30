import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="us-east-2")

def create_volume_snapshots():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod']
            }
        ]
    )
    for volume in volumes['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )
        print(new_snapshot)
        
schedule.every(5).seconds.do(create_volume_snapshots)

while True:
    schedule.run_pending()
def create_volume_snapshots():
    """
    This function retrieves all AWS EC2 volumes with the 'prod' tag and creates a snapshot for each volume.
    The function uses the Boto3 library to interact with AWS services.

    Parameters:
    None

    Returns:
    None. However, it prints the details of each newly created snapshot.
    """
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod']
            }
        ]
    )
    for volume in volumes['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )
        print(new_snapshot)













