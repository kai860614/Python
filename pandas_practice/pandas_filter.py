import pandas as pd

#篩選條件
data=pd.Series([30,15,20])
#condition=[True,False,True]
condition=data>18
filterData=data[condition]
print(filterData)
print('--------------------------------')

data=pd.Series(["您好",'Pandas','Python'])
condition=data.str.contains('P') #字串包含P
filterData=data[condition]
print(filterData)
print('--------------------------------')

data=pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000,40000,50000]
}, index=['a','b','c'])

condition=data['salary']>=40000
print(condition)
filterData=data[condition]
print(filterData)