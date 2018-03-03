import requests
import json

headers = {
	'Cookie':'urlJumpIp=6;',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

url = 'https://business.591.com.tw/home/search/rsList?is_new_list=1&type=2&kind=11&searchtype=1'

res = requests.get(url, headers = headers)

data = json.loads(res.text)
# print(data)

# print(len(data))
# print(type(data))

# for key, value in data.items() :
	# print(key)

# print(data['data']['page'])

# for key , value in data['data'].items() :
	# print(key)

# print(type(data['data']['data']))

# print(type(data['data']['data'][0]))

# for key, value in data['data']['data'][0].items() :
# 	print(key)
# 	print(value)
# 	print('\n')


# print(len(data['data']['data'][0]))

# txt = open("591.txt", "w")
# for key, value in data['data']['data'][0].items() :
# 	txt.write("%s\t%s\n"% (key, value))

# print(len(data['data']['data']))

for idx in range(0, len(data['data']['data'])) :
	print(data['data']['data'][idx]['ltime'])

	# txt.write("%s\n\n"% value)
	# print(key)
	# print(value, '\n')

# txt.close()

# https://sale.591.com.tw/home/house/detail/2/4710515.html
# https://sale.591.com.tw/home/house/detail/2/4687598.html

# https://sale.591.com.tw/home/house/detail/2/4776056.html





