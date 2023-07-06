def get_phone_code(country_name,countries_info):#I didn't find a library who gives the phone code from the country name
    for i in countries_info:#Search in the web data all the countries.
        if i[0] in country_name:
            code=i[1]
            return code
    return 'XX'

def get_correct_number(string):#Get the string as phonecode/phonenumber and the convert the data as needed 
    code=string.split('/')[0]
    number=string.split('/')[1]
    number_no_0=number.lstrip('0')
    correct_number='+'+code+number_no_0
    return correct_number.replace('-','')

def add_column_phone(df_clients,country_code):#Get the email for each row
    for i in range(len(df_clients['properties.phone'])):
        for j in range(len(country_code)):
            if df_clients['properties.phone'][i] == None:#If there are not number phone, set an empty string
                df_clients['fixed_phone number'][i]=''
            else:
                if df_clients['country found'][i]!='':#If we know the country name go ahead
                    if df_clients['country found'][i] in country_code[j][1]:
                        df_clients['fixed_phone number'][i]=get_correct_number(country_code[j][0]+'/'+df_clients['properties.phone'][i])#add one by one the value in the correct column with the code and phone number 
                else:
                    df_clients['fixed_phone number'][i]=get_correct_number('XX/'+df_clients['properties.phone'][i])#If we don't know the country name set a 'XX' in the country code
    return df_clients