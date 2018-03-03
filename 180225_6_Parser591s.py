import requests
import json

from lxml import html

headers = {
	'Cookie':'urlJumpIp=6;',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

url = 'https://business.591.com.tw/home/search/rsList?is_new_list=1&type=2&kind=11&searchtype=1&region=6&firstRow=60&totalRows=640'

res = requests.get(url, headers = headers)

data = json.loads(res.text)

# print(type(data))
# ==> <class 'dict'>

# print(len(data))
# ==> 4

# print(data.keys())
# dict_keys(['records', 'is_recom', 'data', 'status'])

# print(type(data['data']))
# ==> <class 'dict'>

# print(data['data'].keys())
# ==> dict_keys(['data', 'biddings', 'page', 'topData'])

# print(type(data['data']['data']))
# ==> <class 'list'>

# print(len(data['data']['data']))
# ==> 30

# print(type(data['data']['data'][0]))
# ==> <class 'dict'>

# print(data['data']['data'][0].keys())
# ltime, sectionname,... 98 indexeas

# for k in range(0,30) :
	# print(data['data']['data'][k]['post_id'],' ', data['data']['data'][k]['ltime'],' ', data['data']['data'][k]['sectionname'])

# print(data['data']['data'][0]['layout_str'])
# ==> <span class="layout">類別：住宅用地</span>

# print(type(data['data']['data'][0]['layout_str']))
# ==> <class 'str'>

# span class="layout"
# tree = html.fromstring(data['data']['data'][0]['layout_str'])
# landtype = tree.xpath('//span[@class="layout"]/text()')

# print(landtype)
# ==> ['類別：農地']

# print(type(landtype))
# ==> <class 'list'>

# print(len(landtype))

# EX: str.split(str="", num=string.count(str)).

# landtype = data['data']['data'][0]['layout_str']
# landtype = landtype.split('：')
# print(landtype)
# ==> ['<span class="layout">類別', '工業用地</span>']

# landtype = landtype[1].split('</span>')
# print(landtype[0])



# print(type(data['data']['data'][0]['price']))
# ==> replace(old, new[, max])

# price  = data['data']['data'][0]['price']
# print(price)
# ==> 29,400

# price = price.replace(",","")
# print(price)
# ==> 29400

# print(type(int(price)))
# ==> <class 'int'>

## milestone
# for k in range(0,30) :
# 	landtype = data['data']['data'][k]['layout_str']
# 	landtype = landtype.split('：')
# 	landtype = landtype[1].split('</span>')[0]
# 	if len(landtype) > 2 :
# 		landtype = landtype[0]+landtype[1]

# 	print(data['data']['data'][k]['post_id'],' ', data['data']['data'][k]['ltime'],' ', data['data']['data'][k]['sectionname'], '\t',
# 		landtype, '\t', data['data']['data'][k]['price'], '\t', data['data']['data'][k]['street_name'])
##
# print('工業'.encode("utf-8"))
# ==> b'\xe5\xb7\xa5\xe6\xa5\xad'


desection = ["平鎮".encode("big5"), "大園".encode("big5"), "新屋".encode("big5"), "龜山".encode("big5"),
 			 "楊梅".encode("big5"), "觀音".encode("big5"), "大溪".encode("big5"), "復興".encode("big5"), "龍潭".encode("big5")]
 			 
delandtype = ["工業".encode("big5"), "商業".encode("big5"), "林地".encode("big5")]

for k in range(0,30) :
	landtype = data['data']['data'][k]['layout_str']
	landtype = landtype.split('：')
	landtype = landtype[1].split('</span>')[0]

	if len(landtype) > 2 :
		landtype = landtype[0]+landtype[1]

	SN = data['data']['data'][k]['sectionname'][0]+data['data']['data'][k]['sectionname'][1]

	cFlag = 0

	for l in range(0, len(desection)) :
		if desection[l] == SN.encode("big5") :
			cFlag = 1

	for l in range(0, len(delandtype)) :
		if delandtype[l] == landtype.encode("big5") :
			cFlag = 1

	if cFlag:
		continue


	print(data['data']['data'][k]['post_id'],' ', data['data']['data'][k]['ltime'],' ', data['data']['data'][k]['sectionname'], '\t',
		landtype, '\t', data['data']['data'][k]['price'], '\t', data['data']['data'][k]['street_name'])




