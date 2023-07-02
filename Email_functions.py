def get_email(string):#Adapt the string to only have the email
    string=string.replace('<',',')
    string=string.replace('>',',')
    email=string.split(',')[1]
    return email

def add_column_email(df_clients):#Get the email for each row
    for i in range(len(df_clients['properties.raw_email'])):
        if df_clients['properties.raw_email'][i] != None:
            df_clients['found email'][i]=get_email(df_clients['properties.raw_email'][i])
    return df_clients