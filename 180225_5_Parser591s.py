import requests
import json

headers = {
	'Cookie':'urlJumpIp=6;',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

# url = 'https://business.591.com.tw/home/search/rsList?is_new_list=1&type=2&kind=11&searchtype=1'

x = 60

url = 'https://business.591.com.tw/home/search/rsList?is_new_list=1&type=2&kind=11&searchtype=1&region=6&firstRow=60&totalRows=640'

# url = 'abc'+str(x)+'def'
# print(url)



res = requests.get(url, headers = headers)
# print(res.url)
# print(type(res))


print(res.json())
# data = json.loads(res.text)

# for idx in range(0, len(data['data']['data'])) :
# 	print(data['data']['data'][idx]['ltime'])

	





