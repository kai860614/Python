#載入pandas模組
import pandas as pd

#資料索引
data=pd.Series([5,4,-2,3,7],index=['a','b','c','d','e']) #index:自訂索引
#print(data)
#觀察資料
print('資料型態:',data.dtype)
print('資料數量:',data.size)
print('資料索引:',data.index)

print('---------------------')
#取得資料：根據順序、根據索引
print(data[2])
print(data["e"])

print('---------------------')
#數字運算：基本、統計、順序
print("最大值：",data.max())
print("總和：",data.sum())
print('標準差：',data.std())
print('中位數：',data.median())
print("最大的三個數：\n",data.nlargest(3)) #最小的三個數：nsmallest

print('---------------------')
#字串運算：基本、串接、搜尋、取代
data2=pd.Series(["您好","Python",'Pandas'])

print(data2.str.lower()) #lower:全部變小寫 / upper:全部變大寫
print(data2.str.len()) #len:字串長度
print(data2.str.cat(sep=",")) #sep=""：把字串串起來，可以自訂串接的符號
print(data2.str.contains("P")) #contains:判斷每個字串是否包含特定的字元
print(data2.str.replace("您好","Hello")) #replace:取代A值為B值