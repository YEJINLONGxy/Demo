#!/usr/bin/env python3

#局域或全局变量
#使用 global 关键字，对函数中的 a 标志为全局变量，让函数内部使用全局变量的 a

a = 9
def change():
	global a
	print(a)
	a = 100

print("Before the function call", a)
print("inside change function", end=" ")
change()
print("After the function call ", a)

#程序中的 end=' ' 参数表示，print 打印后的结尾不用换行，而用空格。
#默认情况下 print 打印后会在结尾换行。
#
#程序执行的结果，不会报错了，因为函数体内可以访问全局的变量 a：

#运行代码：
#[root@dev1 python_code]# ./global.py 
#Before the function call 9
#inside change function 9
#After the function call  100
#
