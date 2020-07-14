"""
	模板与自定义过滤器
"""
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
	data = {
		"name": "chenhan",
		"age": 20,
		"my_dict": {"city": "Shanghai"},
		"my_list": [1,2,3,4,5],
		"my_int": 0,
	}
	# **data解包操作，把data中的数据平展开
	return render_template("index.html", **data)


@app.route("/xss", methods=["GET", "POST"])
def xss():
	"""xss攻击，一种利用转义字符，向前端输入脚本文件，启动的形式"""
	text = ""
	if request.method == "POST":
		text = request.form.get("name")
	return render_template("xss.html", text = text)


# 方式一：通过自定义函数，然后注册
def list_step_2(li):
	"""自定义过滤器——一个列表，隔一个值取一个值"""
	return li[::2]


# 注册自定义过滤器      功能函数名，  自定义过滤器名
app.add_template_filter(list_step_2, 'li2')


# 方式二：自定义函数，装饰器注册方式
@app.template_filter("li3")
def list_step_3(li):
	return li[::3]


if __name__ == '__main__':
	app.run(debug=True)
