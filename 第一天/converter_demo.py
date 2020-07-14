"""
	路由转换器的进阶使用
	to_python和to_url的使用及作用
"""

from flask import Flask, url_for, redirect
from werkzeug.routing import BaseConverter

app = Flask(__name__)

# 1.创建自定义转换器
class RegexConverter(BaseConverter):
	def __init__(self, url_map, regex):
		# 调用父类的初始化方法
		super(RegexConverter, self).__init__(url_map)
		# 将正则表达式的参数保存到对象的属性中，flask会使用这个属性来进行路由的正则匹配
		self.regex = regex

	def to_python(self, value):
		print("该方法会被调用")
		# value是在路径进行正则表达式匹配的时候提取的参数
		# return "abc"
		return value

	def to_url(self, value):
		print("使用url_for方法时，to_url方法会被调用")
		# return "110"
		return value
		

# 2.把自定义的转换器添加到Flask应用中
app.url_map.converters["re"] = RegexConverter

@app.route("/send/<re(r'1[345789]\d{9}'):phone_num>")
def send_sms(phone_num):
	return "Your phone_num is %s" % phone_num

@app.route("/index")
def index():
	url = url_for("send_sms", phone_num="19946238583")
	return redirect(url)

if __name__ == "__main__":
	app.run(debug=True)

