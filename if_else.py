# 輸入一個數來確定此數介於0-200之間的哪個區間


x = input("請輸入一個數字")
x = int(x)
if x > 200:
    print("大於200")
elif (x > 100):
    print("大於100,小於等於200")
else:
    print("小於等於100")


# 四則運算 輸入兩個數及運算符號進行運算並輸出答案

"""
n1 = int(input("請輸入第一個數 : "))
n2 = int(input("請輸入第二個數 : "))
op = input("請輸入運算+,-,*,/ : ")

if op == '+':
    print(n1+n2)
elif op == '-':
    print(n1-n2)
elif op == '*':
    print(n1*n2)
elif op == '/':
    print(n1/n2)
else:
    print('不支援的運算法則')
"""