from flask import Flask, request

app = Flask(__name__)

# 接口：主要用来描述类的功能
# 127.0.0.1:5000/index?city=Shanghai&country=China  ?号后面的是 查询字符串(QueryString)
@app.route("/index", methods=["GET", "POST"])
def index():
	"""
		request中包含了前端发送过来的所有请求数据
		通过request.form可以直接获取请求体中的表单格式数据， 是一个类字典的对象
	对于获取的前端的数据最好用get方法，如request.form["name']当取的值没有是会报错，get则显示none
		通过get方法，只能拿到多个同名参数的第一个
	表单格式之一：name=xx&age=XX&gender=XX
	"""
	# form 获取表单提交信息  data和form都是请求体数据
	name = request.form.get("name")
	# 通过get方法，只能拿到多个同名参数的第一个
	age = request.form.get("age")
	gender = request.form.get("gender")
	# 当出现多个重名参数时可以使用getlist()方法
	name_li = request.form.getlist("name")

	# args 获取查询字符串 --> url地址中的参数(查询字符串)
	city = request.args.get("city")

	# data指所有前端数据，因为表单数据被from解析了，会显示空，当传递的是json数据时可以显示
	print("request.data:%s" % request.data)
	return "Hello %s(age=%s), welcome to %s. This is index page.".format(name, age, city)


if __name__ == '__main__':
	app.run(debug=True)
