import boto3
import sys


def get_unassociated_eips(client):
    return [x for x in client.describe_addresses()['Addresses'] if 'AssociationId' not in x]


def release_eips(client, eip_list):
    for eip in eip_list:
        client.release_address(AllocationId=eip['AllocationId'])
        print("Released EIP: {}".format(eip['PublicIp']))


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2 or len(argv) > 3:
        print("USAGE: python3 unassociated_eips.py [list|release]")
        exit()
    task = argv[1]
    region = 'ap-south-1' if len(argv) == 2 else argv[2]
    client = boto3.client('ec2', region_name=region)

    unassociated_eips = get_unassociated_eips(client)
    if len(unassociated_eips) == 0:
        print("No Unassociated EIPs found in region: {}!".format(region))
        exit()
    if task.lower() == "list":
        print([x['PublicIp'] for x in unassociated_eips])
    elif task.lower() == "release":
        release_eips(client, unassociated_eips)
