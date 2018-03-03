import requests
import json

from lxml import html

# headers = {
# 	'Cookie':'urlJumpIp=6;',
# 	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
# }

# url = 'https://business.591.com.tw/home/search/rsList?is_new_list=1&type=2&kind=11&searchtype=1&region=6&firstRow=60&totalRows=640'

# res = requests.get(url, headers = headers)

# data = json.loads(res.text)

# print(data['data']['data'][0])
data = {
'addition3': 0,
'living': '',
'isvip': 0,
'updatetime': 1519613803,
'hasimg': 1, 
'vipBorder': '', 
'addInfo': '', 
'closed': 0, 
'icon_name': '出售', 
'addition2': 0, 
'address': '富國路一段富國路收租農地', 
'refreshtime': 1519614002, 
'address_img_title': '富國路收租農地', 
'housetype': 3, 
'regionid': 6, 
'floor2': 0, 
'browsenum_all': 0, 
'cases_name': '', 
'allfloor': 0, 
'fci_time': '', 
'groundarea': 0, 
'sectionid': 79, 
'browsenum': 0, 
'posttime': '6分鐘內', 
'price_hide': 'price-hide', 
'section_name': '蘆竹區', 
'vipstyle': '', 
'kind': 11, 
'linkman': '住商不動產', 
'shape': 0, 
'post_id': 4839065, 
'discounted_unit': '', 
'streetid': 15035, 
'floor': 0, 
'filename': 'https://hp2.591.com.tw/house/active/2017/03/15/148955839121139201_210x158.crop.jpg', 
'room': 0, 
'new_img': '<div class="isNew"></div>', 
'fulladdress': '富國路一段富國路收租農地', 
'browsenum_name': '總瀏覽', 
'groundarea_str': '', 
'regionname': '桃園市', 
'icon_class': 'sell', 
'layout_str': '<span class="layout">類別：農地</span>', 
'discounted': None, 
'house_img': '104832484,104832485,104832486,104832487,104832488,104832489,', 
'id': 4839065, 
'balcony_area': 0, 
'kind_name_img': '土地', 
'nick_name': '仲介 住商不動產', 
'houseimg': None, 
'sectionname': '蘆竹區', 
'type': '2', 
'approve_pass': '<a href="http://www.591.com.tw/message-212.html" class="approve_pass" target="_blank" title="已通過仲介職業認證" data-stat="list_approve_pass">已認證</a>', 
'kind_name': '土地', 
'region_name': '桃園市', 
'ltime': '2018-02-26 11:00:44', 
'cover': 'https://hp2.591.com.tw/house/active/2017/03/15/148955839121139201_210x158.crop.jpg', 
'cartplace': '', 
'alley_name': '', 
'new_list_comment_total': 0, 
'floorInfo': '', 
'checkstatus': 0, 
'onepxImg': '', 
'mainarea_str': '', 
'mainarea': 0, 
'storeprice': 0, 
'mvip': 0, 
'houseid': 4839065, 
'user_id': 1213933, 
'status': '', 
'vipimg': '', 
'houseage': 0, 
'comment_unread': 0, 
'addition4': 0, 
'addr_number_name': '', 
'discounted_ico': '', 
'old_price': None, 
'cases_id': 0, 
'perarea_str': '單價：34.52萬元', 
'photo_alt': '桃園買屋,蘆竹買房子,土地出售,富國路收租農地', 
'unit': '萬元', 
'layout': '類別：農地', 
'address_img': '富國路收租農地', 
'distance': 0, 
'search_name': '', 
'lane_name': '', 
'street_name': '富國路一段', 
'saletype': 0, 
'area_name': '總坪數：', 
'area': 25.5, 
'comment_total': 0, 
'is_combine': 0, 
'price': '880', 
'condition': 'balcony_1', 
'comment_ltime': 0, 
'space_type_str': '', 
'comment_class': 'none', 
'photoNum': '6'}

# for k in range(0, len(data['data']['data'])) :
# 	landtype = data['data']['data'][k]['layout_str']
# 	landtype = landtype.split('：')
# 	landtype = landtype[1].split('</span>')[0]

# 	if len(landtype) > 2 :
# 		landtype = landtype[0]+landtype[1]

# 	print(landtype)

# print(data['data']['data'][0])

landtype = data['layout_str']
landtype = landtype.split('：')
landtype = landtype[1].split('</span>')[0]
print(data['sectionname'], '【', landtype, '】')
print('類別: ', data['area'])
print('總價: ', data['price'],'萬')
print('單價: ', data['perarea_str'] )
print(data['address'])