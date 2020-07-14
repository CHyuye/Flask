# 使用from '.'的方式导入当前所属目录下创建的app_cart蓝图模块
from . import app_cart
from flask import render_template

@app_cart.route("/get_cart")
def get_cart():
	return render_template("cart.html")
