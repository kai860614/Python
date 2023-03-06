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
numbers = [1, 2, 3, 4, 5]
odds = []
for num in numbers:
    if num % 2 != 0:
        odds.append(num)
print(odds)

"""


# EX 1+2+4+7+11+16

#印出陣列
sum=1
a=[]
for i in range(6):
    sum+=i
    a.append(sum) #將新增的值加進陣列最後

#求陣列總和
sum2=0
for j in a:
    sum2+=j
print(sum2)

#求陣列中的第n個數的值
x=int(input("第幾個數："))
x=1+(((1+(x-1))*(x-1))/2)
print(x)
