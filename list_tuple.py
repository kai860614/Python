#List 有序可變動列表 使用中跨號

grades=[12,13,14,15,16]
grades[1:4]=[] #連續刪除列表中從編號1到4(不包括)的資料 
#grades=grades+[17,18] #在列表最後方直接加入新資料
print(grades)


data=[3,4,5],[6,7,8]
print(data)
data[0][0:2]=[5,5,5]
print(data)

test=["A","E"]
test2=['b','c','d']

test[1:1]=test2
print(test)

#Tuple 有序不可變動列表 使用小跨號

data2=(4,5,6)
data2[0]=1 #報錯 Tuple資料不可改動
print(data2)
