import req_client_data
import pandas as pd
import Country_functions


url='https://api.hubapi.com/crm/v3/objects/contacts/search/'
properties=[ "raw_email", "country","phone", "technical_test___create_date", "industry", "address","hs_object_id"]
filters=[
    {
    "propertyName": "allowed_to_collect",
    "operator": "EQ",
    "value": "true"
    }
]
#If anything else is needed we could change the values of the url and so on
collected_data=req_client_data.collect_all_info(url,properties,filters)
#Help to pass the json format to a dataframe
df_clients=pd.json_normalize(collected_data)
#Collect all the values in properties.country without duplicates 
propCountries=set(df_clients['properties.country'])
#get the info as needed in the test (country, city)
result_countries=[Country_functions.city_or_country(i) for i in propCountries]
#Get the city and the country separate
countries_sear=[i[0] for i in result_countries]
city_sear=[i[1] for i in result_countries]
#Creates the new columns
df_clients['country found']=''
df_clients['city found']=''
#Add the correct values to the column
df_clients=Country_functions.add_columns_country_city(countries_sear, city_sear, df_clients)

