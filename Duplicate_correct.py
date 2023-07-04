import pandas as pd

def correct_duplicate(df_clients):
    df_clients['full name']=df_clients['properties.firstname']+' '+df_clients['properties.lastname']# Create the full name in a new column
    unique_names=list(set(df_clients['full name']))#Get a list with the unique names
    group_array=[None]*len(unique_names)#Create an empty array with the length of the unique names
    for i in range(len(unique_names)):
        group_array[i]=df_clients.loc[df_clients['full name'] == unique_names[i]]#Assign in each space of  the empty array all the rows with the same name in the dataframe
        if group_array[i].empty: #save the index of the empy name to delete it after the FOR loop
            save=i
    del group_array[save]#Delete the empty name
    group_array_nan=df_clients.loc[df_clients['full name'].isnull()].reset_index(drop=True)#Create a datafrane with the nan values in full name
    drop=[]
    for i in range(len(group_array_nan)):
        for j in range(len(group_array)):
            if group_array_nan.iloc[i]['found email'] in group_array[j]['found email'].values:#Detect when a nan full name has a same email as other full name (non nan)
                group_array[j].append(group_array_nan.iloc[i])#If exist then save the row of nan full name in the array of dataframes (Is important know that here we are grouping by email after we did the grouping by name)
                drop.append(i)#Save the index of the rows that were saved in the respective group. Why? Because it could be a possibility that one email of the full name nan doesn't exist in the list of the dataframes     
                break
    group_array_nan=group_array_nan.drop(labels=drop)#Drop the values, in this case there are not single emails
    def_array=[]

    for i in range(len(group_array)):
        group_array[i]=group_array[i].sort_values(by=['properties.technical_test___create_date'], ascending=False)#Sort the values by createdAt (Remember at this time we have all grouped in a list so for example in list[0] are all the records of sara, in list[1] all of Jhon and so on)
        def_array.append(group_array[i].loc[group_array[i]['properties.technical_test___create_date'] == max(group_array[i]['properties.technical_test___create_date'].values), ["properties.hs_object_id","full name","found email","country found","city found", "fixed_phone number","properties.industry","properties.technical_test___create_date"]].iloc[0])#Detect the max value of created date and also put the data as we want and save it in a new list
        new_industry=';'+';'.join(list(set(group_array[i]['properties.industry'].values)))#Put the industry as we want
        def_array[i]['properties.industry']=new_industry#Change the value of property on the new list
        if def_array[i].isnull().values.any():#Detect if there are one ore more values in nan
            none_values=def_array[i].isna().index[def_array[i].isna() == None] # If exist detect the name of the index
            for j in none_values:
                for k in range(len(group_array[i])):
                    if group_array[i].iloc[k][j]!=None:
                        def_array[i][j]=group_array[i].iloc[k][j]#Change the value of the indexes in nan with the previous sorted values 
                        break
    def_array=pd.DataFrame(def_array)
    def_array.columns=['temporary_id', 'firstname', 'email', 'country','city', 'phone', 'original_industry', 'original_create_date']
    def_array['original_create_date'] = def_array['original_create_date'].map(lambda x: (x[:10]))
    return def_array