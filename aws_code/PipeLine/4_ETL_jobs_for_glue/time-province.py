# importing all requried packages
import pandas as pd 
import numpy as np
from user_defined_functions import transform_slices , replace_negative_values


# Taking path variables requried
input_file = "D:/DataManagement-2/DS4C_DataSet_pandas_checking/TimeProvince.csv"
staging_file= "D:/DataManagement-2/Staging_files/temp_TimeProvince.csv"
Transformed_file= "D:/DataManagement-2/Transfomed_files/Transformed_TimeProvince.csv"

# Extracting Data from DynamoDB
df_ = pd.read_csv(input_file)

list_of_proviences = ['Seoul' ,'Busan' ,'Daegu' ,'Incheon', 'Gwangju', 'Daejeon' ,'Ulsan', 'Sejong',
                        'Gyeonggi-do' ,'Gangwon-do', 'Chungcheongbuk-do' ,'Chungcheongnam-do',
                        'Jeollabuk-do' ,'Jeollanam-do', 'Gyeongsangbuk-do', 'Gyeongsangnam-do',
                        'Jeju-do']


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
        codes = {'Seoul' : 10000,
                'Busan' : 11000,
                'Daegu' : 12000,
                'Incheon': 14000, 
                'Gwangju': 13000, 
                'Daejeon' : 15000,
                'Ulsan' : 16000, 
                'Sejong' : 17000,
                'Gyeonggi-do' : 20000 ,
                'Gangwon-do' : 30000, 
                'Chungcheongbuk-do' : 40000,
                'Chungcheongnam-do' : 41000,
                'Jeollabuk-do' : 50000,
                'Jeollanam-do' : 51000, 
                'Gyeongsangbuk-do' : 60000, 
                'Gyeongsangnam-do' : 61000,
                'Jeju-do' : 70000 }
        return codes[row['province']]

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



df = df[['slice_no', 'date' , 'provice_code' , 'province'  , 'confirmed' , 'released', 'deceased'   ]]
# Generating Transformed csv file
df.to_csv(Transformed_file, index=False)