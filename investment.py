#!/usr/bin/env python3
#

#amount = float(input('Enter amount: '))  #输入数额
#inrate = float(input('Enter Interest rate: ')) #输入利率
#period = int(input('Enter period: '))	#输入期限

#value = 0
#year = 1

def investment():
	amount = float(input('Enter amount: '))  #输入数额
	inrate = float(input('Enter Interest rate: ')) #输入利率
	period = int(input('Enter period: '))   #输入期限
	
	value = 0
	year = 1

	while year <= period:
		value = amount + (inrate * amount)	#计算投资总得
		#print("Year {} Rs. {:.2f}".format(year, value))
		amount = value
		year += 1
		
	return year-1, amount
	
investment = investment()
print('Year {} Rs. {:.2f}'.format(investment[0], investment[1]))

