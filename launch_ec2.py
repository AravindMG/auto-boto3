import boto3
client = boto3.client('ec2')
resp = client.run_instances(ImageId='ami-0f2176987ee50226e',
                     InstanceType='t2.micro',
                     MinCount=1,
                     MaxCount=1)

for instance in resp['Instances']:
    print(instance['InstanceId'])
