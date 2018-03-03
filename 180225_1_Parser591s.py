import requests
import json

res = requests.get('https://business.591.com.tw/home/search/rsList?is_new_list=1&type=2&kind=11&searchtype=1')
print(res)