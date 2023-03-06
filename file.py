# 儲存檔案

file = open('data.txt', mode='w')  # 開啟
# 'r':讀取 'w':寫入 'r+':讀寫
# 如要寫入中文資料, 可在mode後加入, encoding:"utf-8"
file.write('Hello File')  # 操作
file.close()  # 關閉


# 較好的寫法 讀寫後自動關閉檔案

"""
with open("data.txt", mode='w', encoding='utf-8') as file:
    file.write("測試中文\n好棒棒")
"""


# 讀取檔案


with open("data.txt", mode='r', encoding='utf-8') as file:
    data = file.read()
print(data)


# 把檔案中的數字資料, 一行一行的讀取出來, 並計算總合


with open("data.txt", mode='w', encoding='utf-8') as file:
    file.write("10\n20")

sum = 0
with open("data.txt", mode='r', encoding='utf-8') as file:
    for x in file:
        sum += int(x)  # 將資料中讀取的字串型態轉變為int
    print(sum)


# 使用Json格式讀取 寫入檔案
# 從檔案中讀取json資料, 放入變數data中

import json

with open("config.json", mode='r') as file:

    """
    data = json.load(file)
    """

print(data)  # data 是一個字典資料
print("name:", data["name"])
print("version:", data["version"])


data["name"] = "New name"  # 修改變數中的資料
# 把最新的資料複寫回檔案中
with open("config.json", mode='w') as file:

    """
     json.dump(data, file)
    """
