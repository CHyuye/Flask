"""
	python中map函数的使用:
	map函数：传入一个定义函数，传入对应的值，返回相对应的结果
"""

li = [1, 2, 3, 4]
li2 = [1, 2]


def add(num1, num2):
	"""相加函数"""
	return num1 + num2


def add_self(num):
	"""自加函数"""
	return num + 2


ret = map(add, li, li2)
ret2 = map(add_self, li)

# python3中需要加上list转换为具体的值，否则返回对象
print(list(ret))
print(list(ret2))

# python2中直接返回具体值
# print(ret)

