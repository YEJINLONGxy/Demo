#!/usr/bin/env python3
"""
实现一个程序，将分钟转为小时和分钟

注意：代码中不要使用 input() 函数，否则挑战测试会卡住，出现 Timeout 的报错

在 MinutesToHours.py 文件中实现一个函数 Hours()，将用户输入的 分钟数 转化为 小时数和分钟数，并要求小时数尽量大。
将结果以 XX H, XX M 的形式打印出来。

要求：

用户能够通过命令行参数输入分钟数，不要使用 input，命令行参数可以使用 sys.argv 来提取。例如程序执行为 python3 Min
utesToHours.py 80，传入的参数 80 就是分钟数，程序需要打印出相应的小时数和分钟数，输出为 1 H, 20 M。

如果用户输入的是一个负值，程序需要 raise 来抛出 ValueError 异常。
Hours() 函数调用的时候，需要使用 try...except 处理异常。获取异常后，在屏幕上打印出 Parameter Error 提示用户输入
的值有误

运行方式：
[root@dev1 python_code]# ./MinutesToHours.py -10
Parameter Error
[root@dev1 python_code]# ./MinutesToHours.py nihao
Parameter Error
[root@dev1 python_code]# ./MinutesToHours.py 80
1 H, 20 M


提示语
	sys.argv 获取命令行参数，注意获取的参数为字符串，可以使用 int() 将字符串转为整数，此处也可能会出现异常情
况，例如输入为 "abcd" 是无法转为整数的
	raise 语句
	try...except 语句

知识点
	异常
	文件处理
	if-else

"""


import sys

def Hours(minute):
	#如果为负数则 raise 异常
	if minute < 0:
		raise ValueError("Input number cannot be negative")
	else:
		print("{} H, {} M".format(*divmod(minute,60)))		#divmod()返回元组整数和余数

if __name__ == "__main__":
	#函数调吊用及异常处理逻辑 "列如输入字母的判断"
	try:
		Hours(int(sys.argv[1]))
	except:
		print("Parameter Error")


#++++++++错误+++++++++++++++
#def Hours(H):
#	try:	
#		print("{} H, {} M ".format(*divmod(H,60)))
#	except ValueError:
#		print("Parameter Error")
#
#if __name__ == "__main__":
#	minute = int(sys.argv[1])
#	if minute < 0:
#		raise ValueError("Input number cannot be negative")
#	else:
#		Hours(minute)
#		
#	
