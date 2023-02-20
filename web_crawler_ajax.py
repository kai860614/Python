# 使用ajax技術的網頁時瀏覽器會發送兩次請求給伺服器
# 第一次請求：伺服器回傳不帶資料的HTML網頁給瀏覽器
# 第二次請求：瀏覽器取得資料並產生網頁畫面

# 抓取Medium.com的文章資料

import urllib.request as req
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.kkday.com/zh-tw/home/ajax_get_homepage_setting?csrf_token_name=6ff99eab12b865e3421a34084fdc41ee"

# 建立一個request物件,附加Request headers的資訊
request = req.Request(url, headers={
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8") #根據觀察，取得的資料為json格式

# 解析json格式
import json
# 把原始的json資料解析成字典/列表的表示形式
data=json.loads(data) #json.load"s":字串 / json.load:檔案物件


posts=data["data"]["top_products"]["prod_list"] 
for key in posts:
    print(key["name"])
    

"""
count = 0
with open('movie.txt', 'w', encoding=('utf-8')) as file:
    for title in titles:
        if title.a != None:  # 如果標題包含</a>標籤(沒有被刪除)
            count += 1
            if count != len(titles):
                # 印出具有</a>標籤的標題(類型:string字串)並寫入movie.txt中
                file.write(title.a.string+'\n')
            else:
                file.write(title.a.string)
"""

