Instances = [
    {
        "InstanceName" : "arq-netregistry",
        "InstanceId" : '8bf12987-e86b-4f87-8080-185544c17b7c',
     },
    # {
    #     "InstanceName" : "arq-netregistry-staging",
    #     "InstanceId" : '9635fb7b-7022-4dac-a237-3d2a8a73f03b',
    # }
]

WMESalesQueues = [
    {
        "QueueName" : "SMB_WME_SALES",
        "QueueId" : "55af34de-d23e-46d4-bfd5-56571105fc61",
    },
    {
        "QueueName" : "SMB_WME_PPC",
        "QueueId" : "20a0b3ef-3076-4229-8a66-6a1fccf358bd",
    },
    {
        "QueueName" : "SMB_WME_SEO",
        "QueueId" : "78a3dfdd-a224-44be-9257-4a9031a5f879",
    }
]

Queues = [
    {
        "QueueName" : "Netregistry - Care Admin",
        "QueueId" : "c32cbc0f-b731-4b64-ab64-e7bb5d7db858",
    },
    {
        "QueueName" : "Netregistry - Care Extended Team",
        "QueueId" : "d1ca383d-e8f2-4462-9538-b881e54fad41",
    },
    {
        "QueueName" : "Netregistry - Care Technical Support",
        "QueueId" : "343aedb5-fb66-4957-a404-54e063b3f145",
    },
    {
        "QueueName" : "Melbourne IT - Care Technical Support",
        "QueueId" : "41c28c40-e024-478c-bc92-782d2d2032b6",
    },
    {
        "QueueName" : "Melbourne IT - Care Extended Team",
        "QueueId" : "56e5e22c-c89c-424d-8f4e-da647ef4d947",
    },
    {
        "QueueName" : "Melbourne IT - Care Admin",
        "QueueId" : "a8fef19e-23db-4112-a155-7f4e4c2e7ccb",
    },
    {
        "QueueName" : "Domainz - Care Technical Support",
        "QueueId" : "67bd5178-b9c7-4e4f-970e-85b83db6fcf6",
    },
    {
        "QueueName" : "Domainz - Care Admin",
        "QueueId" : "015a4b1e-f43d-43f2-b97e-29a9f687de5f",
    },
    {
        "QueueName" : "Domainz - Care Extended Team",
        "QueueId" : "fd59dcad-d4e6-4ad1-a64c-6425297ec89c",
    },
    {
        "QueueName" : "Corporate IT",
        "QueueId" : "b2abfa52-850a-46fc-96ff-bb9a692e15b9",
    },
    {
        "QueueName" : "Telstra CS1",
        "QueueId" : "a7ae7e27-6663-4d9c-bb33-5b24fa4fb6ae",
    },
    {
        "QueueName" : "Reception",
        "QueueId" : "48432e21-b1bc-471d-b67d-49d474507e1d",
    }
]

ConnectMetrics = [
    {
        "MetricName" : "AGENTS_ONLINE",
        "Unit" : "COUNT",
        "Statistic" : "MAX"
    },
    {
        "MetricName" : "AGENTS_AVAILABLE",
        "Unit" : "COUNT",
        "Statistic" : "MAX"
    },
    {
        "MetricName" : "AGENTS_ON_CALL",
        "Unit" : "COUNT",
        "Statistic" : "MAX"
    },
    {
        "MetricName" : "AGENTS_NON_PRODUCTIVE",
        "Unit" : "COUNT",
        "Statistic" : "MAX"
    },
    {
        "MetricName" : "AGENTS_AFTER_CONTACT_WORK",
        "Unit" : "COUNT",
        "Statistic" : "MAX"
    },
    {
        "MetricName" : "AGENTS_ERROR",
        "Unit" : "COUNT",
        "Statistic" : "MAX"
    },
    {
        "MetricName" : "AGENTS_STAFFED",
        "Unit" : "COUNT",
        "Statistic" : "MAX"
    },
    {
        "MetricName" : "CONTACTS_IN_QUEUE",
        "Unit" : "COUNT",
        "Statistic" : "MAX"
    },
    {
        "MetricName" : "CONTACTS_SCHEDULED",
        "Unit" : "COUNT",
        "Statistic" : "MAX"
    },
    {
        "MetricName" : "AGENTS_ON_CONTACT",
        "Unit" : "COUNT",
        "Statistic" : "MAX"
    },
    {
        "MetricName" : "SLOTS_ACTIVE",
        "Unit" : "COUNT",
        "Statistic" : "MAX"
    },
    {
        "MetricName" : "SLOTS_AVAILABLE",
        "Unit" : "COUNT",
        "Statistic" : "MAX"
    },
    {
        "MetricName" : "OLDEST_CONTACT_AGE",
        "Unit" : "SECONDS",
        "Statistic" : "MAX"
    }
    # {
    #     "MetricName" : "SERVICE_LEVEL"
    #     "Threshold" : {
    #             "Comparison": "LT",
    #             "ThresholdValue": 60
    #         },
    #     "Unit" : "PERCENT"
    #     "Statistic" : "MAX"
    # },
    # {
    #     "MetricName" : "SERVICE_LEVEL"
    #     "Threshold" : {
    #             "Comparison": "LT",
    #             "ThresholdValue": 90
    #         },
    #     "Unit" : "PERCENT"
    #     "STATISTIC" : "MAX"
    # },
    # {
    #     "MetricName" : "SERVICE_LEVEL"
    #     "Threshold" : {
    #             "Comparison": "LT",
    #             "ThresholdValue": 300
    #         },
    #     "Unit" : "PERCENT"
    #     "STATISTIC" : "MAX"
    # }
]


ConnectInstanceMetrics = [
    {
        "NameSpace" : "AWS/Connect",
        "MetricName" : "ToInstancePacketLossRate",
        "Unit" : "Percent",
        "Period" : 3600,
        "Dimensions" : [
            {
                "Name" : "Participant",
                "Value" : "Agent"
            },
            {
                "Name" : "Type of Connection",
                "Value" : "WebRTC"
            },
            {
                "Name": "Stream Type",
                "Value": "Voice"
            }
        ]
    },
        {
        "NameSpace" : "AWS/Connect",
        "MetricName" : "ConcurrentCalls",
        "Unit" : "Count",
        "Period" : 300,
        "Dimensions" : [
            {
                "Name" : "MetricGroup",
                "Value" : "VoiceCalls"
            }
        ]
    }
]
