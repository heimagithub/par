# line publish
import os
import lineTool

# parser
import requests
import json

# database
import os
import sqlite3


## databse setting
dbpath = '/home/heima/Databases/land591.db'

conn = sqlite3.connect(dbpath)
c = conn.cursor()
c.execute('''CREATE TABLE LAND(
	ID 			INT 	PRIMARY KEY NOT NULL,
	DATETIME 	TEXT	NOT NULL,
	SECTION		TEXT 	NOT NULL,
	LANDTYPE	TEXT	NOT NULL,
	AREA 		TEXT 	NOT NULL,
	PRICE 		TEXT 	NOT NULL,
	NOTE		TEXT 	NOT NULL);''')
##

headers = {
	'Cookie':'urlJumpIp=6;',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

url = 'https://business.591.com.tw/home/search/rsList?is_new_list=1&type=2&kind=11&searchtype=1&region=5&firstRow=60&totalRows=629'
res = requests.get(url, headers = headers)
data = json.loads(res.text)

totalRows = res.url.split("totalRows=")[1]

desection = ["平鎮".encode("big5"), "大園".encode("big5"), "新屋".encode("big5"), "龜山".encode("big5"),
 			 "楊梅".encode("big5"), "觀音".encode("big5"), "大溪".encode("big5"), "復興".encode("big5"), "龍潭".encode("big5")]
 			 
delandtype = ["工業".encode("big5"), "商業".encode("big5"), "林地".encode("big5")]

for k in range(0, int(totalRows), 30) :
	url = 'https://business.591.com.tw/home/search/rsList?is_new_list=1&type=2&kind=11&searchtype=1&region=6&firstRow='+str(k)+'&totalRows='+str(totalRows)
	res = requests.get(url, headers = headers)
	data = json.loads(res.text)
	
	datalen = len(data['data']['data'])

	for l in range(0, datalen) :

		cFlag = 0

		landtype = data['data']['data'][l]['layout_str']
		landtype = landtype.split('：')
		landtype = landtype[1].split('</span>')[0]

		if len(landtype) > 2 :
			landtype = landtype[0]+landtype[1]

		for m in range(0, len(delandtype)) :
			if delandtype[m] == landtype.encode("big5") :
				cFlag = 1

		SN = data['data']['data'][l]['sectionname'][0]+data['data']['data'][l]['sectionname'][1]

		for m in range(0, len(desection)) :
			if desection[m] == SN.encode("big5") :
				cFlag = 1

		if cFlag:
			# print('Continue')
			continue

		print(data['data']['data'][l]['post_id'],' ', data['data']['data'][l]['ltime'],' ', data['data']['data'][l]['sectionname'], '\t',
			landtype, data['data']['data'][l]['area'], '\t', data['data']['data'][l]['price'], '\t', data['data']['data'][l]['street_name'])

		c.execute("INSERT INTO LAND(ID, DATETIME, SECTION, LANDTYPE, AREA, PRICE, NOTE) \
			VALUES (?, ?, ?, ?, ?, ?, ?)", 
				(data['data']['data'][l]['post_id'], 
					data['data']['data'][l]['ltime'], 
					data['data']['data'][l]['sectionname'], 
					landtype,
					data['data']['data'][l]['area'],
					data['data']['data'][l]['price'],
					data['data']['data'][l]['street_name']));

conn.commit()
conn.close()
