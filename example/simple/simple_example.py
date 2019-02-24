from aiweb import Aiapi


class AiTest(object):

    def parse(self, aaa):
        return "lol"
        
ai = Aiapi("config.ini")
ai.predict_class = AiTest
ai.predict_func = AiTest.parse
ai.predict_func_args = ["aaa"]
ai.run()