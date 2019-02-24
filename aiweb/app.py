import os
import configparser
import logging
from klein import Klein
from twisted.internet import reactor
from aiweb.utils.ai_tools import ai_json_dumps, ai_json_loads
from aiweb.utils.ai_wraper import check_cors
import numpy as np
logger = logging.getLogger(__name__)


class Aiapi(object):
    """Class representing ai http server"""
    app = Klein()

    def __init__(self,
                 config_name=None,
                 ):
        self.root_path = os.getcwd()
        self.config_name = config_name
        self.predict_class = ""
        self.predict_func = ""
        self.config = {}
        self.cors_origins = "*"
        self.predict_func_args = []
        self.predict_func_kwargs = {}

        if self.root_path is None:
            raise Exception("You need to add the config file name!!!")

        self._make_config()

        self._configure_logging()
        reactor.suggestThreadPoolSize(16)

    def _configure_logging(self):
        logging.basicConfig(filename=self.config["log_file"],
                            level=self.config["log_level"])
        logging.captureWarnings(True)

    def save_args(self):
        """ save something """
        if not self.predict_func:
            raise Exception("Please add your predict function! ")

        for arg in self.predict_func_args:
            exec(arg + '= %r' % "")
            self.predict_func_kwargs[arg] = eval(arg)

    def _make_config(self):
        """ from config file import arguments"""
        conf = configparser.ConfigParser()
        conf.read(self.root_path + '/' + self.config_name)
        for key in conf.options("aiweb"):
            self.config[key.lower()] = conf.get("aiweb", key)

    def rebuild_router(self):
        if self.config.get("predict_class") or self.config.get("predict_func"):
            self.router.append("/parse")

    def run(self):
        self.save_args()
        self.app.run(self.config["host"], int(self.config['port']))

    @app.route("/", methods=['GET', 'OPTIONS'])
    @check_cors
    def hello(self, request):
        """ check if the server is online"""
        logger.info(request.getClientIP())
        return "Hello~ by clannadhh version 0.0.1"

    @app.route("/parse", methods=['GET', 'POST', 'OPTIONS'])
    @check_cors
    def parse(self, request):
        request.setHeader('Content-Type', 'application/json')
        if request.method.decode('utf-8', 'strict') == 'GET':
            return ai_json_dumps({"args": self.predict_func_args})
        else:
            try:
                request_params = request.content.read().decode('utf-8', 'strict')
                if request_params:
                    request_params = ai_json_loads(request_params)
                    for key in self.predict_func_args:
                        temp = request_params.get(key)
                        if temp:
                            self.predict_func_kwargs[key] = temp
                        else:
                            raise Exception("[Error] I can't find argument -> {}".format(key))
            except Exception as error:
                return ai_json_dumps({"error": str(error)})
        try:
            result = self.predict_func(**(self.predict_func_kwargs))
            
            if isinstance(result,np.ndarray):
                result = result.tolist()
                print(type(result))
        except Exception as error:
            result = str(error)
        return ai_json_dumps(result)

    @app.route("/version", methods=['GET', 'OPTIONS'])
    @check_cors
    def version(self, request):
        """Returns the aiweb server's version"""
        return "<h2>Welcome!!! ai-web_0.0.1<h2>"

