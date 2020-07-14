from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)


class Config(object):
	# sqlalchemy的配置参数
	# SQLALCHEMY_DATABASE_URI = "mysql+pymsql"此处的mysql和pymsql都是链接MySQL的
	# SQLALchemy只是用来将模型类转换为sql语句，mysql+pymsql将sql语句添加到数据库，前提创建一个对应的数据库author
	SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@192.168.232.136:3306/author_book"

	# 设置sqlalchemy自动更跟踪数据库
	SQLALCHEMY_TRACK_MODIFICATIONS = True

	SECRET_KEY = "doiso7fd89fyd9asdfavre"


app.config.from_object(Config)

db = SQLAlchemy(app)


# 定义数据库的模型
class Author(db.Model):
	"""作者"""
	__tablename__ = "tbl_authors"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(32), unique=True)
	books = db.relationship("Book", backref="author")


class Book(db.Model):
	"""书籍"""
	__tablename__ = "tbl_books"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	author_id = db.Column(db.Integer, db.ForeignKey("tbl_authors.id"))


# 定义表单模型类
class AuthorBookForm(FlaskForm):
	# 作者数据表单模型
	author_name = StringField(label="作者", validators=[DataRequired("请填写作者名")])
	book_info = StringField(label="书名", validators=[DataRequired("请填写书名")])
	submit = SubmitField(label="保存")


@app.route("/", methods=["POST", "GET"])
def index():
	# 创建表单模型
	form = AuthorBookForm()

	if form.validate_on_submit():
		# 验证表单通过，提取表单数据
		author_name = form.author_name.data
		book_info = form.book_info.data

		# 保存数据库
		author = Author(name=author_name)
		db.session.add(author)
		db.session.commit()

		book = Book(name=book_info, author_id=author.id)
		# book = Book(name=book_info, author=author) 因为前面设置好了backref
		db.session.add(book)
		db.session.commit()

	# 查询数据库
	author_li = Author.query.all()
	return render_template("author_book.html", authors=author_li, form=form)


# post请求 /delete_book  json  --> {"book_id": x}
@app.route("/delete_book", methods=["POST"])
def delete_book():
	"""删除图书记录"""
	# 提取参数
	# 如果前端发送过来的请求体数据是Json格式，get_json()转化为json
	# get_json 要求前端传送的数据Content-Type: application/json
	rep_dict = request.get_json()
	book_id = rep_dict.get("book_id")

	# 删除数据
	book = Book.query.get(book_id)
	db.session.delete(book)
	db.session.commit()

	# "Content-Type":"application/json"
	return jsonify(code=0, message="OK")


# GET请求，查询字符串的方式 /delete_book?bood_id=xx
# @app.route("/delete_book", methods=["GET"])
# def delete_book():
# 	"""删除数据"""
# 	# 提取参数
# 	book_id = request.args.get("book_id")
#
# 	# 删除数据
# 	book = Book.query.get(book_id)
# 	db.session.delete(book)
# 	db.session.commit()
#
# 	return redirect(url_for("index"))


if __name__ == "__main__":
	# todo 先把这些模型类数据添加到数据库
	# db.drop_all()
	# db.create_all()
	# au_xi = Author(name='我吃西红柿')
	# au_qian = Author(name='萧潜')
	# au_san = Author(name='唐家三少')
	# db.session.add_all([au_xi, au_qian, au_san])
	# db.session.commit()
	#
	# bk_xi = Book(name='吞噬星空', author_id=au_xi.id)
	# bk_xi2 = Book(name='寸芒', author_id=au_qian.id)
	# bk_qian = Book(name='飘渺之旅', author_id=au_qian.id)
	# bk_san = Book(name='冰火魔厨', author_id=au_san.id)
	# db.session.add_all([bk_xi, bk_xi2, bk_qian, bk_san])
	# db.session.commit()

	app.run(debug=True)
