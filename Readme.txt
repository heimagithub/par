- 180222_par591.py
  爬591 雛型版

- 180223_OLParser591.py
  爬591 排版

- 180224_linenot.py
  測試 line推送訊息
  參考：http://pythonorz.blogspot.tw/2017/12/python-line-notify-line-notify-line.html 

- 180225_1_Parser591s.py
  直接用 requests 直接爬 失敗

- 180225_2_Parser591s.py
  參考：https://www.youtube.com/watch?v=jV6eHoLzD2E
  加入 headers 成功抓取

- 180225_3_Parser591s.py
  轉 JSON

- 180225_4_Parser591s.py
  調閱資料內容

- 180225_5_Parser591s.py
  加入 cookie 爬特定區域

- 180225_6_Parser591s.py
  調閱資料內容及型態

- 180225_7_Parser591s.py
  儲存一筆土地資料 離線測試

- 180225_8_Parser591s.py
  儲存一筆土地資料 離線測試 並且透過 LINE NOTIFY 推送  

- 180225_9_Parser591s.py
  線上爬取 並且濾掉不合意的案件

- 180225_10_Parser591s.py
  爬取所有頁面案件 並且儲存再資料庫中 sqlite

- 180226_Example.py
  一筆土地範例資料

- 180227_1_sqlite.py
  python 連線資料庫

- 180227_2_sqlite.py
  python 創建資料庫

- 180227_3_sqlite.py
  儲存一筆土地資料到資料庫中

- 180227_datetime.py
  python 時間資料格式測試

- 180227_ParYoutube.py
  python 爬取 youtube 影片 失敗
  但是可以從中學習到 程式設計方法
  
- downYB.py
  利用 pytube 套件抓取視頻
  參考：https://www.youtube.com/watch?v=uSosZCcLr_U
  注意 pytube 版本(sudo pip3 install pytube==6.4.2)

- 180227_4_sqlite_cr.py
  建一個新的DB 並給予兩比資料

- 180227_5_sqlite_up.py
  更新DB 

- 180227_6_sqlite_del.py
  刪除DB 

- 180228_MainSq.py
  參考：http://www.sqlitetutorial.net/sqlite-python/update/
  主副程式 SQLITE 寫法

- 180225_11_Parser591s.py
  爬所有頁面的案子 
  不考慮 工商業和林地 另外只考慮 盧竹桃園八德區域 加入資料庫
  濾掉面積太小的選項 發送賴 到群組

  BUGs:
  requests get 失敗 造成程式中斷  

- 180225_12_Parser591s.py
  updata 一筆土地案子
