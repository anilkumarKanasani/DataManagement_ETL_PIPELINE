# importing all requried packages
import pandas as pd 
import numpy as np
from user_defined_functions import transform_slices , replace_negative_values, input_files_location , input_files_location


# Taking path variables requried
input_file = input_files_location + "Weather.csv"
staging_file= "D:/DataManagement-2/Staging_files/temp_Weather.csv"
Transformed_file= "D:/DataManagement-2/Transfomed_files/Transformed_Weather.csv"

######################### EXTRACTION PHASE ############################################################
df_ = pd.read_csv(input_file)


######################### TRANSFORMAITON PHASE ############################################################

# Checking for Schema Completence Quality Dimension
# Deleting unwanted attributes in schema
df = (
        df_.drop('Record_id', 1)
)
# Saving into staging folder
df.to_csv(staging_file)


# Removing all string values in numberical columnes and replacing with empty cells
numberic_cols = ['avg_temp' , 'min_temp' , 'max_temp' , 'precipitation' ,  'max_wind_speed' , 'most_wind_direction',
        'avg_relative_humidity' , 'code']

for col in  numberic_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')


df.to_csv(staging_file)


# Checking for value completency Quality Dimension
# If any null values, it will fillup with before row value in that column


df['avg_temp'].fillna(df['avg_temp'].min() , inplace = True)
df['min_temp'].fillna(df['min_temp'].min() , inplace = True)

df['max_temp'].fillna(df['max_temp'].min() , inplace = True)

df['precipitation'].fillna(df['precipitation'].min() , inplace = True)
df['max_wind_speed'].fillna(df['max_wind_speed'].min() , inplace = True)
df['most_wind_direction'].fillna(df['most_wind_direction'].min() , inplace = True)
df['avg_relative_humidity'].fillna(df['avg_relative_humidity'].min() , inplace = True)
df['date'] = df['date'].fillna(method='ffill')
df['province'] = df['province'].fillna(method='ffill')
df['code'] = df['code'].fillna(method='ffill')





# Replacing file in staging folder with latest
df.to_csv(staging_file)



def transform_slices(df , col_name , value):
        # Adding slice number to male records
        df_ = df[df[col_name] == value].reset_index().drop('index', 1)
        df_['slice_no'] = pd.Series([int(i) for i in range (1 , df_.shape[0] +1 )])
        return df_

list_of_proviences = ['Seoul' ,'Busan' ,'Daegu' , 'Gwangju', 'Incheon',  'Daejeon' ,'Ulsan',
                        'Gyeonggi-do' ,'Gangwon-do', 'Chungcheongbuk-do' ,'Chungcheongnam-do',
                        'Jeollabuk-do' ,'Jeollanam-do', 'Gyeongsangbuk-do', 'Gyeongsangnam-do',
                        'Jeju-do']
                        

temp = pd.DataFrame()
for current_pro in list_of_proviences:
        temp = temp.append([transform_slices ( df , "province" , current_pro) ] )

temp['provice_code'] = temp['code']
df = temp.sort_values(by=['slice_no' , 'provice_code'], ascending=[True, True])
df.to_csv(staging_file)


######################### LOADING PHASE ############################################################
df = df[['slice_no', 'date' , 'provice_code' , 'province', 'avg_temp' , 'min_temp' , 'max_temp' , 'precipitation' ,  'max_wind_speed' , 'most_wind_direction',
        'avg_relative_humidity' ]]
df.to_csv(Transformed_file, index=False)