#!/usr/bin/env python3

import unittest
from factorial import fact

class TestFactorial(unittest.TestCase):
	"""
	我们的基本测试类
	"""

	def test_fact(self):
		"""
		实际测试
		任何以 `test_` 开头的方法都被视作测试用例
		"""
		
		res = fact(5)
		self.assertEqual(res, 120)
		#self.assertEqual(res, 121)

	def test_error(self):
		"""
		测试由运行时错误引起的异常
		"""

		self.assertRaise(ZeroDivisionError, div, 0)

if __name__ == '__main__':
	unittest.main()
