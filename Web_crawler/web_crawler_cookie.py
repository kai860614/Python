# 抓取PTT八卦版的網頁原始碼(HTML)
# 在進入八卦版前有18禁限制的頁面，因此需要加入cookie

import urllib.request as req
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def getData(url):

    # 建立一個request物件,附加Request headers的資訊
    request = req.Request(url, headers={
        "cookie": "over18=1",  # 新增是否滿18禁檢查頁面的cookie
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})


    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    # 解析原始碼, 取得每篇文章的標題
    import bs4  # 載入解析套件
    root = bs4.BeautifulSoup(data, "html.parser")  # 讓Beautifulsoup協助我們解析HTML格式文件

    titles = root.find_all("div", class_="title")
    # find_all():尋找所有符合class="title" 的div標籤
    # 因class為python內建保留字因此在使用find方法時需加入_

    for title in titles:
        if title.a != None:  # 如果標題包含</a>標籤(沒有被刪除)
            print(title.a.string)
    
    #抓取上一頁的連結
    nextLink=root.find("a", string="‹ 上頁") #找到內文是‹ 上頁的a標籤
    return nextLink["href"] #使用return使呼叫函式時能夠回傳上一頁的連結

#主程序：抓取多個頁面的標題    
pageURL = "https://www.ptt.cc/bbs/Gossiping/index.html"#首頁的網址
count=0
while count < 5: #抓取前五頁的標題
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1