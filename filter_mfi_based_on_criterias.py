import pandas as pd
import os
user_distance_query_param ='711202'
result_list=[]
path = os.path.abspath('MFI_sheet.xls')

df = pd.read_excel(path)

for row in df.iterrows():
    if row[1]['pincode'] == int(user_distance_query_param):
        list= []
        list.append(row[1]['name'])
        list.append(row[1]['coordinates'])
        list.append(row[1]['distance'])
        list.append(row[1]['contact'])
        result_list.append(tuple(list))
print (result_list)






