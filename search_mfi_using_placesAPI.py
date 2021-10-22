import json
import pandas as pd
import requests
import gps

if __name__ == '__main__':
    API_KEY='i70ykL_KDbRxb9HfiHJR05bBfnf_8nRjHqElwNspoIo'
    #current_location = (22.5626,88.3630)
    current_location = gps.GPS.get_current_loc()
    search_string = 'bank'

    #url = 'https://discover.search.hereapi.com/v1/discover?at=22.5626,88.3630&q=bank&apiKey=i70ykL_KDbRxb9HfiHJR05bBfnf_8nRjHqElwNspoIo'
    url = 'https://discover.search.hereapi.com/v1/discover?at={current_location}&q=bank&apiKey=i70ykL_KDbRxb9HfiHJR05bBfnf_8nRjHqElwNspoIo'
    payload ={}
    headers ={}
    response = requests.get(url, headers=headers, json= payload).text
    data = json.loads(response)

    result= pd.DataFrame
    result['name']= []
    result['distnce']= []
    result['coordinates']= []
    result['contact']= []
    result['pincode']= []

    df = pd.DataFrame
    for i in range(len(data['items'])):
        for item in data['items']:
            if item['distance'] <= int('20000'): # Within a radius of 20km
                result.insert(i , item['title'], item['distance'], item['position', item['contacts']['phone'], item['address']['postalcode']])
    data_df= pd.DataFrame.from_dict(result)

    df.to_excel(r"Users\deepa\Desktop\GPS\MFI_sheet.xlsx", index=False, header=True)


