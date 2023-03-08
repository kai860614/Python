# 網路連線
import urllib.request as request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context  # Mac需加入的ssl憑證驗證

src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"

import json # 因此API為Json格式, 因此需Import Json即以Json的形式讀取
with request.urlopen(src) as response:
    data = json.load(response)  

# 將公司名稱列表出來
# 從API return得知我們所需的資料在列表「result」下的「results」中
clist = data["result"]["results"]


# 將搜集的公司名稱寫入一名為“companydata.txt”的檔案中並換行
count = 0
with open("companydata.txt", 'w', encoding=('utf-8')) as file:
    for company in clist:
        count += 1
        if count != len(clist):
            file.write(company["公司名稱"]+"\n")
        else:
            file.write(company["公司名稱"])  # 當此公司為最後一行不時加入換行
