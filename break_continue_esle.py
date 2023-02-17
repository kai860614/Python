# break 停止
# EX n從0開始, 當=3時break

n = 0
while n < 5:
    if n == 3:
        break
    print(n)  # 印出迴圈中的n
    n += 1
print("最後的n:", n)  # 印出迴圈結束後的n值

# continue 直接跳過進下一圈
# EX n從0開始, 當n可被2整除時(偶數), continue

n = 0
for x in [0, 1, 2, 3]:
    if x % 2 == 0:
        continue
    print(x)
    n += 1
print("最後的n:", n)

# else 常與break去做搭配

sum = 0
for x in range(11):
    sum += x
else:
    print(sum)


# EX 找出整數平方根
# 輸入9 得到3
# 輸入11 得到沒有整數的平方根


"""

n = int(input("請輸入一個正整數: "))
for x in range(n+1):  # x 從 0 ~ n, 選擇n+1才可以算出1的平方根
    if x*x == n:
        print("整數平方根為", x)
        break  # 透過break結束迴圈時, 就不會執行else區塊
else:
    print("沒有整數的平方根")

"""
