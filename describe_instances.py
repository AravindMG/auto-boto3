import boto3

client = boto3.client('ec2')
resp = client.describe_instances(Filters=[{
    'Name': 'tag:env',
    'Values': ['prod']
}])

# describe instances has a nested lists so we are using nested for loop to fetch the instance id
for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'])