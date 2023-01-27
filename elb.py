import boto3

# Create a session
session = boto3.session.Session()

# Create a client
elb_client = session.client('elb')
ec2 = boto3.client('ec2')
regions = [region['RegionName'] for region in ec2.describe_regions()['Regions']]

# Loop over each region
print('')
print('List of all ELBs without instances attached')
print('===========================================')

for region in regions:
    # Switch to the current region
    ec2 = boto3.client('ec2', region_name=region)
    # Get a list of all ELBs
    elbs = elb_client.describe_load_balancers()
    # Iterate through the list of ELBs
    for elb in elbs['LoadBalancerDescriptions']:
    # Get the list of attached instances for each ELB
        instances = elb_client.describe_instance_health(
            LoadBalancerName=elb['LoadBalancerName']
        )
        # Check if the list is empty
        if not instances['InstanceStates']:
            print(f'ELB {elb["LoadBalancerName"]} has no instances attached.')
