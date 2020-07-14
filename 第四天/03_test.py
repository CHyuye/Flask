import unittest
from login import app
import json


class LoginTest(unittest.TestCase):
	"""
		构造单元测试案例
		1.测试用户名或密码不完整的情况
		2.测试用户名或密码错误的情况
		3.测试用户名登录正确的情况
	"""

	def setUp(self):
		"""在进行测试之前，先被执行"""
		# 设置flask工作在测试模式下
		# app.config["TESTING"] = True   方式一
		# 激活测试模式，建议打开这样可以看到测试代码的所有错误详细信息
		app.testing = True

		# 1.创建web请求的客户端，使用flask提供的，当然亦可以使用requests库
		self.client = app.test_client()

	# 函数名必须以test_开头
	def test_empty_username_pwd(self):
		"""测试用户名密码不完整的情况"""
		# 2.使用Clinton客户端模拟发送请求
		# 情况一：用户名密码都没传
		result = self.client.post("/login", data={})

		# 3.result是视图返回的响应对象，data属性是响应体的数据
		response = result.data

		# 4,因为login视图返回的是json字符串，所以先解析一下
		response = json.loads(response)

		# 5.拿到返回值后进行断言测试
		# 常见断言方法
		# assertEqual 如果两个值相等，则pass
		# assertNotEqual 如果两个值不相等，则pass
		# assertTrue 判断bool值为True，则pass
		# assertFalse 判断bool值为False，则pass
		# assertIsNone 不存在，则pass
		# assertIsNotNone 存在，则pass
		# code，在response中
		self.assertIn("code", response)
		# response的code值等于1
		self.assertEqual(response['code'], 1)

		# 情况二：只传用户名
		result = self.client.post("/login", data={"username": "admin"})

		# 3.result是视图返回的响应对象，data属性是响应体的数据
		response = result.data

		# 4,因为login视图返回的是json字符串，所以先解析一下
		response = json.loads(response)

		# 5.拿到返回值后进行断言测试
		self.assertIn("code", response)
		# response的code值等于1
		self.assertEqual(response['code'], 1)

		# 情况三：只传密码
		result = self.client.post("/login", data={"password": "python"})

		# 3.result是视图返回的响应对象，data属性是响应体的数据
		response = result.data

		# 4,因为login视图返回的是json字符串，所以先解析一下
		response = json.loads(response)

		# 5.拿到返回值后进行断言测试
		self.assertIn("code", response)
		# response的code值等于1
		self.assertEqual(response['code'], 1)

	def test_username_pwd_right(self):
		"""测试用户名密码的正确"""
		# # 1.创建client客户端
		# self.client = app.test_client()
		# 2.使用客户端发送请求
		data = {"username": "admin", "password": "python"}
		result = self.client.post("/login", data=data)
		# 3.接收login视图返回的json字符串
		response = json.loads(result.data)
		# 4.断言测试
		self.assertIn("message", response)
		self.assertEqual(response["code"], 0)

	def test_wrong_username_pwd(self):
		"""测试用户名或密码错误"""
		# 请况一：用户名错误
		result = self.client.post('/login', data={"username": "chenhan"})
		response = json.loads(result.data)
		self.assertIn("code", response)
		self.assertEqual(response["code"], 2)
		# 情况二：密码错误
		result = self.client.post('/login', data={"password": "1025"})
		response = json.loads(result.data)
		self.assertIn("code", response)
		self.assertEqual(response["code"], 2)
		# 请况三：用户名，密码都错误
		data = {"username": "chenhan", "password": "alan"}
		result = self.client.post('/login', data=data)
		response = json.loads(result.data)
		self.assertIn("code", response)
		self.assertEqual(response["code"], 2)


if __name__ == '__main__':
	# unittest.main()这种方式可以直接启动程序，并会检测所有测试
	unittest.main()