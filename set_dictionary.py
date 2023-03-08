# 集合的運算 使用大跨號

s1 = {3, 4, 5}
print(3 in s1)
# 也可以用not in判斷
# 存在集合中=True 反之=False


s1 = {3, 4, 5}
s2 = {4, 5, 6, 7}


s3 = s1&s2  # 交集 : 取兩個集合中，相同的資料
s4 = s1|s2  # 聯集 : 取兩個集合中的所有資料，但不重複取
s5 = s1-s2  # 差集 : 從s1中,減去和s2重疊的部分
s6 = s1^s2  # 反交集 : 取兩個集合中，不重疊的部分
print(s3)
print(s4)
print(s5)
print(s6)


s = set('Hello')  # set(字串) 將字串文字個別拆解成集合(不重覆, 不照順序)
print(s)


# 字典的運算 : key-value配對 使用大誇號

dic = {"apple": "蘋果", "bug": "蟲蟲"}  # key : value
dic["apple"] = "小蘋果"  # 更改key中對應的value
print(dic["apple"])
print("apple" in dic)  # 判斷key值是否存在
# del dic["apple"] #刪除字典中的鍵值對(key-value pair)

dic2 = {x: x*2 for x in [3, 4, 5]}  # 從列表的資料產生字典
print(dic2)


# 結合兩列表為一字典
# a=[1,2,3,4,5] 為key
# b=[5,10,15,20,25] 為value

"""
a = [1, 2, 3, 4, 5]
b = [5, 10, 15, 20, 25]
dic3 = dict(zip(a, b))
print(dic3)

"""
