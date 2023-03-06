
#引用geometry封包內的模組 封包名稱.模組名稱
import Geometry.point

#使用模組內的程式
result=Geometry.point.distance(3,4)
print("距離:" ,result)

import Geometry.line
result=Geometry.line.slope(1,1,3,3)
print("斜率:" ,result)