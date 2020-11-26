import boto3
import sys
import re

def get_s3_buckets(client):
    response = client.list_buckets()
    return [bucket['Name'] for bucket in response['Buckets']]


def empty_s3_bucket(bkt):
    print(f'Emptying bucket: `{bkt}`') 
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bkt)
    # suggested by Jordon Philips 
    bucket.objects.all().delete()


def delete_s3_bucket(client, bkt):
    print(f'Deleting bucket: `{bkt}`') 
    client.delete_bucket(Bucket=bkt)

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2 or len(argv) > 3:
        print("USAGE: python3 s3_buckets.py [list|delete] [pattern]")
        exit()
    task = argv[1]
    client = boto3.client('s3')

    s3_bucket_list = get_s3_buckets(client)

    tcat_bkt_list = [bkt  for bkt in s3_bucket_list if bkt.startswith('tcat-')]

    for bkt in tcat_bkt_list:
        print(bkt)

    confirm = input('Do you want to delete above bucket  > ')
    if confirm == 'y':
        for bkt in tcat_bkt_list:
            empty_s3_bucket(bkt)
            delete_s3_bucket(client, bkt)


    #if task.lower() == "list":
    #    for bkt in s3_bucket_list:
    #        if bkt.startswith('tcat'):
    #            #print(bkt)
    #elif task.lower() == "release":
    #    release_eips(client, unassociated_eips)
