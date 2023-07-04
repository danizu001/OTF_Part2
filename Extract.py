import requests
import pandas as pd



def json_description_contacts(url,limit,after,properties=[],filters=[]):# The function should work for all the endpoints and filters  
    # Request data
    data = {
        #Number of data in the request -> max is 100
        "limit":limit,
        "after":after,
        "properties": properties,
        "filters":filters
      }
    
    # Request headers
    headers = {
        'Authorization': 'Bearer pat-na1-3c7b0af9-bb66-40e7-a256-ce4c5eb27e81',
        'Content-Type': 'application/json'
    }

# Make the POST request
    response = requests.post(url, json=data, headers=headers)
    return response


def collect_all_info(url,properties=[],filters=[]): #This function should work for all the endpoints
    collect_data=[]
    limit=100
    after=0
    response=json_description_contacts(url,limit,after,properties,filters)
    collect_data+=response.json()['results']
    loop=response.json()['total']
    for i in range(loop//100):
        after+=limit
        response=json_description_contacts(url,limit,after,properties,filters)
        collect_data+=response.json()['results']
    return collect_data

def call():
    url='https://api.hubapi.com/crm/v3/objects/contacts/search/'
    properties=[ "firstname","lastname","raw_email", "country","phone", "technical_test___create_date", "industry", "address","hs_object_id"]
    filters=[
        {
        "propertyName": "allowed_to_collect",
        "operator": "EQ",
        "value": "true"
        }
    ]
    collected_data=collect_all_info(url,properties,filters)
    df_clients=pd.json_normalize(collected_data)
    df_clients.to_csv('Extract_data.csv', index=False)
    return df_clients