import pandas as pd

# 建立DataFrame
# 處理二維資料 ex:excel

#由list所組成的dict建立DataFrame
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
print('----------------------------------')

data2=pd.DataFrame({
    #每個 key 的 list 數量必須一致，否則會出現錯誤。 因此若該欄位沒有資料時，需自行補上 nan 的值，可以填入 None 來生成 nan 值。
    "name":["Amy","John","Bob",None],
    "Salary":[30000,40000,50000,60000]
})

print(data2)

print('----------------------------------')

#由dict所組成的list建立DataFrame
data3 = [
        {'a': 1, 'b': 2, 'c': 3}, 
        {'a': 4, 'b': 5, 'c': 6, 'd': 7}
       ]

print("--- DataFrame 1 ---")
df = pd.DataFrame(data3)
# 第一列的資料，缺了 'd' 的值，會補為 nan
# nan 的型別為 float，而其他列的同行的型別為 int
# 由於"同行的型別必須一致"，會取用 int 和 float 相容的型別，因此同行的值都會變為 float。
print(df)

print("--- DataFrame 2 ---")
# index 為列標籤，預設是流水號 0, 1, 2...
# columns 為行標籤，可定義讀取哪些行資料，也決定顯示的順序
df2 = pd.DataFrame(data3, index=['first', 'second'], columns=['d', 'b', 'a'])
print(df2)


print('----------------------------------')


#透過Pandas可以應用 DataFrame 生成 Excel File
#應用 Pandas 處理 Excel 的資料時，Openpyxl 套件會被 Pandas 應用
#因此無須 Import Openpyxl，也能作 Excel 的處理

# 以 list 組成 dict 來建 DataFrame 資料，並給予行標籤 (index)
score_df = pd.DataFrame(
    {
        "Reading": [80, 88, 92, 81, 75],
        "Listening": [75, 86, 85, 88, 80],
        "Speaking": [80, 90, 92, 80, 78],
        "Writing": [80, 95, 98, 82, 80]
    },
    index=["Student A", "Student B",  "Student C", "Student D", "Student E"]
)

# 把 DataFrame 生成 Excel 檔案
score_df.to_excel("score_table.xlsx")

#讀取 Excel 的資料，想要根據各分卷的權重來計算每位學生的成績。
#index_col=0：讓終端不會顯示Unnamed:0的列
df = pd.read_excel('score_table.xlsx',index_col=0)

# 讀取每一行的 index 和 row 資料
# 使用iterrows()來遍歷 score_df DataFrame 的每一行
for index, row in score_df.iterrows():
    score = row["Reading"] * 0.2 + row['Listening'] * 0.25 + row['Speaking'] * 0.3 + row['Writing'] * 0.25

    print(f"{index}: {score}")

#讀取 Excel 檔案，蠻常遇到儲存格的資料為空值，在 Python 讀取的時候會取得 nan 的數值。
#針對 DataFrame 內的 nan 值可以作置換 :

# 把 DataFrame 內所有 nan 值換成數值 0，並生成一個新的 DataFrame
new_df = df.fillna(0)
print(new_df)

# 把 DataFrame 內所有 nan 值換成字串 N/A
# 應用 inplace=True 是直接更換原有的 DataFrame，不會生成新的
df.fillna("N/A", inplace=True)
print(df)


