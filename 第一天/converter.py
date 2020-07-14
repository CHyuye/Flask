"""
    视图函数——路由提取参数和自定义路由转换器
"""

from flask import Flask, url_for, redirect
# 从werkzeug.routing中导入转换器基类
from werkzeug.routing import BaseConverter

app = Flask(__name__)

"""
    转换器：
    int:接收整数
    float:同int，接收浮点数
    path:和默认一样，但接收斜线
"""

# 127.0.0.1:5000/goods/123
# @app.route("/goods/<int:goods_id>") int转换器类型 int:
@app.route("/goods/<goods_id>")  # 如果不加转换器类型，默认普通字符串规则(除了/的字符)
def goods_detail(goods_id):
    """定义视图函数"""
    return "goods detail page %s " % goods_id


# 1.定义自己的转换器——万能转换器，可以通过regex参数接收re正则
class RegexConverters(BaseConverter):
    """自定义转换器——继承BaseConverter"""

    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(RegexConverters, self).__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中，flask会使用这个属性来进行路由的正则匹配
        self.regex = regex

    def to_python(self, value):
        # print("该函数会被调用")
        # value是在路径进行的正则表达式匹配的时候提取出来的参数
        return value

    def to_url(self, value):
        pass


# 定义一个专门用于提取手机号的正则转换器
class PhoneNumConverters(BaseConverter):
    """定义一个提取手机号的转换器"""
    def __init__(self, url_map):
        super(PhoneNumConverters, self).__init__(url_map)
        self.regex = r"1[34578]\d{9}"


# 2.将自定义的转换器添加到flask应用中
app.url_map.converters["re"] = RegexConverters
# 将手机号的转换器添加到flask应用中
app.url_map.converters["phone"] = PhoneNumConverters

"""
127.0.0.1:5000/send/19946238583 --> 通过下面的转换器提取出phone_num=19946238583
--> 视图函数参数phone_num --> BaseConverter的to_python函数的value参数 --> 被返回到视图函数
"""
@app.route("/send/<re(r'1[34578]\d{9}'):phone_num>")
# @app.route("/send/<phone:phone_num>")
def send_sms(phone_num):
    """自定义匹配手机号码信息"""
    return "send your phone number is %s" % phone_num


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)