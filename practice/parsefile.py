#!/usr/bin/env python3

#文本文件相关信息统计

#编写一个程序，对任意给定文本文件中的制表符、行、空格进行计数

import os, sys

def parse_file(path):
	"""
	分析给定文本文件，返回期空格、制表符、行的相关信息
	
	:arg path: 要分析的文件文件的路径

	:return: 包含空格数、制表符、行数的元组
	"""

	fd = open(path)
	i = 0					#计数行
	spaces = 0
	tabs = 0
	for i, line in enumerate(fd):
		spaces += line.count(" ")	#字符串line中，计数空格
		tabs += line.count("\t")
		#print(line)
	#现在关闭打开的文件
	fd.close()

	#以元组形势返回结果
	return spaces, tabs, i + 1


def main(path):
	"""
	函数用于打印文件分析结果

	:arg path: 要分析的文本文件的路径
	:return: 若文件存在则为 True, 否则 False
	"""

	if os.path.exists(path):
		spaces, tabs, lines = parse_file(path)		#return 返回的数据赋值左边
		print("Spaces {}. tabs {}. lines {}".format(spaces, tabs, lines))
		return True
	else:
		return False


if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		sys.exit(-1)
	sys.exit(0)



