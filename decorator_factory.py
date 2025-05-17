def myFactory(base): #包一個裝飾器在裝飾器工廠裡, 並多了接受參數的功能
    def myDeco(callback):
        def run():
            print('裝飾器內的程式',base)
            result=base*2
            callback(result)
        return run
    return myDeco

@myFactory(5) #裝飾器工廠需要加()因為可以新增額外參數
def test(result):
    print('普通函式內的程式',result)

test()

print('-------------------------------------')

# 計算1+2+3+.....+ max的裝飾器工廠
def calculateFactory(max):
    def calculate(callback):
        def run():
            # 裝飾器想要執行的程式碼
            result=0
            for n in range(max+1):
                result+=n
            #把計算結果透過參數傳到被裝飾的普通函式中
            callback(result)
        return run
    return calculate

@calculateFactory(100) # 1+到100的結果
def show(result):
    print('計算結果是',result)

show()