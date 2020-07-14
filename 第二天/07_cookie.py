"""
	cookie的设置，获取与删除(删除只是修改了访问时间)
"""
from flask import Flask, make_response, request


app = Flask(__name__)


@app.route("/set")
def set_cookie():
	"""
		cookie的设置
		认识1：cookie默认有效期为临时的，即浏览器关闭就失效
		认识2：max_age方法设置有效期，单位为秒
	"""
	resp = make_response("If you look this page who congratulate set cookie success")
	resp.set_cookie("username", "python")
	resp.set_cookie("password", "1025")  # 默认cookie会在浏览器关闭后，就消失
	resp.set_cookie("check_pwd", "1025", max_age=3600)  # max_age方法设置访问最大时间
	return resp


@app.route("/get")
def get_cookie():
	"""
		获取cookie，使用Flask的request模块
		认识：request.cookies.get("password")
	"""
	cookie = request.cookies.get("password")
	return "You need cookie where is this:'%s'" % cookie


@app.route("/del")
def del_cookie():
	"""
		删除cookie，使用Flask的make_response模块的delete_cookie方法
		resp.delete_cookie("check_pwd")
	"""
	resp = make_response("Oh no you delete cookie, are you sure?")
	# 删除cookie操作
	resp.delete_cookie("check_pwd")
	return resp


if __name__ == '__main__':
	app.run(debug=True)

