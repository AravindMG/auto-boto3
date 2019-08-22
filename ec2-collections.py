import boto3
ec2 = boto3.resource('ec2')
# for instance in ec2.instances.filter(Filters=[
#     {
#         'Name':'availability-zone',
#         'Values': ['us-west-2a']
#     }
# ]):
#     print(instance.instance_id, instance.instance_type)
# to stop the instances

ec2.instances.filter(Filters=[
    {
        'Name':'availability-zone',
        'Values': ['us-west-2a']
    }
]).stop()
