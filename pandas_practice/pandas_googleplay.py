import pandas as pd

#讀取資料
data=pd.read_csv("googleplaystore.csv") #把CSV格式的檔案讀成一個DataFrame
#觀察資料
print('資料型態:', data.shape)
print('資料欄位:', data.columns)
#分析資料
print('評分:\n',data['Rating'])
print('取得一百個最高評分的應用程式的平均:',data['Rating'].nlargest(100).mean())

#平均大於5不合理，建立篩選條件
condition=data['Rating']<=5
data=data[condition]
print('取得一千個最高評分的應用程式的平均:',data['Rating'].nlargest(1000).mean())
print('------------------------------------------------')

#分析資料延伸
#將Installs中的字串，包含逗號與加號，以及不為數字的部分都轉為空值，並藉由to_numeric轉換為數字
data['Installs']=pd.to_numeric(data['Installs'].str.replace('[,+]','',regex=True).replace('Free',''))
print('安裝數量的平均數：',data['Installs'].mean())
#加入篩選條件
condition=data['Installs']>10000
print('安裝數量大於10000的應用程式有幾個:', data[condition].shape[0]) #shape[0]為僅列出有幾列,不加[0]會同時列出有幾欄 
print('------------------------------------------------')

#基於資料的運用：關鍵字搜尋
keyword=input('請輸入關鍵字:')
condition=data['App'].str.contains(keyword, case=False) #case=False 忽略大小寫
print('包含關鍵字的應用程式數量:',data[condition].shape[0])