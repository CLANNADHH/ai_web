# API自动生成

----------
## 1.项目介绍：
&emsp;&emsp;你是否有过这样的苦恼？训练好了模型，想封装成web接口,让人家去使用，缺不知道如何下手。放心，拥有了这个，你就可以不用关系web接口如何编写了。
## 2.版本支持：
&emsp;python3.5 +
## 3.使用方法 
- 3.1通过pip安装或者通过下载本源码安装。

- 3.2开始使用aiweb
	[代码传送门](https://github.com/CLANNADHH/ai_web/tree/master/example/simple)

 -  下面是一个简单的例子
   - 3.2.1 主程序部分  
   
    -  ``` python
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
    ```
   - 3.2.2 编写配置文件
   
   -  ``` python
	[aiweb]
	# server ip addr
	HOST = 127.0.0.1
	
	# server ip port
	PORT = 1234
	
	# log level # info error warning
	LOG_LEVEL = INFO
	
	# log file name
	LOG_FILE = aiweb.log
    ```
   - 3.2.3 运行你的代码
    
		> 命令行输入  `python simple_example.py` 
		
		> 你可以在浏览器输入  `http://127.0.0.1:1234` 看到下图信息表示你已经成功构建了web接口
		> 
		![返回信息](/image/hello.png)
 
   - 3.2.4 通过**Postman**调用接口预测

		![简单解析](/image/simple_parse.png)

  - 另一个例子： 
  	代码为使用 **sklearn** 预测波士顿房价并使用 **aiweb** 自动生成预测接口
	- [代码传送门](https://github.com/CLANNADHH/ai_web/tree/master/example/boston)
    
	 ![返回信息](/image/boston.png)





----------
# 如果觉得项目还不错，可以star一波。 #
