import requests
import json

headers = {
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

res = requests.get('https://business.591.com.tw/home/search/rsList?is_new_list=1&type=2&kind=11&searchtype=1&region=6&firstRow=90&totalRows=1579', headers = headers)


# https://business.591.com.tw/home/search/rsList?is_new_list=1&type=2&kind=11&searchtype=1
# https://business.591.com.tw/home/search/rsList?is_new_list=1&type=2&kind=11&searchtype=1

# print(res.text)
data = json.loads(res.text)

print(data)
# print(len(data['data']))

# print(data['data'].keys())
# print(type(data))

# print(data['data']['data'])

# print(type(data['data']['data']))
# print(data['data']['data'][0])
# print(type(data['data']['data'][0]))

# print(data['data']['data'][0].keys())
# print(data['data']['data'][0]['mainarea'])
# print(data['data']['data'][1]['allfloor'])
# print(data['data']['data'][1]['regionname'])
# print(data['data']['data'][1]['filename'])


# print(len(data['data']['data']))

# datalength = 30

# for i in range(0, datalength):
# 	for key, value in data['data']['data'][i].items() :
# 		# print(key)
# 	  	if key == 'ltime' :
# 	   		print(value)



