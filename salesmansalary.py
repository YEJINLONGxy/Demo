#!/usr/bin/env python3


#程序计算一位数码相机销售人员的工资。他的基本工资是 1500，
#每售出一台相机他可以得到 200 并且获得 2% 的抽成。程序要求输入相机数量及单价

basic_salary = 1500
bonus_rate = 200
commission_rate = 0.02

#输入销售数量
numberofcamera = int(input("Enter the namber of imputs sold: "))

#输入单价
price = float(input("Enter the price of camera: "))

bonus = (bonus_rate * numberofcamera)
commission = (commission_rate * price * numberofcamera)

print("Bonus		= {:6.2f}".format(bonus))
print("Commission	= {:6.2f}".format(commission))
print("Gross salary	= {:6.2f}".format(basic_salary + bonus + commission))
