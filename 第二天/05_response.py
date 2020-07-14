"""
	设置响应信息的方式
"""
from flask import Flask, make_response

app = Flask(__name__)


@app.route("/")
def index():
	# 1.使用元组的方式，返回自定义的信息
	#         响应体                   响应状态码  响应头信息
	# return "This is a little test.", 400, [("user", "python"), ("age", "20")]
	# return "This is a little test", "666 test Status", {"user":"python", "height": "165"}
	# return "This is a little test", "666 test Status"  # 按照顺序写入要写的参数，响应头可以不写

	# 2.使用make_response 来构造响应的信息
	resp = make_response("In this one, try to make_response method.")  # 设置响应体
	resp.status = "500 Test Status"  # 设置响应状态码
	resp.headers["user"] = "chenhan"  # 设置响应头信息
	return resp


if __name__ == '__main__':
	app.run(debug=True)
