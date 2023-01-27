import boto3

# Create a session
session = boto3.session.Session()

# Create a client
elb_client = session.client('elb')
ec2 = boto3.client('ec2')

# Get all regions
regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]
# Loop over each region
print('')
print('list of unattached EBS Volumes')
print('==============================')

for region in regions:
    # Switch to the current region
    ec2 = boto3.client('ec2', region_name=region)
    # Get all security groups
    groups = ec2.describe_security_groups()
    # Retrieve a list of all unattached EBS volumes
    volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
    # Iterate over the list of volumes and print out their details
    for volume in volumes['Volumes']:
        print('Volume ID: {0} Size: {1} Availability Zone: {2} '.format(volume['VolumeId'], volume['Size'], volume['AvailabilityZone']))

