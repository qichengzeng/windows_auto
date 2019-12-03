from pywinauto.application import Application
from pywinauto import findwindows
from common.get_logger import Logger
logger=Logger().get_logger()
class Base:
    def __init__(self,exe_path,backend="uia"):
        try:
            self.app=Application(backend=backend).start(cmd_line=exe_path)
            logger.info("{}程序启动成功".format(exe_path))
        except:
            logger.exception("{}程序启动失败".format(exe_path))
    def kill(self):
        try:
            self.app.kill()
            logger.info("成功关闭程序")
        except:
            logger.exception("关闭程序失败")
