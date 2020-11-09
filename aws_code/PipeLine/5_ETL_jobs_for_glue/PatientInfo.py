# importing all requried packages
import pandas as pd 
import numpy as np
from user_defined_functions import replace_negative_values , input_files_location , provience_codes ,list_of_cities ,age_group_codes


# Taking path variables requried
input_file = input_files_location + "PatientInfo.csv"
staging_file= "D:/DataManagement-2/Staging_files/temp_PatientInfo.csv"
Transformed_file= "D:/DataManagement-2/Transfomed_files/Transformed_PatientInfo.csv"

######################### EXTRACTION PHASE ############################################################
df = pd.read_csv(input_file)


######################### TRAANSFORMAITON PHASE ############################################################

# Spliting patient_id into two seperate parts.. province_code and patient_id
df['province_code'] = df['patient_id'].apply(lambda s : int( str(s)[:4]) )
df['patient_id'] = df['patient_id'].apply(lambda s: int(str(s)[5:]) )
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


# Checking consitency of sex column
# If it not true (or) false, replacing it with true
df['sex'] = df['sex'].apply(lambda s:s.lower() if type(s) == str else s)
df.loc[~df.sex.isin(['male' , 'female']), 'sex'] = 'male'
df.to_csv(staging_file)



df.loc[~df.age.isin(list(age_group_codes.keys())), 'age'] = '40s'

# Adding age_group based on standard of project
def get_age_group(row):
        return age_group_codes[row['age']]

df['age_group'] = df.apply(get_age_group, axis=1)
df.to_csv(staging_file)

# Filling down all the missed values of confirmed_date
df['confirmed_date'] = df['confirmed_date'].fillna(method='ffill')


# Filling all missing dates of symptom_onset_date with dates from confirmed_date
df['symptom_onset_date']= np.where(df['symptom_onset_date'].isnull(), df['confirmed_date'], df['symptom_onset_date'])


# Coping all empty released dates with confirmed dates ( but we have to delete the decesed cases) ..
df['released_date']= np.where(df['released_date'].isnull(), df['confirmed_date'], df['released_date'])

# Coping all empty deceased_dates with confirmed dates ( but we have to delete the released & Isolated cases) ..
df['deceased_date']= np.where(df['deceased_date'].isnull(), df['confirmed_date'], df['deceased_date'])

# Deleting all the deceased_date of released & Isolated cases
df.loc[df.state.isin(['released' , 'isolated']), 'deceased_date'] = ' '

# Deleting all the Released_date of deceased & Isolated cases
df.loc[df.state.isin(['deceased' , 'isolated']), 'released_date'] = ' '

df.to_csv(staging_file)

df['Origin_country'] = df['country'] 
######################### LOADING PHASE ############################################################

df = df[['patient_id',  'province_code'  , 'sex' , 'age' , 'age_group' , 'province' , 'city' , 'Origin_country' , 
        'symptom_onset_date' , 'confirmed_date' , 'released_date' , 'deceased_date' , 'state'   ]]


df.to_csv(Transformed_file, index=False)