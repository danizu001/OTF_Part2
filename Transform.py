import pandas as pd
import Country_functions
import Email_functions
import Phone_functions
import Request_html_country_code
import Duplicate_correct
import warnings


def call():
    exceptions=['England','Scotland', 'Wales','Northern Ireland']
    #Hide pandas warnings
    warnings.filterwarnings("ignore")
    #Read the csv 
    df_clients=pd.read_csv("Extract_data.csv",dtype=str)
    df_clients=df_clients.where(pd.notnull(df_clients), None)
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
    df_clients['found email']=''
    df_clients['fixed_phone number']=''
    df_clients['full name']=''
    #Add the correct values to the column
    df_clients=Country_functions.add_columns_country_city(countries_sear, city_sear, df_clients)
    #Add the column with the correct values of email
    df_clients=Email_functions.add_column_email(df_clients)
    #Get the country codes into a variable from web page
    countries_info=Request_html_country_code.get_table_code()
    #Get the phone code and set in the exceptions the number 44. so far are the only countries that has a problem with United Kingdom
    country_code=[(Phone_functions.get_phone_code(i,countries_info),i) if i not in exceptions else ('44',i) for i in set(countries_sear)]
    #Add the correct phone number to the data frame
    df_clients=Phone_functions.add_column_phone(df_clients,country_code)
    #Fix the dataframe to delte the duplicates as you want
    df_clients_no_dup=Duplicate_correct.correct_duplicate(df_clients)
    
    df_clients_no_dup.to_csv('Transform_data.csv', index=False)
    return df_clients_no_dup


