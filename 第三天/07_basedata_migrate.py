"""
	数据库迁移操作，不记得可以查看课件资料的信息
	以下都是命令行
	启动    当前的py文件  设置的db命令  操作
	python database.py  db         init
	1.创建迁移仓库 —— 这个命令会创建migrations文件夹，所有迁移文件都放在里面
		python database.py db init
	2.创建迁移脚本 ——自动创建迁移脚本有两个函数，upgrade()函数把迁移中的改动应用到数据库中。
	downgrade()函数则将改动删除。自动创建的迁移脚本会根据模型定义和数据库当前状态的差异，
	生成upgrade()和downgrade()函数的内容。对比不一定完全正确，有可能会遗漏一些细节，需要进行检查
		python database.py db migrate  -- 这个命令会自动生成迁移脚本，但还没有更新到数据库
	建议-->python database db migrate -m 'add age' -- 这个命令的 -m 'add age'是设置提示信息，
	upgrade()函数把迁移中的改动应用到数据库中
	3.更新数据库
		python database.py db upgrade
	4.回退数据库 -- 回退数据库时，需要指定回退版本号，由于版本号是随机字符串，为避免出错，
	建议先使用python database.py db history命令查看历史版本的具体版本号，然后复制具体版本号执行回退
		python database.py db history  查看历史版本的具体版本号
		python database.py db downgrade 版本号

"""
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager  # 脚本管理
from flask_migrate import Migrate, MigrateCommand  # 迁移，迁移命令
from flask import Flask
# from flask_mail import Mail, Message

# 创建Flask对象
app = Flask(__name__)
# 创建管理员对象
manager = Manager(app)

# 配置邮件：服务器/端口/传输层安全协议/邮箱名/密码
app.config.update(
	DEBUG=True,
	MAIL_SERVER="smtp.qq.com",
	MAIL_PORT=465,
	MAIL_USE_TLS=True,
	MAIL_USERNAME="1323057547.com",
	MAIL_PASSWORD="ch19946238583",
)


@app.route("/send_mail")
def send_mail():
	"""这是个测试，所以暂时没有 pip install falsk_mail"""
	# sender 发送方， recipients 接收方列表
	msg = Message("This is a test", sender='1323057547@qq.com', recipients=["123@qq.com"])
	# 邮件内容
	msg.body = "Flask test mail"
	# 发送邮件
	mail.send(msg)
	print("Mail sent")
	return "Sent Success!"


class Config(object):
	# sqlalchemy的配置参数
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@192.168.232.136:3306/author_book"

	# 设置sqlalchemy自动更跟踪数据库
	SQLALCHEMY_TRACK_MODIFICATIONS = True

	# 密钥，用于生成csrf_token
	SECRET_KEY = "doiso7fd89fyd9asdfavre"


# 添加配置信息
app.config.from_object(Config)

# 创建SQLALchemy的工具对象
db = SQLAlchemy(app)

# 创建迁移对象，第一个参数是Flask的实例，第二个参数是SQLALchemy数据库实例
migrate = Migrate(app, db)

# manager是Flask-Script的实例，这条语句在Flask-Script中添加一个db命令，也就是说，命令为db.什么
manager.add_command("db", MigrateCommand)


# 定义模型类
class User(db.Model):
	# 定义表名
	__tablename__ = "tbl_users"

	# 定义对象
	username = db.Column(db.Integer, primary_key=True)
	gender = db.Column(db.Boolean, default=True)
	age = db.Column(db.Integer)

	def __repr__(self):
		"""显示信息"""
		return "User:".format(self.username)


@app.route("/")
def index():
	return "this is a test"


if __name__ == '__main__':
	# 使用命令行的方式启动程序
	manager.run()


