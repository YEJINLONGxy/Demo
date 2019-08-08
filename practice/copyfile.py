#!/usr/bin/env python3

import sys

if len(sys.argv) < 3:		#检测参数是否小于3.如果是，返回操作提示
	print("Wrong parmeter")
	print("./copyfile.py file1 file2")
	sys.exit(1)

f1 = open(sys.argv[1])		# 获取第一个文件，打开
s = f1.read()			#读取文件内容，赋值给 s
f1.close()

f2 = open(sys.argv[2], 'w')	#获取第二个拷贝后的文件名，并创建文件	
f2.write(s)			#将 s 内容写入到文件 f2(即拷贝后的文件)
f2.close()
