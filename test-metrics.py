import pprint
import boto3
from datetime import datetime
client = boto3.client('cloudwatch')

instID = 'i-000f5'
start_time = datetime(2019,4,16,18,00,00)
end_time = datetime(2019,4,17,10,00,00)

response = client.get_metric_statistics(\
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': instID
        },
    ],
    StartTime=start_time,
    EndTime=end_time,
    Period=600,
    Statistics=[
        'Average',
    ]
)
print(pprint.pprint(response['Datapoints']))
