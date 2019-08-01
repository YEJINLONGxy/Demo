#!/usr/bin/env python3
#求圆的面积
# 能够计算出一个半径为2的圆的面积，并且把面积打印出来，保留小数点后10位。

import math
#计算圆的面积
area = 2 * 2 * math.pi    #math.pi :3.14.......


#格式化输出圆的面积，保留10位小数
print('{:.10f}'.format(area))
