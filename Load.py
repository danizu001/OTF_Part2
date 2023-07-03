import requests
import json
import sys

def json_send_contacts(url,data):# The function should work for all the endpoints and filters  
    # Request headers
    headers = {
        'Authorization': 'Bearer pat-na1-0b160beb-be0a-4c1b-9542-6629cc538908',
        'Content-Type': 'application/json'
          }
    data={'properties':data}
# Make the POST request
    response = requests.post(url, json=data, headers=headers)
    return response


def edit_send_info(url,df_clients_no_dup): #This function should work for all the endpoints
    jsons=df_clients_no_dup.to_json(orient='records', lines=True)
    jsons=jsons.replace('}\n{','}##{')
    jsons=jsons.split('##')
    for i in jsons:
        data=json.loads(i)
        response=json_send_contacts(url,data)
        if response==201:
            pass
        else:
            print(response)
    print('finish')


