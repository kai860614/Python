# while 迴圈
# EX 1+2+3+4+...+10 (using while loop)

"""
n=1
sum=0 
while n<=10:
    sum=sum+n
    n+=1
print(sum)
"""


# for 迴圈

# for x in [1,2,3]
# for x in "Hello"
# for x in range(5) # 未定義開頭即從0開始. 列出0 1 2 3 4
# for x in range(5,10) #列出5 6 7 8 9

# EX 1+2+3+4+...+10 (using for loop)

"""
sum=0
for x in range(11):
    sum=sum+x
print(sum)

"""


# EX 1+3+5+7+...+19 (using for loop)

"""
sum2 = 0
a = list(range(1, 20, 2))  # 將等差級數列表出來 a=list(range(start,end,step)
for y in a:
    sum2 = sum2+y
print(sum2)

"""

# EX 移除列表[1,2,3,4,5]的偶數(using for loop)

"""
data = [1, 2, 3, 4, 5]
copyData = data.copy()  # 複製一份相同的列表
x = len(copyData)
for i in range(x):
    if copyData[i] % 2 == 0:
        data.remove(copyData[i])  # 從原本的列表中移除複製列表留下的偶數
print(data)

"""
