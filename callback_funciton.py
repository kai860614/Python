def test(arg):
    arg() #呼叫回呼函式(handle)

#定義一個回呼函式
def handle():
    print(100)

test(handle)


print('----------------------')

def add(n1,n2,test):
    test(n1+n2)

def handle(result):
    print('結果是：',result)

add(3,4,handle)