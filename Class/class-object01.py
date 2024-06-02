# Point 實體物件的設計：平面座標上的點
class Point:
    def __init__(self):  # 初始化函式固定寫法
        self.x = 3
        self.y = 4


p1 = Point()  # 透過初始化函式產生點的實體物件放到變數p1中
print(p1.x, p1.y)  # 操作實體物件的屬性  實體物件.屬性名稱


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(3, 4)  # 對應至函式中的x,y
print(p1.x, p1.y)
p2 = Point(5, 6)
print(p2.x, p2.y)


# FullName 實體物件的設計：分開紀錄姓,名資料的全名

class FullName:
    def __init__(self, first, last):
        self.first = first
        self.last = last


name1 = FullName('Y.K.', 'Huang')
print(name1.first, name1.last)
name2 = FullName('T.Y.', 'Lin')
print(name2.first, name2.last)
