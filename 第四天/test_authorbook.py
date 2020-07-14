"""
	单元测试之数据库测试
	测试author_book案例中的数据库操作
"""
import unittest
from author_book import app, db, Author, Book


class DatabaseTest(unittest.TestCase):
	def setUp(self):
		# 测试模式
		app.testing = True
		# 配置一个空数据库
		app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/flask_test"
		# 创建数据内容
		db.create_all()

	def test_add_author(self):
		"""测试添加作者的数据库操作"""
		author = Author(name="chenhan")
		db.session.add(author)
		db.session.commit()

		# 查询数据库，接收返回值
		result_author = Author.query.filter_by(name="chenhan").first()
		# 断言，结果存在
		self.assertIsNotNone(result_author)

	def test_add_book(self):
		"""测试添加图书数据库操作"""
		book = Book(name="偷影子的人")
		db.session.add(book)
		db.session.commit()

		# 查询数据库，接收返回值
		result_book = Book.query.filter_by(name="偷影子的人").first()
		# 断言。结果存在
		self.assertIsNotNone(result_book)

	def tearDown(self):
		"""这个内置方法，会在所有测试执行后，执行，通常用来清理操作"""
		# 断开数据库连接
		db.session.remove()
		# 清空数据库数据
		db.drop_all()


if __name__ == '__main__':
	# 执行所有测试函数
	unittest.main()


