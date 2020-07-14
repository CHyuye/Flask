"""
	单元测试：目的是检验其是否满足需求，并得出特定的结果，
		以达到弄清楚预期结果和实际结果之间的差别的最终目的。
	断言(assert):断言就是判断一个函数或对象的一个方法所产生的结果是否符合你期望的那个结果。
		python中assert断言是声明布尔值为真的判定，
		如果表达式为假会发生异常。单元测试中，一般使用assert来断言结果

"""


def num_div(num1, num2):
	# assert 断言 后面是一个表达式，如果表达式返回真，则断言成功，程序继续往下执行
	# 如果表达式返回假，则断言失败，assert抛出AssertError，终止程序执行
	assert isinstance(num1, int)
	# isinstance(a, b)方法，判断某个对象是不是属于一个类型
	# issubclass(a, b)方法，判断一个类是不是另一个类的子类
	assert isinstance(num2, int)
	assert num2 != 0
	print(num1 / num2)


if __name__ == '__main__':
	num_div(100, 20)

