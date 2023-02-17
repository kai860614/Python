# Point實體物件的設計：平面座標上的點
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # 定義實體方法

    def show(self):  # self為固定寫法
        print(self.x, self.y)

    def distance(self, targetX, targetY):
        return (((self.x-targetX)**2+(self.y-targetY)**2))**0.5


p = Point(3, 4)  # 建立實體物件並呼叫初始化函式
p.show()  # 呼叫實體方法
result = p.distance(0, 0)  # 計算座標3,4和座標0,0之間的距離
print(result)


# File實體物件的設計：包裝檔案讀取的程式
class File:
    # 初始化函式
    def __init__(self, name):
        self.name = name
        self.file = None  # 尚未開啟檔案：初期是None

    # 定義實體方法
    def open(self):
        # 開啟一個檔案物件放在實體屬性File中
        self.file = open(self.name, mode="r", encoding='utf-8')

    def read(self):
        return self.file.read()  # 讀取檔案物件並回傳


# 讀取第一個檔案
f1 = File("obj-data01.txt")  # 建立實體物件放在f1中
f1.open()  # 呼叫實體方法open
data = f1.read()  # 呼叫實體方法read
print(data)

# 讀取第二個檔案
f2 = File("obj-data02.txt")
f2.open()
data = f2.read()
print(data)
