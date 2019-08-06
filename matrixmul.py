#!/usr/bin/env python3

#这个例子里我们计算两个矩阵的 Hadamard 乘积。
#要求输入矩阵的行/列数（在这里假设我们使用的是 n × n 的矩阵）。

n = int(input("Enter the value of n: "))
print("Enter value for the Matrix A")
a = []
for i in range(n):
	a.append([int(x) for x in input().split()])

print(a)

print("Enter value for the Matrix B")
b = []
for i in range(n):
	b.append([int(x) for x in input().split()])

print(b)

c = []
for i in range(n):
	c.append([a[i][j] * b[i][j] for j in range(n)])

print(c)
print("after matrix multiplication")

print("-" * 7 * n)
for x in c:
	for y in x:
		print(str(y).rjust(5), end=" ")
	print()
print("-" * 7 * n)

#运行如下

#[root@dev1 python_code]# ./matrixmul.py 
#Enter the value of n: 4
#Enter value for the Matrix A
#1 2 3 4
#5 6 7 8
#9 10 11 12
#13 14 15 16
#[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
#Enter value for the Matrix B
#16 15 14 13
#12 11 10 9
#8 7 6 5
#4 3 2 1
#[[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]
#[[16, 30, 42, 52], [60, 66, 70, 72], [72, 70, 66, 60], [52, 42, 30, 16]]
#after matrix multiplication
#----------------------------
#   16    30    42    52 
#   60    66    70    72 
#   72    70    66    60 
#   52    42    30    16 
#----------------------------


#这里我们使用了几次列表推导式:
#[int(x) for x in input().split()] 首先通过 input() 获得用户输入的字符串
#再使用 split() 分割字符串得到一系列的数字字符串，然后用 int() 从每个数字字符串创建对应的整数值
#我们也使用了 [a[i][j] * b[i][j] for j in range(n)] 来得到矩阵乘积的每一行数据

