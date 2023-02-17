# 定義函式
def multiply(a, b):
    print(a*b)
    return  # 回傳值 後面沒東西就是回傳None
    # return (10) #回傳10
    # return (a*b)  # 回傳a*b


# 呼叫函式
value = multiply(6, 5)
print(value)

# 函式可用來做程式的包裝 : 同樣的邏輯可以重複利用

# 定義一函式 使之可以計算1到10的總合 & 1到20的總和 *


def calculate(max):
    sum = 0
    for n in range(1, max+1):
        sum += n
    print(sum)


calculate(10)
calculate(20)
