from geotext import GeoText
from geopy.geocoders import Nominatim

replaces=[[' Éire / Ireland','Ireland']]#We can add here future countries that are not the same as properties.country
exceptions=['England','Scotland', 'Wales','Northern Ireland'] #This exception is created because their has a conflict with the libraries
#Those countries are in the country United Kingdom but United kingdom is a country so those places are not in the country libraries
#At the moment we see more exceptions countries we can add it here

def city_or_country(string): #This function identify the string as city or country
    try: # when the library don't detect the string as city or country  return ('','')
        places = GeoText(string)
        #places is a geotext value and .countries and .cities detect if is a city or country.
        if places.countries or string in exceptions:
            country=string
            #Return the tuple as needed
            return (country,'')
        elif places.cities:
            city=string
            #Call a function to detect the country
            country=get_tuple_country(city)
            return (country,city)
    except:
        return('','')
def get_tuple_country(city):#When is a city this function detect the country
    geolocator = Nominatim(user_agent="OTF_REQUEST")#Is usefull to create the coordenates and all trhe data about the city
    location = geolocator.geocode(city, exactly_one=True)
    #Modify the output to a simple country name
    location_split=location[0].split(',')
    country=location_split[-1]
    return country

def replacements(replaces,df_clients):#Replace all the name of the countries (library geopy) that doesn't has the same name as the df
    for i in replaces:
        df_clients['country found'] = df_clients['country found'].replace(i[0], i[1])
    return df_clients

def add_columns_country_city(countries_sear,city_sear,df_clients):#Add the new columns with the respective value
    for i in range(len(df_clients['properties.country'])):#pass to each value of the dataframe
        if df_clients['properties.country'][i] in city_sear:# if the value is a city add the country and city
            df_clients['country found'][i] = countries_sear[city_sear.index(df_clients['properties.country'][i])]
            df_clients['city found'][i] = city_sear[city_sear.index(df_clients['properties.country'][i])]
        if df_clients['properties.country'][i] in countries_sear:# if the value is a country only is going to add the country
            df_clients['country found'][i] = countries_sear[countries_sear.index(df_clients['properties.country'][i])]
            df_clients['city found'][i] = ''
    #Do the replacements
    df_clients=replacements(replaces, df_clients)
    return df_clients