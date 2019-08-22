import boto3

ec2 = boto3.resource('ec2')
sns_client = boto3.client('sns')

backup_filter = [
    {
        'Name': 'tag:Backup',
        'Values': ['yes']
    }
]

snapshot_ids = []

for instance in ec2.instances.filter(Filters=backup_filter):
    for vol in instance.volumes.all():
        snapshot = vol.create_snapshot(Description='Created by Boto3')
        snapshot_ids.append(snapshot.snapshot_id)

# publish method to send email

sns_client.publish(
    TopicArn='arn:aws:sns:us-west-2:550107863181:snapshots',
    Subject='EBS Snapshots',
    Message=str(snapshot_ids)
)

# to delete the snapshots use delete() based on certain conditions
