# importing all requried packages
import pandas as pd 
import numpy as np
from user_defined_functions import transform_slices , replace_negative_values , input_files_location 


# Taking path variables requried
input_file = input_files_location + "TimeGender.csv"
staging_file= "D:/DataManagement-2/Staging_files/temp_TimeGender.csv"
Transformed_file= "D:/DataManagement-2/Transfomed_files/Transformed_TimeGender.csv"

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
numberic_cols = [ 'confirmed' ,  'deceased' ]

for col in  numberic_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')


df.to_csv(staging_file)

# Chekcing for consistency Quality Dimension



df['sex'] = df['sex'].str.lower()

# Checking for value completency Quality Dimension
# If any null values, it will fillup with before row value in that column
df = (
        df.fillna(method='ffill')
        
)
# Replacing file in staging folder with latest
df.to_csv(staging_file)




# Checking for Validity Quality Dimension
# If the date  & sex are not as per format, then replace with default value

df.loc[~df.sex.isin(['male' , 'female']), 'sex'] = 'male'


df['confirmed'] = replace_negative_values (df['confirmed'])
df['deceased'] = replace_negative_values (df['deceased'])



df_male = transform_slices ( df , "sex" , "male")
df_female = transform_slices ( df , "sex" , "female")

df = pd.concat([df_male , df_female]).sort_values(by=['slice_no'])

######################### LOADING PHASE ############################################################
df = df[['slice_no', 'date' , 'sex' , 'confirmed' , 'deceased' ]]

df.to_csv(Transformed_file, index=False)


