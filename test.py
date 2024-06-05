
# 1,2,3,5,8,13,21,34

numbers = [1, 2]  # 初始化前兩個元素

for n in range(6):  # 後續的6個元素
    next_number = numbers[-1] + numbers[-2]  # 計算下一個費氏數
    numbers.append(next_number)  # 將下一個數添加到數列中

print(numbers)  # 輸出完整的費氏數列
