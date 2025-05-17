# Iterable 可疊代的資料型態
# 字串 列表 集合 字典

# for迴圈
# for 變數名稱 in 可疊代的資料
dic={'a':3,'b':5}

for key in dic:
    print(key)
    print(dic[key])

# 內建函式
# max(可疊代資料)
result=max([10,2,5])
print(result)
result=max('afd')
print(result)
result=max({11,3,7})
print(result)
result=max({'a':3,'z':5})
print(result) #印出key值

# # sorted(可疊代資料
result=sorted([10,2,5])
print(result)
result=sorted('dzg')
print(result)
result=sorted({11,3,95,-2})
print(result)
result=sorted({'z':3,'a':5})
print(result)