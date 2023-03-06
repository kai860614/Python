
#引用geometry封包內的模組 封包名稱.模組名稱
import geometries.point

#使用模組內的程式
result=geometries.point.distance(3,4)
print("距離:" ,result)

import geometries.line
result=geometries.line.slope(1,1,3,3)
print("斜率:" ,result)