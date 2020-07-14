# 一个文件，加上一个__init__.py就是一个包
# 以下操作展示，用目录形式定义蓝图，cart模型
from flask import Blueprint

# 创建一个蓝图，如果要在小蓝图里面定义模板文件，需要在此定义指定参数，
# 但如果主应用程序有同名模板文件，优先显示主目录下的模板文件
app_cart = Blueprint(
	'app_cart',
	__name__,
	template_folder="templates",
	static_folder="static"
)

# 在__init__.py文件正被执行的时候，把视图view.py加载进来，让蓝图与应用程序知道有视图的存在
from .view import get_cart

