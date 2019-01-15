import os
import configparser
import logging

from klein import Klein
from twisted.internet import reactor, threads
from aiweb.utils.ai_wraper import check_cors

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
        
        
        if self.root_path is None:
            raise "You need to add the config file path!!!"
        self._make_config()
        self._configure_logging()
        reactor.suggestThreadPoolSize(16)

    def _configure_logging(self):
        logging.basicConfig(filename=self.config["log_file"],
                            level=self.config["log_level"])
        logging.captureWarnings(True)
    
        
    def _make_config(self):
        conf = configparser.ConfigParser()
        conf.read(self.root_path + '/' +self.config_name)
        print(conf.sections())
        print(conf.options("default"))
        for key in conf.options("default"):         
            self.config[key] = conf.get("default",key)
        
        
    def run(self):     
        self.app.run(self.config["host"],int(self.config['port']))
    
    @app.route("/",methods=['GET', 'OPTIONS'])
    @check_cors
    def hello(self,request):
        logger.info(request.getClientIP())
        print(dir(request),request)
        print("Hello~ by clannadhh")
        return "Hello~ by clannadhh"
    
    @app.route("/parse",methods=['GET','POST','OPTIONS'])
    @check_cors
    def parse(self,request):
        return "parse"
    