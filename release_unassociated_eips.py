import boto3

client = boto3.client('ec2', region_name='ap-south-1')


def get_unassociated_eips():
    return [x for x in client.describe_addresses()['Addresses'] if 'AssociationId' not in x]


def release_eips(eip_list):
    for eip in eip_list:
        client.release_address(AllocationId=eip['AllocationId'])
        print("Released EIP: {}".format(eip['PublicIp']))


if __name__ == "__main__":
    unassociated_eips = get_unassociated_eips()
    release_eips(unassociated_eips)
