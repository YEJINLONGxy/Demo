#!/usr/bin/env python3

#求N个数字的平均值，测试10个数字的评价值

N = 10
sum = 0
count = 0

print('Please input 10 number: ')
while count < N:
	number = float(input())
	sum = sum + number
	count += 1

average = sum / N
print("N = {}, Sum = {}".format(N, sum))
print("Average = {:.2f}".format(average))
