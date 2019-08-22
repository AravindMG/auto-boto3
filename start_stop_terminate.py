import boto3
client = boto3.client('ec2')

# can pass multiple instances as comma separated

# code to start the ec2 instance
# client.start_instances(InstanceIds=['i-0a73483f6a699e134'])

# code to stop the ec2 instance
#  client.stop_instances(InstanceIds=['i-0a73483f6a699e134'])

# code to terminate the ec2 instance
resp = client.terminate_instances(InstanceIds=['i-09f13e5c63821bbcd'])

for instances in resp['TerminatingInstances']:
    print(instances['InstanceId'])