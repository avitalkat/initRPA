import requests
import json
import datetime
import sys

# arguments
project_id = sys.argv[1]
file_name = sys.argv[2]
period = sys.argv[3]
projectType = sys.argv[4]


# Function Authenticate: Retrieve Token for Authorization
def httpAuthenticate_Orchestrator(in_ETLapiusers, in_ETLapipass, in_ETLTenant, in_URL):
    try:
        url = in_URL
        payload = json.dumps({
            "password": str(in_ETLapipass),
            "usernameOrEmailAddress": str(in_ETLapiusers),
            "tenancyName": str(in_ETLTenant)
        })
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        json_object = json.loads(response.text)
        print(str(response.status_code))
        # print(json_object["result"])
        return str(json_object["result"])
    except:
        print('Fail')
        return 'Fail'


# Function:Add Queue Item on Uipath Orchestrator
def httpAddQueueItems_Orchestrator(in_projectId, in_URL, in_Token, in_QueueName, in_timestamp, in_filename, in_period, in_projectType):
    try:
        url = in_URL
        payload = json.dumps({
            "itemData": {
                "Priority": "Normal",
                "Name": str(in_QueueName),
                "SpecificContent": {
                    "in_projectId": in_projectId,
                    "in_timestamp": str(in_timestamp),
                    "in_filename": in_filename,
                    "in_period": in_period,
                    "in_projectType": in_projectType,
                },
                "Reference": "ETL"
            }
        })
        headers = {
            'X-UIPATH-OrganizationUnitId': '',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + in_Token
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        print(str(response.status_code))
        return response.text
    except:
        print('Fail')
        return 'Fail'


# Variables to Call Function : usually the folowing ones will not change
# OnPremuser: orchestrator username (this particular one was created for ETL process)
# OnPrempass = orchestrator password for the user
# OnPremtenant = orchestrator tenat name
# OnPremUrlAuth = POST orchestrator authetication end point
# OnPremUrlAddQueue = POST orchestrator add queue item end point

OnPremuser = "apiConnectETL"
OnPrempass = "pap2021A!"
OnPremtenant = "Default"
OnPremUrlAuth = "https://orchestrator-prod.rpa.papayaglobal.com/api/Account/Authenticate"
OnPremUrlAddQueue = "https://orchestrator-prod.rpa.papayaglobal.com/odata/Queues/UiPathODataSvc.AddQueueItem"

# Variables to Call Function : usually the folowing ones will not change
# projectId: projectid to be processed by RPA
# OnPremQueue = queueName where the process will be added
# OnPremTime = timestamp
# OnPremFileName = filename that triggered ETL
OnPremProjectId = project_id  # arg1
OnPremFileName = file_name  # arg2
OnPremPeriod = period  # arg3
OnPremProjectType = projectType
OnPremQueue = "ETL_RPA_Queue"
OnPremTime = datetime.datetime.now()


OnPremtoken = httpAuthenticate_Orchestrator(OnPremuser, OnPrempass, OnPremtenant, OnPremUrlAuth)
httpAddQueueItems_Orchestrator(OnPremProjectId, OnPremUrlAddQueue, OnPremtoken, OnPremQueue, OnPremTime, OnPremFileName, OnPremPeriod, OnPremProjectType)


