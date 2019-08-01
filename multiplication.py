#!/usr/bin/env python3

#打印 10 以内的乘法表

i = 1
print("-" * 50)
while i < 11:
	n = 1
	while n <= 10:
		if n <= i :
			print("{} * {} = {}".format(i, n, i * n), end=" ")
			#print("{:5d}".format(i * n), end=" ")
		n += 1
	print() #换行
	i += 1

#字符串若是乘上整数 n，将返回由 n 个此字符串拼接起来的新字符串。
print("-" * 50)

#这里我们在 while 循环里使用了另一个 while 循环，这被称为嵌套循环
