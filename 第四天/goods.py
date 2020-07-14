"""
蓝图：用于实现单个应用的视图，模板，静态文件的集合
蓝图就是模块化的类，简单来说，蓝图就是存储操作路由映射的方法的容器，主要用来实现客户端请求和URl相互关联的功能
	蓝图的使用和基本定义
	1.创建蓝图对象
	2.注册蓝图路由
	3.主程序实例中注册该蓝图
"""
from flask import Blueprint

# 创建一个蓝图的对象，蓝图就是一个小模块的抽象的概念
# Blueprint必须指定以下两个参数，app_goods表示蓝图的名称，__name__表示蓝图所在的模块
app_goods = Blueprint("app_goods", __name__)


@app_goods.route("/get_goods")
def get_goods():
	return "get goods page."


@app_goods.route("/choice_goods")
def choice_goods():
	return "choice goods page"

