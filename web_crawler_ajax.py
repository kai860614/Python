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
"authority": "www.kkday.com",
"method": "GET",
"path": "/zh-tw/home/ajax_get_homepage_setting?csrf_token_name=0bd38f235825379f18e12fff1ecd5a4e",
"scheme": "https",
"accept": "application/json, text/javascript, */*; q=0.01",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
"cookie": "country_lang=zh-tw; currency=TWD; KKUD=4016abd1b8963ac621057af02ff177af; _gcl_au=1.1.623031411.1676723809; __lt__cid=3bbc8d44-121d-47ef-910b-45872b4774ab; rskxRunCookie=0; rCookie=hlagy0nxkxaoca01qk2ui9le9y2crq; adid=167672381117238; _hjSessionUser_628088=eyJpZCI6ImIxMjkwODUxLTRmNDMtNWU0MC05Yjg1LTcyYjc2NzAyODE5MSIsImNyZWF0ZWQiOjE2NzY3MjM4MDk5MjYsImV4aXN0aW5nIjp0cnVlfQ==; CookieConsent={stamp:%27wamIzgGAGf3DDLxqcs9aD+RaQW9QUjDststADSuNhaoHyL1GOCYHow==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:1%2Cutc:1676879904933%2Cregion:%27tw%27}; _gid=GA1.2.426419451.1677048489; __lt__sid=258c533c-f4fae7e1; _hjIncludedInSessionSample_628088=0; _hjSession_628088=eyJpZCI6ImQzZjM0NDJjLTdkZTgtNGUxMS1hNDVhLTEyMTc0YmMyMGI3OCIsImNyZWF0ZWQiOjE2NzcwNDg0ODkxOTksImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; csrf_cookie_name=0bd38f235825379f18e12fff1ecd5a4e; KKWEB=a%3A4%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2240d6f3632c3e7b33301ce273c54d11c1%22%3Bs%3A7%3A%22channel%22%3Bs%3A5%3A%22GUEST%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1677048488%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D0ae9353313ceb9ce9e369538111954cd; _ga=GA1.2.1346640872.1676723809; _uetsid=ded230f0b27c11ed9cd491a2387b8995; _uetvid=ea856150af8811edbabdaff4f4c3cc52; lastRskxRun=1677048855226; cto_bundle=Htht9F90UGlaTVpCU3ZEbFlEbkRKT2ltbmpOSU1paU9PN3BhSXd3dU42SHF1R1p4d2RpaHN5WHJEellCJTJCdGJieXptaFg4RjZsaCUyRmpCRUZFUiUyQmlWR3FqcnA5MkZBTFFQaUVIVU9JVVhMTlVJM2ZVMWhaclR6VXYlMkJQM3Q1YnBnMkxSSGlJQyUyRng1TDlrUUtSME9pZjk0MHhMWHRCYkt0MEI0aHNGbSUyRkxqcW9IeE5ja05mU01wNEpjaU8lMkIwQzJFNnlvdVhyUQ; datadome=7Gx_Eg8Sph4Iidaqmya1EZh0DSFYPc0U057VAuwwLZ7qWINQsMEyVYmQk9~ps6iEVjgOe0ss~6EAWoLKjlD9SfzQrT7Etjj34qrAd6jKkSTTNAqjP3VK3lZwYiuZlkpZ; _ga_RJJY5WQFKP=GS1.1.1677048489.4.1.1677049611.60.0.0; mp_b8150a8ddf736c19fdc0f146b9ffac24_mixpanel=%7B%22distinct_id%22%3A%20%221866486e9df1c2d-048aaabaa52fa3-16525635-13c680-1866486e9e01629%22%2C%22%24device_id%22%3A%20%221866486e9df1c2d-048aaabaa52fa3-16525635-13c680-1866486e9e01629%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22Platform%22%3A%20%22www.kkday.com%22%2C%22LoginChannel%22%3A%20%22NO%22%2C%22DisplayCurrency%22%3A%20%22TWD%22%2C%22DisplayLang%22%3A%20%22zh-tw%22%2C%22DisplayCountry%22%3A%20%22TW%22%2C%22Cid%22%3A%20%22%22%2C%22Ud1%22%3A%20%22%22%2C%22Ud2%22%3A%20%22%22%2C%22Tier%22%3A%20null%2C%22MemberUuid%22%3A%20%22%22%2C%22Kkud%22%3A%20%224016abd1b8963ac621057af02ff177af%22%7D; _dd_s=rum=2&id=b0ebd942-a4b1-49df-8443-cb33df637a8b&created=1677048488558&expire=1677050512232",
"referer": "https://www.kkday.com/zh-tw",
"sec-ch-ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform" : "\"macOS\"",
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
"x-requested-with": "XMLHttpRequest"
})

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

