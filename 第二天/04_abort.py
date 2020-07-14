"""
    abort函数介绍：可以立即终止视图函数的进行，并可以返回给前端特定信息
"""

from flask import Flask, request, abort, Response


app = Flask(__name__)


def login():
    # name = request.form.get()
    # pwd = request.form.get()
    name = ""
    pwd = ""
    if name != "chenhan" or pwd != "virgin":
        # 使用abort函数可以立即终止视图函数进行,并可以返回会前端特定信息
        # 1.传递状态码信息，必须是标准的http状态码, 一般来说，方式一比较好
        abort(404)

        # 2.传递响应体信息
        # resp = Response("You seeking file in the sky.")
        # abort(resp)

    return " This is login page, please register a new customer!"


# 自定义错误处理显示信息
@app.errorhandler(404)
def handle_404_error(error):
    """自定义处理错误404页面方法"""
    return "唉呀妈呀，出现错误了！错误原因:{}".format(error)


if __name__ == '__main__':
    app.run(debug=True)
