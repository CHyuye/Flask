"""
	Flask视图函数的路由
"""
from flask import Flask, current_app, redirect, url_for

# 创建一个flask的应用对象
# __name__表示当前的模块名
app = Flask(__name__)


@app.route("/")
def index():
	"""定义视图函数"""
	return "Hello World, my name is Chenhan."


# 设置请求方式，通过methods限定访问方式，传入的是一个列表，网页默认为GET请求
@app.route("/post", methods=["POST", "GET"])
def post_only():
	"""定义只允许post请求方式视图函数"""
	return "Hello python."


# 同一路由装饰多个视图函数，可以用methods限定方式，区分
@app.route("/hello", methods=["POST"])
def hello1():
	"""程序从上往下执行，所以如果不设定methods，访问的是hello1"""
	return "hello1"

@app.route("/hello", methods=["GET"])
def hello2():
	"""因为网页请求默认为GEY请求方式，所以此时会访问hello2"""
	return "hello2"


# 同一个视图函数被多个路由器装饰
@app.route("/h1")
@app.route("/h2")
def multi():
	return "multi decorate"


# 通过url_for，redirect实现网页跳转
@app.route("/login")
def login():
	"""登录函数"""
	# url = "/"  代码写死了，之后如更改url会很麻烦
	# 通过url_for函数，通过视图函数的名字找到视图函数对应的url路径，即使url更改也不会有影响
	url = url_for("index")
	return redirect(url)

@app.route("/register")
def register():
	"""注册函数"""
	url = url_for("index")
	return redirect(url)

if __name__ == '__main__':
	# 通过url_map可以查看整个flask中的路由信息
	print(app.url_map)
	# 启动flask程序
	app.run(debug=True)
