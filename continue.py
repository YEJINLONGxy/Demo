#!/usr/bin/env python3

#continue 语句
#如同 break ，我们可以在循环中使用另一个语句 continue，它会跳过其后的代码回到循环开始处执行
#这意味着它可以帮助你跳过部分循环。


#在下面的例子中，我们要求用户输入一个整数，如果输入的是负数，那么我们会再次要求输入，
#如果输入的是整数，我们计算这个数的平方。用户输入 0 来跳出这个无限循环

while True:
	n = int(input('Please enter an Integer: '))
	if n < 0:
		continue	#如果是负数，这会返回到循环开始处执行
	#elif n == 0:
	#	break		#如果是0，程序关闭
	else:		
		print("Squa is ", n**2)
		break
print("Goodbye")
