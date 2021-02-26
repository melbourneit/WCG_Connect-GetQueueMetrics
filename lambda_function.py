import boto3, json, os
from metrics import *
from splunk import send_single_event


def lambda_handler(event, context):
    token = os.environ['SPLUNK_HEC_TOKEN']
    endpoint = os.environ['SPLUNK_HEC_URL']
    payload=  {}

    session = boto3.Session()

    for instance in Instances:
        for queue in Queues:
            for metric in ConnectMetrics:
                connect = session.client('connect',region_name='ap-southeast-2')
                response = connect.get_current_metric_data(
                    InstanceId=instance["InstanceId"],
                    Filters={
                        'Queues': [
                            queue["QueueId"]
                        ],
                        'Channels': [
                            'VOICE'
                        ]
                    },
                    Groupings=[
                        'QUEUE'
                    ],
                    CurrentMetrics=[
                    {
                        'Name': metric["MetricName"],
                        'Unit': metric["Unit"]
                    },
                    ]
                )
                if response['MetricResults'] != []:
                #Build event
                    event = {}
                    event["InstanceId"] = instance["InstanceId"]
                    event["InstanceName"] = instance["InstanceName"]
                    event["QueueId"] =  response['MetricResults'][0]['Dimensions']['Queue']['Id']
                    event["QueueName"] = queue["QueueName"]
                    event["MetricName"] = metric["MetricName"]
                    event["Unit"] = metric["Unit"]
                    event["Value"] = response['MetricResults'][0]['Collections'][0]['Value']
                    payload.update(event)
                    print(payload)
                    send_single_event(token,endpoint,event=payload)



