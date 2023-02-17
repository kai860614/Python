# 隨機模組
import statistics as stat
import random

# 隨機選取

data = random.choice([1, 5, 7, 10, 13])  # choice : 從列表中隨機選取一個數
print(data)

data = random.sample([1, 5, 7, 10, 13], 3)  # sample : 從列表中隨機選取指定個數的值
print(data)

data = [1, 5, 8, 20]
random.shuffle(data)  # shuffle : 隨機變換順序
print(data)

print('-------------------------------')

data = random.random()  # only 0~1之間的隨機亂數
print(data)
# same as uniform
# but uniform可控制區間, ex : (60,100) 即為60到100之間
data = random.uniform(0, 100)
print(data)

data = random.randint(1, 100)  # 隨機選出1~100之間的整數
print(data)

# 取得常態分配亂數
# 平均數100, 標準差10, 得到的資料『多數』在90~110之間
data = random.normalvariate(100, 10)
print(data)

print('-------------------------------')

# 在1~100中隨機抽取5個數字

"""
result = []
count = 0
while count < 5:
    data = random.randint(1, 100)
    result.append(data)
    count += 1
print(result)

"""


# 統計模組

data = stat.mean([1, 2, 3, 4, 5])  # mean :取得平均值
print(data)

data = stat.median([1, 2, 3, 4, 5])  # median :取得中位數
print(data)

data = stat.stdev([1, 2, 3, 4, 5])  # stdev :取得標準差
print(data)
