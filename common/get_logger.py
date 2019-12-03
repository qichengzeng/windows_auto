import logging
from common.all_of_path import logger_path
class Logger:
    def __init__(self,name="e_ceph"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        #添加文件日志和控制台日志
        self.filehandler=logging.FileHandler(filename=logger_path,mode="w+",encoding="utf-8")
        self.consolehandler=logging.StreamHandler()
        #为文件日志和控制台日志添加日志级别
        self.filehandler.setLevel("INFO")
        self.consolehandler.setLevel("DEBUG")
        #文件日志处理器和控制台日志处理器添加日志输出格式
        formatt = logging.Formatter("%(asctime)s____%(name)s___%(levelname)s___%(message)s")#___[%(filename)s:%(lineno)d]
        self.filehandler.setFormatter(formatt)
        self.consolehandler.setFormatter(formatt)
        self.logger.addHandler(self.filehandler)
        self.logger.addHandler(self.consolehandler)
        self.filehandler.close()
        self.consolehandler.close()
    def get_logger(self):
        return self.logger
    def remove_handle(self):
        self.logger.removeHandler(self.consolehandler)
        self.logger.removeHandler(self.filehandler)
if __name__ == '__main__':
   l=Logger()
   t=l.get_logger()
   t.info("我是info1信息")
   t.info("我是info2信息")
   # t.exception("超时异常")
   # l.remove_handle()
