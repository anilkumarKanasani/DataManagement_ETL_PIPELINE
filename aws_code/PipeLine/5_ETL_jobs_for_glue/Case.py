# importing all requried packages
import pandas as pd 
import numpy as np
from user_defined_functions import replace_negative_values , input_files_location , provience_codes ,list_of_cities


# Taking path variables requried
input_file = input_files_location + "Case.csv"
staging_file= "D:/DataManagement-2/Staging_files/temp_Case.csv"
Transformed_file= "D:/DataManagement-2/Transfomed_files/Transformed_Case.csv"

# Extracting Data from DynamoDB
df = pd.read_csv(input_file)


######################### TRAANSFORMAITON PHASE ############################################################

# Spliting case_id into two seperate parts.. province_code and Case_id
df['province_code'] = df['case_id'].apply(lambda s : int( str(s)[:4]) )
df['case_id'] = df['case_id'].apply(lambda s: int(str(s)[5:]) )

# Removing all string values in numberical columnes and replacing with empty cells
numberic_cols = ['province_code' , 'case_id' ,  'confirmed' , 'latitude' , 'longitude']

for col in  numberic_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')


df.to_csv(staging_file)

# Cross validating the proviencs colum w.r.t Region.CSV (or) standard list of proviences
# If any starange value, replacing with Seoul
list_of_proviencs = list(provience_codes.keys())
df.loc[~df.province.isin(list_of_proviencs), 'province'] = 'Seoul'
df.to_csv(staging_file)



# Filling out missing city names.
# Considering missing cities as Provience main city
df.loc[~df.city.isin(list_of_cities), 'city'] = df.province
df.to_csv(staging_file)


# Checking consitency of group column
# If it not true (or) false, replacing it with true
df['group'] = df['group'].apply(lambda s:s.lower() if type(s) == str else s)
df.loc[~df.group.isin(['true' , 'false']), 'group'] = 'true'
df.to_csv(staging_file)



# Replacing all missed values of confirmed clolumn with minimum values
df['confirmed'].fillna(df['confirmed'].min() , inplace = True)


df['latitude'] = df['latitude'].fillna(method='ffill')
df['longitude'] = df['longitude'].fillna(method='ffill')
df.to_csv(staging_file)

	

df = df[['case_id', 'province' , 'province_code'  , 'city' , 'confirmed' , 'latitude' , 'longitude' ]]

# Generating Transformed csv file
df.to_csv(Transformed_file, index=False)
