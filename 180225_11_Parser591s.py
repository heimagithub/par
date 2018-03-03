# parser
import requests
import json

# database
import os
import sqlite3

# timer
import time

# line
import lineTool


## databse setting
dbpath = '/home/heima/Databases/land591.db'

if os.path.isfile(dbpath) :
	os.remove(dbpath)

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

headers = {
	'Cookie':'urlJumpIp=6;',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

url = 'https://business.591.com.tw/home/search/rsList?is_new_list=1&type=2&kind=11&searchtype=1&region=5&firstRow=60&totalRows=629'
res = requests.get(url, headers = headers)

totalRows = res.url.split("totalRows=")[1]

desection = ["平鎮".encode("big5"), "大園".encode("big5"), "新屋".encode("big5"), "龜山".encode("big5"),
 			 "楊梅".encode("big5"), "觀音".encode("big5"), "大溪".encode("big5"), "復興".encode("big5"), "龍潭".encode("big5")]
 			 
delandtype = ["工業".encode("big5"), "商業".encode("big5"), "林地".encode("big5")]

IDlist = []
token = "4iiogtVpLF8UbSabgqwabwSbXCn4Y26Zro0S1WR9veT"


while(1) :

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

			# filter out by landtype
			for m in range(0, len(delandtype)) :
				if delandtype[m] == landtype.encode("big5") :
					cFlag = 1

			SN = data['data']['data'][l]['sectionname'][0]+data['data']['data'][l]['sectionname'][1]

			# filter out by section name
			for m in range(0, len(desection)) :
				if desection[m] == SN.encode("big5") :
					cFlag = 1

			if cFlag == 1 :
				continue

			
			# check data is in database or not
			for row in IDlist :
				if(data['data']['data'][l]['post_id'] == row) :
					cFlag = 1

			print(cFlag, data['data']['data'][l]['post_id'],' ', data['data']['data'][l]['ltime'],' ', data['data']['data'][l]['sectionname'], '\t',
				landtype, data['data']['data'][l]['area'], '\t', data['data']['data'][l]['price'], '\t', data['data']['data'][l]['street_name'])

			if cFlag == 1 :
				c.execute(''' 	UPDATE LAND
								SET DATETIME = ?, 
									SECTION = ?, 
									LANDTYPE = ?, 
									AREA = ?, 
									PRICE = ?, 
									NOTE = ?
								WHERE ID = ? ''', 
									(data['data']['data'][l]['ltime'], 
										data['data']['data'][l]['sectionname'], 
										landtype,
										data['data']['data'][l]['area'],
										data['data']['data'][l]['price'],
										data['data']['data'][l]['street_name'],
										data['data']['data'][l]['post_id']))
			else :
				c.execute("INSERT INTO LAND(ID, DATETIME, SECTION, LANDTYPE, AREA, PRICE, NOTE) \
					VALUES (?, ?, ?, ?, ?, ?, ?)", 
						(data['data']['data'][l]['post_id'], 
							data['data']['data'][l]['ltime'], 
							data['data']['data'][l]['sectionname'], 
							landtype,
							data['data']['data'][l]['area'],
							data['data']['data'][l]['price'],
							data['data']['data'][l]['street_name']))

				IDlist.append(data['data']['data'][l]['post_id'])

			conn.commit()

			if(landtype == '農地' and float(data['data']['data'][l]['area']) < 750) :
				continue
			if(landtype == '建地' and float(data['data']['data'][l]['area']) < 50) :
				continue
			if(landtype == '住宅' and float(data['data']['data'][l]['area']) < 50) :
				continue

			price = int(data['data']['data'][l]['price'].replace(',',''))

			if(price > 5000):
				continue

			msg1 = data['data']['data'][l]['sectionname']+ '【'+landtype+'】'
			msg2 = '面積: '+ str(data['data']['data'][l]['area'])
			msg3 = '總價: '+ data['data']['data'][l]['price']+'萬'
			msg4 = '單價: '+ data['data']['data'][l]['perarea_str']
			msg5 = data['data']['data'][l]['address']

			landId = data['data']['data'][l]['houseid']
			msg6 = 'https://sale.591.com.tw/home/house/detail/2/'+str(landId)+'.html'

			msg = "\n"+msg1+"\n"+msg2+"\n"+msg3+"\n"+msg4+"\n"+msg5+"\n"+msg6
			lineTool.lineNotify(token, msg)


	print("Wait 1000 seconds ")
	time.sleep(1000)

conn.close()