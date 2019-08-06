#!/usr/bin/env python3

#在讲解单词计数之前我们先了解一个概念：格式化操作符（%）
# >>> print("my name is %s.I am %d years old" % ('shiyanlou', 4))
# my name is shiyanlou.I am 4 years old

#在这个例子中，%s 为第一个格式符，表示一个字符串；%d 为第二个格式符，表示一个整数。
#格式符为真实值预留位置，并控制显示的格式。常用的有：

#%s 字符串（用 str() 函数进行字符串转换）

#%r 字符串（用 repr() 函数进行字符串转换）

#%d 十进制整数

#%f 浮点数

#%% 字符“%”

###########################################################
#对用户输入的一行文本进行单词计数

s = input("Enter a line: ")
print("The number or words in the line are %d" % (len(s.split(" ")))) 

#split(" ") 以空格分割字符串，返回列表
#len()	计数列表长度

