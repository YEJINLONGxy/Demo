#!/usr/bin/env python3

import sys

def fact(n):
	"""
	阶乘函数

	:arg n : 数字
	:returns: n 的阶乘

	"""

	if n == 0:
		return 1
	return n * fact(n -1)

#hello=fact()
#print(hello)

def div(n):

	"""
	只是做除法
	"""

	res = 10 / n
	return res


def main(n):
	res = fact(n)
	print(res)


if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(int(sys.argv[1]))


