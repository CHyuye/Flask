"""
	上传文件——此处展示上传图片操作
"""
from flask import Flask, request


app = Flask(__name__)


@app.route("/upload", methods=["POST", "GET"])
def upload():
	"""接收前端传送过来的文件"""
	file_obj = request.files.get("pic")  # pic为前端指定的传输名字
	if file_obj is None:
		return "上传文件失败！"

	# 将上传文件保存到本地
	# # 1.创建一个文件
	# f = open("./demo.png", "wb")
	# # 2.读取传输文件内容
	# file_data = f.read(file_obj)
	# # 3.写入，保存本地
	# f.write(file_data)
	# # 4.关闭文件
	# f.close()

	# 方法二
	# with open("./demo/png", "wb") as f:
	# 	 	file_data = f.read(file_obj)
	# 	 	f.write(file_data)

	# 方法三
	# 直接使用file_obj上传文件对象调用保存方法
	file_obj.save("./demo.png")
	return "文件上传成功！"


if __name__ == '__main__':
	app.run(debug=True)
