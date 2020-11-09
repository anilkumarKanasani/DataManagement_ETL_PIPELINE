# importing all requried packages
import pandas as pd 
import numpy as np
from user_defined_functions import transform_slices , replace_negative_values , input_files_location ,provience_codes


# Taking path variables requried
input_file = input_files_location + "TimeProvince.csv"
staging_file= "D:/DataManagement-2/Staging_files/temp_TimeProvince.csv"
Transformed_file= "D:/DataManagement-2/Transfomed_files/Transformed_TimeProvince.csv"

######################### EXTRACTION PHASE ############################################################
df_ = pd.read_csv(input_file)

list_of_proviences = list(provience_codes.keys())

######################### TRAANSFORMAITON PHASE ############################################################

# Checking for Schema Completence Quality Dimension
# Deleting unwanted attributes in schema
df = (
        df_.drop('Record_id', 1)
        .drop('time', 1)
)
# Saving into staging folder
df.to_csv(staging_file)


# Adding Provice Code from Another dataframe
def get_provice_code(row):
        return provience_codes[row['province']]

df['provice_code'] = df.apply(get_provice_code, axis=1)


# Checking for value completency Quality Dimension
# If any null values, it will fillup with before row value in that column
df = (
        df.fillna(method='ffill')
        
)
# Replacing file in staging folder with latest
df.to_csv(staging_file)

# Removing all string values in numberical columnes and replacing with empty cells
numberic_cols = [ 'confirmed' , 'released' ,  'deceased' ]

for col in  numberic_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')


df.to_csv(staging_file)

df['confirmed'] = replace_negative_values (df['confirmed'])
df['deceased'] = replace_negative_values (df['deceased'])
df['released'] = replace_negative_values (df['released'])


temp = pd.DataFrame()
for current_pro in list_of_proviences:
        temp = temp.append([transform_slices ( df , "province" , current_pro) ] )

df = temp.sort_values(by=['slice_no' , 'provice_code'], ascending=[True, True])


######################### LOADING PHASE ############################################################
df = df[['slice_no', 'date' , 'provice_code' , 'province'  , 'confirmed' , 'released', 'deceased'   ]]

df.to_csv(Transformed_file, index=False)