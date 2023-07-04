import requests
import json
import pandas as pd

def json_send_contacts(url,data):# The function should work for all the endpoints and filters  
    # Request headers
    headers = {
        'Authorization': 'Bearer pat-na1-0b160beb-be0a-4c1b-9542-6629cc538908',#My private key 
        'Content-Type': 'application/json'
          }
    data={'properties':data}
    # Make the POST request
    response = requests.post(url, json=data, headers=headers)
    return response


def edit_send_info(url,df_clients_no_dup): #This function should work for all the endpoints
    jsons=df_clients_no_dup.to_json(orient='records', lines=True)#df to json
    jsons=jsons.replace('}\n{','}##{')#replace the space between properties for something we could slpit then
    jsons=jsons.split('##')#Split the jsons in multiple lists of json
    for i in jsons:#I can't send multiple properties in a single request, may be exist but I did´nt find it
        data=json.loads(i)
        json_send_contacts(url,data)
    print('finish')
    
    
def call():
    url_post='https://api.hubapi.com/crm/v3/objects/contacts'
    df_clients_no_dup=pd.read_csv("Transform_data.csv",dtype=str)#Get the csv to df
    df_clients_no_dup=df_clients_no_dup.where(pd.notnull(df_clients_no_dup), None)#Change the nan values to None
    edit_send_info(url_post, df_clients_no_dup)

