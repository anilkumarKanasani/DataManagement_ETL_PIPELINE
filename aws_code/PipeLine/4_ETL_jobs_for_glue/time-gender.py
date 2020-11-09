# importing all requried packages
import pandas as pd 
import numpy as np


# Taking path variables requried
input_file = "D:/DataManagement-2/DS4C_DataSet_pandas_checking/TimeGender.csv"
staging_file= "D:/DataManagement-2/Staging_files/temp_TimeGender.csv"

# Extracting Data from DynamoDB
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

li = []
for value in df['sex']:
        if value == 'male' or value == 'female':
                li.append(value)
        else:
                li.append('male')

df['sex'] = pd.Series(li)

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

# Adding slice number to male records
df_male = df[df['sex'] == 'male'].reset_index().drop('index', 1)
rows , columns = df_male.shape
df_male['slice_no'] = pd.Series([int(i) for i in range (1 , rows )])

# converting accumulated values into normal day wise values
temp_confirmed = df_male.loc[ 0 , "confirmed"]
temp_deceased = df_male.loc[ 0 , "deceased"]
df_male['confirmed'] = df_male['confirmed'].diff()
df_male['deceased'] = df_male['deceased'].diff()
df_male.loc[ 0 , "confirmed"] = temp_confirmed
df_male.loc[ 0 , "deceased"] = temp_deceased


# Adding slice number to Female records
df_female = df[df['sex'] == 'female'].reset_index().drop('index', 1)
rows , columns = df_female.shape
df_female['slice_no'] = pd.Series([int(i) for i in range (1 , rows )])

# converting accumulated values into normal day wise values
temp_confirmed = df_female.loc[ 0 , "confirmed"]
temp_deceased = df_female.loc[ 0 , "deceased"]
df_female['confirmed'] = df_female['confirmed'].diff()
df_female['deceased'] = df_female['deceased'].diff()
df_female.loc[ 0 , "confirmed"]= temp_confirmed
df_female.loc[ 0 , "deceased"] = temp_deceased

df = pd.concat([df_male , df_female]).sort_values(by=['slice_no'])


# Replacing file in staging folder with latest
df.to_csv(staging_file)


