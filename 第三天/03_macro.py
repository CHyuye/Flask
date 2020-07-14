"""
	模板宏：就相当于Django模板的继承原则，抽出一个父模板，重复调用
"""
from flask import Flask, render_template, flash


app = Flask(__name__)

# 模板闪现的使用
flag = True

app.config["SECRET_KEY"] = "fjv9airefjpohawp9ejpo"


@app.route("/")
def macro():
	if flag:
		# 添加闪现信息
		flash("闪现提示一")
		flash("闪现提示二")
		flash("闪现提示三")
		global flag
		flag = False
	return render_template("macro.html")


if __name__ == '__main__':
	app.run(debug=True)
