import pandas as pd 


input_files_location = 'D:/DataManagement-2/DS4C_DataSet_pandas_checking/'

# converting accumulated values into normal day wise values
def transform_accumulte(ser):
        temp= ser[0]
        ser = ser.diff()
        ser[0] = temp
        return ser

        
def transform_slices(df , col_name , value):
        # Adding slice number to male records
        df_ = df[df[col_name] == value].reset_index().drop('index', 1)
        df_['slice_no'] = pd.Series([int(i) for i in range (1 , df_.shape[0] +1 )])


        # converting accumulated values into normal day wise values
        df_["confirmed"] = transform_accumulte(df_["confirmed"] )
        df_["deceased"] = transform_accumulte(df_["deceased"] )

        if col_name == 'province':
                df_["released"] = transform_accumulte(df_["released"] )

        return df_

def replace_negative_values(ser):
        li = []
        for value in ser:
                if value >= 0 :
                        li.append(value)
                else:
                        li.append(0)
        return pd.Series(li)
