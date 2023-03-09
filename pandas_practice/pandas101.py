# 載入pandas模組
import pandas as pd

# 建立Series
data=pd.Series([20,10,15])

# 基本Series操作
# print(data)
print("Max:",data.max()) #最大值
print("Median:",data.median()) #中位數

data=data*2 
print(data)

data=data==20
print(data)

print('----------------------------------')

# 建立DataFrame
data=pd.DataFrame({
    "name":["Amy","John","Bob"],
    "Salary":[30000,40000,50000]
})

# 基本DataFrame操作
print(data)
print('----------------------------------')
#取得特定的欄位
print(data['name'])
print('----------------------------------')
#取得特定的列
print(data.iloc[0]) #印出第一列