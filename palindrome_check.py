#!/usr/bin/env python3
#回文检查

#回文是一种无论从左还是从右读都一样的字符序列。比如 “madam”
#在这个例子中，我们检查用户输入的字符串是否是回文，并输出结果

s = input("Please enter a string: ")
z = s[::-1]  #把输入的字符串 s 进行倒叙处理形成新的字符串 z

if s == z:
	print("The string is a palindrome")
else:
	print("The string is not a palindrome")

#运行程序
#[root@dev1 python_code]# ./palindrome_check.py 
#Please enter a string: madam1
#The string is not a palindrome
#[root@dev1 python_code]# ./palindrome_check.py 
#Please enter a string: madam
#The string is a palindrome

