# 在geometry模組中定義幾何運算功能

# 計算兩個點的距離
def dis(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5  # 公式 不用背

# 計算線段的斜率


def slo(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)  # 公式 不用背
