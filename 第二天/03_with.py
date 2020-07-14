"""
	with上下文管理器:上下文管理器就是调用了python魔法方法
	__enter__和__exit_，他会先调用__enter__方法，进行对应操作，__exit__捕获异常操作
"""

# try -- except -- finally 可以保证文件出错时，关闭文件操作
# 1.创建一个文件
# f = open("./demo.txt", "a")
# try:
# 	# 2.write 写入文件
# 	f.write("Hello python")
# except Exception:
# 	pass
# finally:
# 	# 3.关闭文件
# 	f.close()

# with -- 上下文管理器
# with open("./demo.txt", 'a') as f:
# 	f.write("welcome to China")
#

class Foo(object):

	def __enter__(self):
		"""进入with语句时会被调用"""
		print("enter is called")

	def __exit__(self, exc_type, exc_val, exc_tb):
		"""退出with时会被调用到"""
		print("exit is called")
		print("*" * 30)
		print("exc_type: %s" % exc_type)  # 检测error的错误类型
		print("exc_val: %s" % exc_val)  # 检测error的错误原因
		print("exc_tb: %s" % exc_tb)  # 检测error的错误地址


with Foo() as foo:
	print("Welcome to China")
	# a = 1 / 0
	print("Programme is ending")