"""
	请求钩子：别人给你预留的位子，在执行视图函数前后，Flask使用装饰器给我们提供一些连带功能
	请求钩子是通过装饰器形式实现的
	在客户端和服务器交互中，有些准备工作或扫尾工作需要处理时，
	为了让每个视图函数避免重复功能的代码，可以使用请求钩子
"""
from flask import Flask, request, url_for


app = Flask(__name__)


@app.route("/index")
def index(): 
	print("index 被执行")
	a = 1 / 0
	return "Welcome to index page"


@app.route("/other")
def other():
	print("other 被执行")
	return "this is a unable page"


@app.before_first_request
def handle_before_first_request():
	"""视图函数在第一次请求处理之前先被执行，只执行一次"""
	print("handle_before_first_request 被执行")


@app.before_request
def handle_before_request():
	"""视图函数每次请求之前都会被执行"""
	print("handle_before_request 被执行")


@app.after_request
def handle_after_request(response):
	"""
	after_request和teardown_request请求钩子需要接收视图函数传递过来的response参数
	而且我们需要返回
	视图函数在每次请求（视图函数处理）之后都被执行，前提是视图函数没有出现异常
	"""
	print("handle_after_request 被执行")
	return response


@app.teardown_request
def handle_teardown_request(response):
	"""
	视图函数在每次请求（视图函数处理）之后，无论视图函数是否出现异常，都会被执行，
	但要在生产环境中，即不是（工作）debug模式
	"""
	# request.path可以取出当前请求的url地址
	# print(request.path)
	path = request.path
	if path == url_for("index"):
		print("在请求钩子中判断请求视图逻辑，做出需要的操作：index")
	elif path == url_for("other"):
		print("在请求钩子中判断请求的视图函数逻辑，做出相应的操作：other")

	print("handle_teardown_request 被执行")
	return response


if __name__ == '__main__':
	app.run()
