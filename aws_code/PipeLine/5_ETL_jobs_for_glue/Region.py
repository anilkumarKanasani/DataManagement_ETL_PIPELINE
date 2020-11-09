# importing all requried packages
import pandas as pd 
import numpy as np
from user_defined_functions import replace_negative_values , input_files_location



# Taking path variables requried
input_file = input_files_location + "Region.csv"
staging_file= "D:/DataManagement-2/Staging_files/temp_Region.csv"
Transformed_file= "D:/DataManagement-2/Transfomed_files/Transformed_Region.csv"

######################### EXTRACTION PHASE ############################################################
df = pd.read_csv(input_file)

######################### TRANSFORMAITON PHASE ############################################################

# Removing all string values in numberical columnes and replacing with empty cells
numberic_cols = ['code' ,  'latitude' , 'longitude' , 'elementary_school_count',
                 'kindergarten_count' , 'university_count' , 'academy_ratio' , 'elderly_population_ratio',
                 'elderly_alone_ratio' , 'nursing_home_count']

for col in  numberic_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')


df.to_csv(staging_file)


# Checking for value completency Quality Dimension
# If any null values, it will fillup with before row value in that column

for col in numberic_cols:
        df[col].fillna(df[col].min() , inplace = True)

# Filling all string type columns

df['province'] = df['province'].fillna(method='ffill')
df['city'] = df['city'].fillna(method='ffill')


# Replacing file in staging folder with latest
df.to_csv(staging_file)


#Replacing if any negative values in numerical columns
for col in numberic_cols:
        df[col] = replace_negative_values(df[col])

# No slicing requried for this table. This is static data.

######################### LOADING PHASE ############################################################
# Generating Transformed csv file
df.to_csv(Transformed_file, index=False)