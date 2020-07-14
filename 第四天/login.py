"""
	以下代码模拟一个模板表单，使用单元测试，检测其逻辑性
"""
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
	# 接收参数
	username = request.form.get("username")
	password = request.form.get("password")

	# 检验参数
	# 如果参数不完整，返回错误信息
	if not all([username, password]):
		resp = {
			"code": 1,
			"message": "invalid params"
		}
		return jsonify(resp)

	# 模拟从数据库读取信息，判断当前用户
	if username == 'admin' and password == 'python':
		resp = {
			"code": 0,
			"message": "login success"
		}
		return jsonify(resp)

	else:
		resp = {
			"code": 2,
			"message": "wrong username or password"
		}
		return jsonify(resp)

	# 返回请求


if __name__ == '__main__':
	app.run(debug=True)

