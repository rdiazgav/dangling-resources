import boto3

ec2_client = boto3.client('ec2')

# Get all regions
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

print('')
print('List of unused network interfaces')
print('=================================')

# Loop over each region
for region in regions:
    # Switch to the current region
    ec2_client = boto3.client('ec2', region_name=region)
    # Get all network interfaces
    nis = ec2_client.describe_network_interfaces()['NetworkInterfaces']
    # Filter out network interfaces with associated instances
    unused_nis = [ni for ni in nis if not ni.get('Attachment')]
    # Print list of unused network interfaces
    for ni in unused_nis:
        print(f'Region: {region}, Network Interface Id: {ni["NetworkInterfaceId"]}')
