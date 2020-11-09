import pandas as pd 
def transform_slices(df , col_name , value):
        # Adding slice number to male records
        df_ = df[df[col_name] == value].reset_index().drop('index', 1)
        rows , columns = df_.shape
        df_['slice_no'] = pd.Series([int(i) for i in range (1 , rows )])

        # converting accumulated values into normal day wise values
        temp_confirmed = df_.loc[ 0 , "confirmed"]
        temp_deceased = df_.loc[ 0 , "deceased"]
        df_['confirmed'] = df_['confirmed'].diff()
        df_['deceased'] = df_['deceased'].diff()
        df_.loc[ 0 , "confirmed"] = temp_confirmed
        df_.loc[ 0 , "deceased"] = temp_deceased
        return df_