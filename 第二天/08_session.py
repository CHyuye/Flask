"""
	session机制说明(广义)：
		当你访问浏览器，处理相应操作时，服务器给你设置的cookie，session_id，
		session_id会被服务器端保存到数据库中，如果你下次再次访问时，输入对应的信息，
		服务器会从数据库找出对应的session_id，还原你的信息
	session(狭义)：
		保存到服务器中的session数据

	拓展：flask的上下文对象
	请求上下文：request和session
	request从flask导入时是一个全局变量，当我们向服务器发出请求，request.form.get("name")
	服务器请求前端传递的form表单中的name参数，request会创建一个线程A对用户A记录A的操作，
	当用户B也去请求表单操作，request也会创建一个线程B记录B的操作

	应用上下文（application context）
	current_app和 g 都属于应用上下文对象
	current_app：表示当前与运行程序文件的程序实例
	g：处理请求时，用于临时存储的对象，每次请求都会重设这个变量
"""
from flask import Flask, session, request, g


app = Flask(__name__)


# flask中的session设置必须要用到密钥字符串secret_key(字符串内容可以随意)
app.config["SECRET_KEY"] = "youdonotwanttoknowthissecret_key"


@app.route("/login")
def login():
	# 设置session数据
	session["name"] = "python"
	session["password"] = "1025"
	session["phone"] = "19946238583"

	# g变量--可以用于函数之间传递数据，但每次Flask请求之后都会被清空，重设
	g.username = "chenhan"
	return "login success"


@app.route("/index")
def index():
	# 获取session数据
	name = session.get("name")
	password = session.get("password")
	# g变量--其他函数取出数据
	username = g.username
	return "Hello %s, you password is '%s'." % (name, password)


if __name__ == '__main__':
	app.run(debug=True)

