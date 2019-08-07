#!/usr/bin/env python3
#局域或全局变量

#我们通过几个例子来弄明白局域或全局变量，首先我们在函数内部和函数调用的代码中都使用同一个变量 a

def change():
	a = 90
	print(a)
a = 9
print("Befor the function call", a)
print("inside change function", end=" ")
change()
print("After the function call", a)

#执行代码

#[root@dev1 python_code]# ./local.py 
#Befor the function call 9
#inside change function 90
#After the function call 9

"""
首先我们对 a 赋值 9，然后调用更改函数，这个函数里我们对 a 赋值 90，然后打印 a 的值。
调用函数后我们再次打印 a 的值。      当我们在函数里写 a = 90 时，它实际上创建了一个
新的名为 a 的局部变量，这个变量只在函数里可用，并且会在函数完成时销毁。所以即使这两
个变量的名字都相同，但事实上他们并不是同一个变量。
"""
########################################################

#那么如果我们先定义 a，在函数中是否可以直接使用呢？
#例如下面这段代码：
#a = 9
#def chenge():
#	print(a)
#change()

#这段代码是没有问题的，可以直接打印输出 9。稍微改动一下：

##########################################################

#a = 9
#def change():
#	print(a)
#	a = 100
#change()
#
#[root@dev1 python_code]# ./local.py 
#Traceback (most recent call last):
#  File "./local.py", line 40, in <module>
#    change()
#  File "./local.py", line 38, in change
#    print(a)
#UnboundLocalError: local variable 'a' referenced before assignment

"""
现在就会报错了：“UnboundLocalError: local variable 'a' referenced before assignment”，
原因是当函数中只要用到了变量 a，并且 a 出现在表达式等于号的前面，就会被当作局部变量。

上面代码中，当执行到 print(a) 的时候会报错，因为 a 作为函数局部变量是在 print(a) 之后才定义的
"""




