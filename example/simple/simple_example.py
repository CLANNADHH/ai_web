# 导入aiweb
from aiweb import Aiapi

# 算法部分
class AiTest(object):

	# 预测函数
    def parse(self,aaa,bbb=None):
        return aaa

# 实例化aiweb
ai = Aiapi("config.ini")

# 算法类实例化并赋值
ai.predict_class = AiTest()

# 算法预测函数赋值
ai.predict_func = AiTest.parse

# 在列表中添加预测函数所需要传递的参数名字，类型为 str
ai.predict_func_args = ["aaa"]

# 启动http服务
ai.run()