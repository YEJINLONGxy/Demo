#!/usr/bin/env python3


#在 Python 里我们使用文档字符串（docstrings）来说明如何使用代码，
#这在交互模式非常有用，也能用于自动创建文档。下面我们来看看使用文档字符串的例子。

import math

def longest_side(a, b):
	"""
	Function to find the length of the longest side of a right triangle.
	
	:arg a: Side a of the triangle
	:arg b: Side b of the triangle

	:return: Length of the longest side c as float
	"""
	return math.sqrt(a*a + b*b)


if __name__ == "__main__":
	print(longest_side.__doc__)
	print(longest_side(4,5))


#运行程序：
#[root@dev1 python_code]# ./DocumentationString.py 
#
#	Function to find the length of the longest side of a right triangle.
#	
#	:arg a: Side a of the triangle
#	:arg b: Side b of the triangle
#
#	:return: Length of the longest side c as float
#	
#6.4031242374328485
#





