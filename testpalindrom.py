#!/usr/bin/env python3

#定义一个函数
#让我们编写一个函数来检查给出的字符串是否为回文，然后返回 True 或者 False

def palindrome(s):
	return s == s[::-1]

if __name__ == '__main__':
	s= input("Enter a string: ")
	if palindrome(s):
		print("Yay a plindrome")
	else:
		print("Oh no, not a palindrome")

#运行程序

#[root@dev1 python_code]# ./testpalindrom.py 
#Enter a string: 1221
#Yay a plindrome
#[root@dev1 python_code]# ./testpalindrom.py 
#Enter a string: fofo
#Oh no, not a palindrome
