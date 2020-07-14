"""
	flask_script模块，导入Manager启动命令管理类，
	就需要向Django一样通过命令行运行程序，当然Manager支持扩展其他命令
"""

from flask import Flask
from flask_script import Manager  # 脚本（启动）命令的管理类


app = Flask(__name__)

# 创建Manager管理类的对象
manager = Manager(app)


@app.route("/")
def index():
	return "昔日龌龊不足夸，今朝放荡思天涯。/n春风得意马蹄急，一日看尽长安花。"


if __name__ == '__main__':
	# app.run()
	# 通过管理对象来启动flask
	manager.run()

