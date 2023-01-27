import boto3

# Create a session
session = boto3.session.Session()

# Create a client
elb_client = session.client('elb')
ec2 = boto3.client('ec2')

# Get all security groups
groups = ec2.describe_security_groups()

print('')
print('Security group without instances attached')
print('=========================================')

# Iterate over each security group
for group in groups['SecurityGroups']:
    # Get all instances using the security group
    instances = ec2.describe_instances(Filters=[
        {'Name': 'instance.group-id', 'Values': [group['GroupId']]}
    ])

    # If no instances are using the security group, print the group ID
    if not instances['Reservations']:
        print(group['GroupId'], 'has not instances associated.')
