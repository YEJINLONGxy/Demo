#!/usr/bin/env python3

#局域或全局变量
#函数内使用 global 会有什么作用呢？
#尝试下面代码

def change():
	global a
	a = 90
	print(a)
a = 9
print("Before the function call ", a)
print("inside change function ", end=" ")
change()
print("After the function call ", a)

#程序执行的结果:
#
#[root@dev1 python_code]# ./global2.py 
#Before the function call  9
#inside change function  90
#After the function call  90
#
#这里通过关键字 global 来告诉 a 的定义是全局的，
#因此在函数内部更改了 a 的值，函数外 a 的值也实际上更改了




