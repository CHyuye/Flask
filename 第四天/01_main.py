from flask import Flask
from register import register  # 不使用蓝图
from goods import app_goods  # 使用蓝图
from cart import app_cart  # 使用目录形式蓝图
# 循环引用：就是多个模块之间相互导入，但都没有完全执行完的一种状态，
# 第一种方式解决方法，推迟一方的导入，让另一方先执行完

app = Flask(__name__)

# 第二种方法：使用装饰器解决模块的分割问题
app.route("/register")(register)


"""
蓝图：用于实现单个应用的视图，模板，静态文件的集合
蓝图就是模块化的类，简单来说，蓝图就是存储操作路由映射的方法的容器，主要用来实现客户端请求和URl相互关联的功能
	蓝图的使用和基本定义
	1.创建蓝图对象
	2.注册蓝图路由
	3.主程序实例中注册该蓝图
"""
# 注册蓝图，参数url_prefix="" 加前缀，可以使得该模型下的定义路由更清晰
app.register_blueprint(app_goods, url_prefix="/goods")
# 注册cart蓝图，你会发现，它并不会去检测执行cart目录下的view.py,需要在__init__中导入view.py,让它读取
app.register_blueprint(app_cart, url_prefix="/cart")

"""
如何理解app.route("/register")(register)的性质呢？
三层闭包函数，就是装饰器
def route(params):
	def decorator(func):
		def inner():
			pass
		return inner
	return decorator

# route("/goods")(goods) 其实就是decorator(goods), route是最外层装饰，decorator可以携带属于自己的func
"""
@app.route("/")
def index():
	return "index page"


# 现在模拟模块化划分，将以下分成两个
# @app.route("/register")
# def register():
# 	return "register page"
#
#
# @app.route("/goods")
# def goods():
# 	return "goods page"


if __name__ == '__main__':
	print(app.url_map)
	app.run(debug=True)
