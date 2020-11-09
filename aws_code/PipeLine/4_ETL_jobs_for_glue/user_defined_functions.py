import pandas as pd 
def transform_slices(df , col_name , value):
        # Adding slice number to male records
        df_ = df[df[col_name] == value].reset_index().drop('index', 1)
        rows , _ = df_.shape
        df_['slice_no'] = pd.Series([int(i) for i in range (1 , rows )])

        # converting accumulated values into normal day wise values
        temp_confirmed = df_.loc[ 0 , "confirmed"] 
        temp_deceased =  df_.loc[ 0 , "deceased"]

        if col_name == 'province':
                temp_released =  df_.loc[ 0 , "released"]
                df_['released'] = df_['released'].diff()
                df_.loc[ 0 , "released"] = temp_released

        
        df_['confirmed'] = df_['confirmed'].diff()
        df_['deceased'] = df_['deceased'].diff()
        df_.loc[ 0 , "confirmed"] = temp_confirmed
        df_.loc[ 0 , "deceased"] = temp_deceased
        return df_

def replace_negative_values(ser):
        li = []
        for value in ser:
                if value >= 0 :
                        li.append(value)
                else:
                        li.append(0)
        return pd.Series(li)