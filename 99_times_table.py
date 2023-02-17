
# 99乘法表 雙層迴圈

# 直接輸出結果


for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end='\t')  # 二層迴圈內結束前數據不換行 並保留一個tab的距離
    print()  # 二層迴圈結束後換行


# 利用f-string 表達=前字串

"""
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{j}x{i}={i*j}", end='\t')
    print()

"""

# 利用.format 表達=前字串

"""
for i in range(1,10):
    for j in range(1,10):
        print("{}x{}={}".format(j,i,i*j), end='\t')
    print()
"""
