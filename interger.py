#!/usr/bin/env python3

days = int(input("Enter days: "))
months = days // 30   #取整数
days = days % 30 	#取余数

print("Months = {} dasy = {}".format(months, days))

###################or#####################
#days = int(input("Enter days: "))
#print("Months = {} days = {}".format(*divmod(days, 30)))

#divmod(num1, num2) 返回一个元组，这个元组包含两个值，
#第一个是 num1 和 num2 相整除得到的值，第二个是 num1 和 num2 求余得到的值，
#然后我们用 * 运算符拆封这个元组，得到这两个值。

#>>> divmod(235, 30)
#(7, 25)

