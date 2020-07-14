"""
	配置SQLAlchemy
	建立flask框架写的模型类对应的往sql数据库插入数据，需要三个工具
	一：SQLAlchemy将对应的模型类——>sql语句
	二：MySQL-Python或pymysql将sql语句传送到sql数据库中
	三：SQLAlchemy将sql语句操作结果——>模型类
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


class Config(object):
	"""SQLAlchemy的配置参数"""
	# SQLAlchemy的配置参数       数据库://用户名:密码@Ip地址:端口号:/创建的数据库名
	SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/db_python"

	# 设置SQLAlchemy自动跟踪数据库
	SQLALCHEMY_TRACK_MODIFICATIONS = True


# flask配置
app.config.from_object(Config)

# 创建数据库SQLAlchemy工具对象
db = SQLAlchemy(app)


"""
	表名的常见规范
	ihome --> ih_user  数据库名缩写_表名
	tbl_user  tbl_表名
"""


# 创建数据库模型类
class User(db.Model):
	"""创建用户表"""
	__tablename__ = "tbl_users"  # 指明数据库的表名

	id = db.column(db.Integer, primary_key=True)  # 整型的主键，会默认主键自增
	name = db.column(db.String(32), unique=True)
	email = db.column(db.String(64), unique=True)
	password = db.column(db.String(32))
	# 建立外键关系                                  角色数据表名的id
	role_id = db.column(db.Integer, db.ForeignKey("tbl_roles.id"))

	def __repr__(self):
		"""定义显示信息"""
		return "User object: name={}".format(self.name)


class Role(db.Model):
	"""创建角色表"""
	__tablename__ = "tbl_roles"

	id = db.column(db.Integer, primary_key=True)
	name = db.column(db.String(32), unqiue=True)
	age = db.column(db.Integer)
	gender = db.column(db.Boolean, default=True)

	# 与用户表建立关系，       模型类名   反推出角色表中对应的角色在用户表的信息
	users = db.relationship("User", backrefb="role")

	def __repr__(self):
		"""定义显示方法"""
		return "Role object:{}".format(self.name)


if __name__ == '__main__':
	# 清除数据库中所有数据，仅限第一次创建数据库使用
	# db.drop_all()
	
	# 创建所有的表
	db.create_all()

	# 创建对象，保存数据到数据库
	role1 = Role(name="吕布", age="29", gender=True)
	# session记录对象任务
	db.session.add(role1)
	# commit提交任务到数据库中
	db.session.commit()

	role2 = Role(name="嫦娥", age="21", gender=False)
	db.session.add(role2)
	db.session.commit()

	role3 = Role(name="猪八戒", age="26", gender=True)
	db.session.add(role3)
	db.session.commit()

	# 添加用户表
	us1 = User(name="lv", email="lv@163.com", password="4399", role_id=role1.id)
	us2 = User(name="chang", email="chang@163.com", password="4399", role_id=role2.id)
	us3 = User(name="sun", email="sun@163.com", password="4399", role_id=role3.id)

	# 一次保存多条数据
	db.session.add_all([us1, us2, us3])
	db.session.commit()
