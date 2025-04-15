# 載入內建的sys模組並取得資訊
import sys # +as 別名 功能相同 ex:import sys as system
# print(sys.platform)
# print(sys.maxsize)


# Scenario
# 新增一資料夾 並將模組檔案放入新資料夾
# 在模組的搜尋路徑列表中[新增路徑],資料夾名稱:modules
# 若未進行append新增路徑, 在call模組時會因為找不到模組路徑而報錯
sys.path.append("modules")

# 建立 geometry模組, 載入使用
import geometry
print(geometry.distance(1, 1, 5, 5))
print(geometry.slope(1,2,5,6))

print(sys.path)#印出模組的搜尋路徑列表
