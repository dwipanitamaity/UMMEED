import json
from urllib2 import urlopen


class GPS:
    def get_current_loc(self):
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        try:
            data = json.load(response)
            #print(data['loc'])
            return data['loc']
        except Exception as e:
            e.__str__()
            return ""
