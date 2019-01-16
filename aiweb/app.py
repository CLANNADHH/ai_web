import os
import configparser
import logging

from klein import Klein
from twisted.internet import reactor, threads
from aiweb.utils.ai_wraper import check_cors
from aiweb.utils.ai_wraper import check_route
from aiweb.utils.ai_path import *


logger = logging.getLogger(__name__)


class Aiapi(object):

    app = Klein()

    def __init__(self,
        config_name = None,
    ):
        self.root_path = os.getcwd()
        self.config_name = config_name
        self.conf = None
        self.config = {}
        self.cors_origins = "*"
        self.router=[]
        
        if self.root_path is None:
            raise "You need to add the config file name!!!"
        
        check_path()
        
        self._make_config()
        self.rebuild_router()
        
        self._configure_logging()
        reactor.suggestThreadPoolSize(16)

    def _configure_logging(self):
        logging.basicConfig(filename=self.config["log_file"],
                            level=self.config["log_level"])
        logging.captureWarnings(True)
    
    
    def check_path(self):
        if self.config.get("predict_class_path"):
            pass
        else:
            raise "Can't find predict_class_path o(╥﹏╥)o"
    
    def _make_config(self):
        conf = configparser.ConfigParser()
        conf.read(self.root_path + '/' +self.config_name)
        print(conf.sections())
        print(conf.options("default"))
        for key in conf.options("default"):         
            self.config[key] = conf.get("default",key)
        
    def rebuild_router(self):
        if self.config.get("predict_class") or self.config.get("predict_func"):
            self.router.append("/parse")
        
            
    def run(self):     
        self.app.run(self.config["host"],int(self.config['port']))
    
    @app.route("/",methods=['GET', 'OPTIONS'])
    @check_cors
    def hello(self,request):
        logger.info(request.getClientIP())
        return "Hello~ by clannadhh (*^▽^*)"
    
    @app.route("/parse",methods=['GET','POST','OPTIONS'])
    @check_cors
    @check_route
    def parse(self,request):
        return "parse"
        
    @app.route("/version",methods=['GET','OPTIONS'])
    @check_cors
    def parse(self,request):
        return "<h2>Welcome!!! ai-web_0.0.1<h2>"
    