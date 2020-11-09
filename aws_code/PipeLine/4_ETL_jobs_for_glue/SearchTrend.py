# importing all requried packages
import pandas as pd 
import numpy as np
from user_defined_functions import transform_slices , replace_negative_values 


# Taking path variables requried
input_file = "D:/DataManagement-2/DS4C_DataSet_pandas_checking/SearchTrend.csv"
staging_file= "D:/DataManagement-2/Staging_files/temp_SearchTrend.csv"
Transformed_file= "D:/DataManagement-2/Transfomed_files/Transformed_SearchTrend.csv"

# Extracting Data from DynamoDB
df_ = pd.read_csv(input_file)


######################### TRAANSFORMAITON PHASE ############################################################

# Checking for Schema Completence Quality Dimension
# Deleting unwanted attributes in schema
df = (
        df_.drop('Record_id', 1)
)
# Saving into staging folder
df.to_csv(staging_file)



# Removing all string values in numberical columnes and replacing with empty cells
numberic_cols = ['cold' , 'flu' ,  'pneumonia' ,  'coronavirus' ]

for col in  numberic_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')


df.to_csv(staging_file)



# Checking for value completency Quality Dimension
# If any null values, it will fillup with before row value in that column


df['cold'].fillna(df['cold'].min() , inplace = True)
df['flu'].fillna(df['flu'].min() , inplace = True)

df['pneumonia'].fillna(df['pneumonia'].min() , inplace = True)

df['coronavirus'].fillna(df['coronavirus'].min() , inplace = True)
df['date'] = df['date'].fillna(method='ffill')

# Replacing file in staging folder with latest
df.to_csv(staging_file)


# Adding Slice numbers
df['slice_no'] = pd.Series ([ i for i in range (1,df.shape[0]+1)])
df.to_csv(staging_file)



df = df[['slice_no', 'date' , 'cold' , 'flu' ,  'pneumonia' ,  'coronavirus' ]]
# Generating Transformed csv file
df.to_csv(Transformed_file, index=False)
