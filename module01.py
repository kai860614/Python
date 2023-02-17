# 載入內建的sys模組並取得資訊
# import sys # +as 別名 功能相同 ex:import sys as system
# print(sys.platform)
# print(sys.maxsize)


# 建立 geometry模組, 載入使用
import geometry
result = geometry.dis(1, 1, 5, 5)
print(result)
# result=geometry.slope(1,2,5,6)
# print (result)

# 調整搜尋模組的路徑

# Scenario
# 新增一資料夾 並將模組檔案放入新資料夾
# 在模組的搜尋路徑列表中[新增路徑],資料夾名稱:modules
# 若未進行append新增路徑, 在call模組時會因為找不到模組路徑而報錯
# print(sys.path)
# print('---------------------------------------')
# sys.path.append("modules")
# print(sys.path)
