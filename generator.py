# 定義生成器函式
def test():
    print('階段一')
    yield 3
    print('階段二')
    yield 5
# 呼叫並回傳生成器
gen=test()
print (gen)
# 搭配for迴圈使用
for data in gen:
    print(data)
print('----------------------------------')
def generateEven(maxnumber):
    number=0
    while number<=maxnumber:
        yield number
        number+=2
        
evenGenerator=generateEven(10)

for data in evenGenerator:
    print(data)