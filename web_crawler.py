# 抓取PTT電影版的網頁原始碼(HTML)

import urllib.request as req
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.ptt.cc/bbs/movie/index.html"

# 建立一個request物件,附加Request headers的資訊
request = req.Request(url, headers={
                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})


with req.urlopen(request) as response:
    data = response.read().decode("utf-8")  #decode:將取得的資料從位元組轉成字串並用utf-8解碼處理


import bs4  # 載入解析套件
# 解析原始碼, 取得每篇文章的標題
root = bs4.BeautifulSoup(data, "html.parser")  # 讓Beautifulsoup協助我們解析HTML格式文件

titles = root.find_all("div", class_="title")
# find_all():尋找所有符合class="title" 的div標籤
# 因class為python內建保留字因此在使用find方法時需加入_

count = 0
with open('movie.txt', 'w', encoding=('utf-8')) as file: #為了寫入檔案，需在以encode的方式以utf-8編碼，轉換資料為二進位制儲存
    for title in titles:
        if title.a != None:  # 如果標題包含</a>標籤(沒有被刪除)
            count += 1
            if count != len(titles):
                file.write(title.a.string+'\n')  # 印出具有</a>標籤的標題(類型:string字串)並寫入movie.txt中
            else:
                file.write(title.a.string)
