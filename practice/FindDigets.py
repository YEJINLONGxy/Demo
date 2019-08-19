#!/usr/bin/env python3
"""
程序用来提取文件中的字符串中的数字，然后打印输出

wget http://labfile.oss.aliyuncs.com/courses/790/String.txt
这个文件 String.txt 中存储了一个很长的字符串，需要读取并进行处理。

创建 FindDigits.py Python 脚本：

FindDigits.py 中，我们需要完成以下任务：

	1、使用 open 打开文件 /tmp/String.txt 并读取其中的字符串
	2、提取字符串中的所有数字，并组合成一个新的字符串，然后打印输出

提示语：

	1、可以使用循环来访问字符串中的单个字符
	2、可以使用 isdigit() 来判断字符是否为数字
	3、使用 print() 把新的数字组成的字符串输出

知识点：
	1、文件读取
	2、for 循环
	3、字符串操作

"""
import os, sys
#path = "/home/shiyanlou/String.txt"

#打开并读取文件里的字符串
def openfile(path):
	with open(path) as f:
		s = f.read()
	return s
#print(openfile(path))


#循环字符串里的每个字符。判断是否为数字
def char(path):
	s = openfile(path)
	res = ""
	#print(s)
	for char in s:
		if char.isdigit():
			res += char
	return res

if __name__ == "__main__":
	path = "/home/shiyanlou/String.txt"
	if len(sys.argv) > 1:			#如果有外部参数，则使用
		string = char(sys.argv[1])
		print(string)
	else:
		string = char(path)
		print(string)
		
