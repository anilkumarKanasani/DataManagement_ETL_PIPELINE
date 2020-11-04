ort pandas as pd
from pandas_profiling import ProfileReport as pr
import os


for file in os.listdir("D:\DataManagement-2\DS4C_DataSet"):
    csv_file_path = "D:\DataManagement-2\DS4C_DataSet\"+file
    df = pd.read_csv()
    profile = pr(df, title= file + ' PROFILING REPORT' , explorative=True)
    output_filename = 'D:\DataManagement-2\Data_Profiling\ ' + file[:-4] + '.html'
    profile.to_file(output_filename)