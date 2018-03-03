import requests
import json

headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

url = 'https://business.591.com.tw/home/search/rsList?is_new_list=1&type=2&kind=11&searchtype=1'

res = requests.get(url, headers  = headers)
# print(res)

data = json.loads(res.text)
print(data)