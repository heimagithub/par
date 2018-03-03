from linebot import LineBotApi
from linebot.models import TextSendMessage

line_bot_api = LineBotApi('iXe5fhFI3HLydVkgV38QOzSnajYT3DdDQ09cWq1wTS2Pfi/5TztSuNGkKgGlki1QsjllM9aR1mR7ncVQktbSO/AjQU6kT0WrOhZEwIOGJtTVJKymGu7i4lrcIGfr+Z3qye84LMcuvsjnGAyzbP2DyQdB04t89/1O/w1cDnyilFU=')
#push message to one user

for i in range(1,1001) :
	str1 = str(i) 	
	line_bot_api.push_message('U6b4429deb4218fa43ebfd82580270ec6', TextSendMessage(text=str1))

#push message to multiple users
# line_bot_api.multicast(['user_id1', 'user_id2'], 
#     TextSendMessage(text='Hello World!'))