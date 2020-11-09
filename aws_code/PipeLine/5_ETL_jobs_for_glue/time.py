# importing all requried packages
import pandas as pd 
import numpy as np
from user_defined_functions import transform_slices , replace_negative_values , transform_accumulte ,input_files_location




# Taking path variables requried
input_file = input_files_location + "Time.csv"
staging_file= "D:/DataManagement-2/Staging_files/temp_Time.csv"
Transformed_file= "D:/DataManagement-2/Transfomed_files/Transformed_Time.csv"

######################### EXTRACTION PHASE ############################################################
df_ = pd.read_csv(input_file)


######################### TRAANSFORMAITON PHASE ############################################################

# Checking for Schema Completence Quality Dimension
# Deleting unwanted attributes in schema
df = (
        df_.drop('Record_id', 1)
        .drop('time', 1)
)
# Saving into staging folder
df.to_csv(staging_file)

# Removing all string values in numberical columnes and replacing with empty cells
numberic_cols = ['test' , 'negative' , 'confirmed' , 'released' ,  'deceased' ]

for col in  numberic_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')


df.to_csv(staging_file)

# Checking for value completency Quality Dimension
# If any null values, it will fillup with before row value in that column
df = (
        df.fillna(method='ffill')
        
)
# Replacing file in staging folder with latest
df.to_csv(staging_file)




df['test'] = replace_negative_values (df['test'])
df['negative'] = replace_negative_values (df['negative'])
df['confirmed'] = replace_negative_values (df['confirmed'])
df['released'] = replace_negative_values (df['released'])
df['deceased'] = replace_negative_values (df['deceased'])
df.to_csv(staging_file)


df['test'] = transform_accumulte(df['test'])
df['negative'] = transform_accumulte(df['negative'])
df['confirmed'] = transform_accumulte(df['confirmed'])
df['released'] = transform_accumulte(df['released'])
df['deceased'] = transform_accumulte(df['deceased'])

df.to_csv(staging_file)



df['slice_no'] = pd.Series ([ i for i in range (1,df.shape[0]+1)])
df.to_csv(staging_file)


######################### LOADING PHASE ############################################################
df = df[['slice_no', 'date' , 'test'  , 'negative',  'confirmed' , 'released', 'deceased'   ]]

df.to_csv(Transformed_file, index=False)

