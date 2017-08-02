import logging.handlers
import os
"""
logging.basicConfig(level=logging.DEBUG,
                    format = '%(asctime)s %(filename)s[line:%(lineno)d] % (levelname)s %(message)s',
                    datefmt='%a,%d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')
logging.debug('this is debug message')
logging.info('this is info message')
logging.warning('this is a warning message')

logging.basicConfig(level=logging.ERROR,
                    # format='%(asctime)s:%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # datefmt='%a, %d %b %Y %H:%M:%S',
                    filename = os.path.join(r','log.txt'),
                    filemode='w')
logging.info('msg')
logging.debug('msg22')
logging.warning('this is warnning')
logging.error('this is an error')
"""
import logging
import sys
import configparser

class Log:
    def __init__(self):
        pass

    def __new__(cls):
        if  not hasattr(cls,'instance'):
            cls._instance = super(Log, cls).__new__(cls)
            conf = configparser.ConfigParser()
            conf.read('log_config.ini',encoding='utf-8')
            cls._instance.level = conf.get('logging','level')
            cls._instance.name = conf.get('logging', 'logger_name')
            cls._instance.path = conf.get('logging', 'file_path')
            cls._instance.formatter = conf.get('logging', 'formatter')
            cls._instance.format = cls._instance.formatter.replace('|', '%')
            cls._instance.console_output_on = conf.getint('logging', 'console_output_on')
            cls._instance.file_output_on = conf.getint('logging', 'file_output_on')
            cls._instance.logger =logging.getLogger('test')
            cls._instance.log()
        return cls._instance


    def get_log(self):
        return self.logger


    def log(self):
        if self.console_output_on == 1:
            self.logger.setLevel(self.level)
            # 设置log.txt路径
            #设置控制台输出日志
            sh = logging.StreamHandler(sys.stderr)
            # 设置格式
            formatter = logging.Formatter(self.format)
            sh.setFormatter(formatter)
            self.logger.addHandler(sh)

        if  self.file_output_on==1:
            self.logger.setLevel(self.level)
            # 设置log.txt路径
            # 设置文件输入日志地址
            #最多备份5个日志文件，每个日志文件最大10M,这个Handler类似于上面的FileHandler，但是它可以管理文件大小。
            # 当文件达到一定大小之后，它会自动将当前日志文件改名，然后创建 一个新的同名日志文件继续输出
            #fh = logging.RotatingFileHandler(self.path,maxBytes=10*1024*1024,backupCount=5)
            fh = logging.FileHandler(self.path)
            # 设置格式
            formatter = logging.Formatter(self.format)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
            return self.logger




log = Log().get_log()
