import logging, time
import logging.handlers
import configparser
import sys
rq = time.strftime('%Y%m%d', time.localtime(time.time()))
class Log(object):

    def __init__(self):
        pass

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls._instance = super(Log,cls).__new__(cls)
            cp = configparser.SafeConfigParser()
            cp.read('logging_config.ini')
            cls._instance.level = cp.get('logging', 'level')
            cls._instance.format = cp.get('logging', 'format')
            cls._instance.fmt = cls._instance.format.replace('|', '%')
            cls._instance.log_file = cp.get('logging', 'log_file')
            cls._instance.console_log_on = cp.getint('logging', 'console_log_on')
            cls._instance.logfile_log_on = cp.getint('logging', 'logfile_log_on')
            cls._instance.logger = logging.getLogger('test')
            cls._instance.write_log()
        return cls._instance

    def get_log(self):
        return self.logger

    def write_log(self):
        if self.logfile_log_on == 1:
            self.logger.setLevel(self.level)
            #设置文件输出log
            fh = logging.FileHandler(self.log_file)
            #设置输入的格式
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

        if self.console_log_on == 1:
            self.logger.setLevel(self.level)
            # 设置文件输出log
            sh = logging.StreamHandler()
            # 设置输入的格式
            formatter = logging.Formatter(self.fmt)
            sh.setFormatter(formatter)
            self.logger.addHandler(sh)




log = Log().get_log()