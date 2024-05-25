import pandas as pd

data=pd.DataFrame({
    'Month':['January','Febuary','March','April','May'],
    'Salary':[30000,40000,None,60000,None]
},
index=['A','A','A','A','A']
)

data.to_excel('monthly_paid.xlsx')

df=pd.read_excel('monthly_paid.xlsx',index_col=0)
df.fillna('N/A',inplace=True)
print(df)