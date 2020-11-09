# importing all requried packages
import pandas as pd 
import numpy as np
from user_defined_functions import transform_slices


# Taking path variables requried
input_file = "D:/DataManagement-2/DS4C_DataSet_pandas_checking/TimeAge.csv"
staging_file= "D:/DataManagement-2/Staging_files/temp_TimeAge.csv"
Transformed_file= "D:/DataManagement-2/Transfomed_files/Transformed_TimeAge.csv"

# Extracting Data from DynamoDB
df_ = pd.read_csv(input_file)

list_of_ages = ['0s' , '10s' , '20s' , '30s' , '40s' , '50s' , '60s' , '70s' , '80s' ]

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


df['age'] = df['age'].str.lower()

# Checking for value completency Quality Dimension
# If any null values, it will fillup with before row value in that column
df = (
        df.fillna(method='ffill')
        
)
# Replacing file in staging folder with latest
df.to_csv(staging_file)

# Adding Provice Code from Another dataframe
def get_age_group(row):
        codes = {'0s' : 1,
                '10s' : 2,
                '20s' : 3,
                '30s': 4, 
                '40s': 5, 
                '50s' : 6,
                '60s' : 7, 
                '70s' : 8,
                '80s' : 9 }
        return codes[row['age']]

df['age_group'] = df.apply(get_age_group, axis=1)


# Checking for Validity Quality Dimension
# If the date  & sex are not as per format, then replace with default value

li = []
for value in df['age']:
        if value in list_of_ages :
                li.append(value)
        else:
                li.append('40s')

df['age'] = pd.Series(li)


li = []
for value in df['confirmed']:
        if value >= 0 :
                li.append(value)
        else:
                li.append(0)

df['confirmed'] = pd.Series(li)



li = []
for value in df['deceased']:
        if value >= 0 :
                li.append(value)
        else:
                li.append(0)

df['deceased'] = pd.Series(li)




temp = pd.DataFrame()
for current_age in list_of_ages:
        temp = temp.append([transform_slices ( df , "age" , current_age) ] )


df = temp.sort_values(by=['slice_no' , 'age_group'], ascending=[True, True])



df = df[['slice_no', 'date' , 'age'  , 'age_group' , 'confirmed' , 'deceased' ]]
# Generating Transformed csv file
df.to_csv(Transformed_file, index=False)


