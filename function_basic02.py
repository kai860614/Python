# 參數的預設資料

def power(base, exp=0):  # exp=0 > 未給參數值時使用預設資料
    print(base**exp)  # **為次方


power(3, 2)

# 使用參數名稱對應


def divide(n1, n2):
    print(n1/n2)


divide(2, 4)
divide(n2=3, n1=6)


# 無限/不定參數資料 在參數名稱前加* 表示不限制輸入參數數量，以Tuple形式儲存

# 定義一函式 使之可以計算輸入參數之平均值並印出(使用者自行輸入字串) *

def avg(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    print(sum/len(numbers))

x = eval(input("請輸入數字串: "))  # 讓使用者輸入字串 並用逗號隔開
avg(*x)



# **kwargs : 讓函式接受任何帶有名稱的參數輸入，並存成一個字典

def test(**kwargs):  
    print(kwargs)

test(a=3, b=4, c=5)



def switch_case(value):
	match value:
            case 1:
                print("Case 1")
            case 2:
                print("Case 2")
            case _:
        # 在未匹配到任何 case 時執行的程式碼
                print("Default Case")

# 測試
switch_case(2)
switch_case(4)