"""
	jsonify方法，操作json数据，传递给前端
"""
from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/")
def index():
	# json就是字符串
	data = {
		"user": "chenhan",
		"gender": "boy",
		"age": 20
	}
	# 方式一 —— 返回给前端json数据的
	# json.dumps(字典)  将Python的字典格式转换为json字符串
	# json.loads(字符串) 将json字符串转换为python的字典格式
	# json_str = json.dumps(data)
	# return json_str, 200, {"Content-Type": "application/json"}

	# 方式二 —— 使用jsonify方法返回json数据
	# return jsonify(data)

	# 或者你想直接返回一些简单的json数据也可以
	return jsonify(city="Shanghai", country="China")


if __name__ == '__main__':
	app.run(debug=True)
