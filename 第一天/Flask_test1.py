# coding:utf-8

# Flask类，是项目的核心类，注册url，注册蓝图都是基于这个类的对象
from flask import Flask, current_app

# 创建flask的对象
# __name__ 表示的是当前模块的名字
# __name__的作用
# 1.可以规定模板文件和静态文件的查找路径
# 2.以后一些Flask的插件，比如Flask-migrate等如果报错了，可以通过这个参数进行找到具体位置
# 模块名，flask以这个模块所在的目录为总目录，默认这个目录中的static为静态目录，templates为模板目录
# 初始化Flask参数
app = Flask(
	__name__,  # 导入路径
	static_url_path="/python",  # 访问静态资源的url前缀，默认值为/static，此处修改为python
	static_folder="static",  # 静态文件的目录，默认值为static，可以自行修改
	template_folder="template_folder",  # 模板文件的目录，默认为templates，可以自行修改
	)

# 配置参数的形式
# 1.使用配置文件
# app.config.from_pyfile("config.cfg")

# 2.使用对象的方式配置参数[项目中可以使用这种方式]
class Config(object):
	DEBUG = True  # 测试模式打开
	ITCAST = "python"


app.config.from_object(Config)

# 3.直接操作config的字典对象[简单操作中]
# app.config["DEBUG"] = True

@app.route("/")
# @app.route("/")是一个装饰器,里面的"/"就是将url中的/映射到index这个视图函数上面
# 以后你访问这个网站或目录时，会执行index这个函数，然后将这个函数的返回值，返回给浏览器
def index():
	"""定义视图函数"""
	# a = 1/0
	# 读取配置参数的方式
	# 1.直接从全局对象app的config字典中取值或[app.config["ITCAST]]
	# print(app.config.get("ITCAST"))

	# 2.通过current_app获取参数
	print(current_app.config.get('ITCAST'))
	return "hello word"


# 如果这个文件是作为主文件运行，那么就执行app.run()方法，启动程序
if __name__ == '__main__':
	# 启动flask程序
	# app.run()，Flask中的测试应用服务器
	# app.run(host="192.168.0.1", port=5000)
	# 当把host参数设置为一个地址时，其他IP地址访问不到，0.0.0.0可以让windows或Linux的IP地址进行访问
	app.run(host="0.0.0.0", port=4455, debug=True)
