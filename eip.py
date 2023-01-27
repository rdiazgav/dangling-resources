import boto3

ec2_client = boto3.client('ec2')
# Get all regions
regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]

# Loop over each region
print('')
print('list of unused/unttached EIPs')
print('=============================')

for region in regions:
    # Switch to the current region
    ec2_client = boto3.client('ec2', region_name=region)
    # Get all EIPs
    eips = ec2_client.describe_addresses()['Addresses']
    # Filter out EIPs with associated instances
    eips_without_network_interface = [eip for eip in eips if not eip.get('NetworkInterfaceId')]
    # Print list of EIPs without associated instances
    for eip in eips_without_network_interface:
    #print(eip['PublicIp'])
        print(f'Region: {region}, IP Address: {eip["PublicIp"]}')
