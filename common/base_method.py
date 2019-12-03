import uiautomation as auto
from common.get_logger import Logger
import subprocess
from test_locator.wby import Wby
logger=Logger().get_logger()
class BaseMethod:
    def __init__(self,exe_path):
        self.process=subprocess.Popen(exe_path)
    def get_windows_control(self,loc):
        try:
             if loc[0]==Wby.NAME:
                windows_control=auto.WindowControl(searchDepth=loc[2],Name=loc[1])
                logger.info("深度为_{}_，名字为_{}__的windows_control获取成功".format(loc[2],loc[1]))
                return windows_control
             if loc[0]==Wby.AUTOMATIONID:
                 windows_control = auto.WindowControl(searchDepth=loc[2], AutomationId=loc[1])
                 logger.info("深度为_{}_，id为_{}__的windows_control获取成功".format(loc[2],loc[1]))
                 return windows_control
        except:
            if loc[0]==Wby.NAME:
               logger.exception("深度为_{}_，名字为_{}__的windows_control获取失败".format(loc[2],loc[1]))
            if loc[0]==Wby.AUTOMATIONID:
               logger.exception("深度为_{}_，id为_{}__的windows_control获取失败".format(loc[2],loc[1]))
    def get_text_control(self,loc):
        try:
             if loc[0]==Wby.NAME:
                text_control=auto.TextControl(searchDepth=loc[2],Name=loc[1])
                logger.info("深度为_{}_，名字为_{}__的text_control获取成功".format(loc[2],loc[1]))
                return text_control
             if loc[0]==Wby.AUTOMATIONID:
                 text_control = auto.TextControl(searchDepth=loc[2], AutomationId=loc[1])
                 logger.info("深度为_{}_，id为_{}__的text_control获取成功".format(loc[2],loc[1]))
                 return text_control
        except:
            if loc[0]==Wby.NAME:
               logger.exception("深度为_{}_，名字为_{}__的text_control获取失败".format(loc[2],loc[1]))
            if loc[0]==Wby.AUTOMATIONID:
               logger.exception("深度为_{}_，id为_{}__的text_control获取失败".format(loc[2],loc[1]))
    def get_button_control(self,loc):
        try:
            if loc[0]==Wby.NAME:
                button_control = auto.ButtonControl(searchDepth=loc[2], Name=loc[1])
                logger.info("深度为_{}_，名字为_{}__的button_control获取成功".format(loc[2],loc[1]))
                return button_control
            if loc[0]==Wby.AUTOMATIONID:
                button_control = auto.ButtonControl(searchDepth=loc[2], AutomationId=loc[1])
                logger.info("深度为_{}_，id为_{}__的button_control获取成功".format(loc[2],loc[1]))
                return button_control
        except:
            if loc[0]==Wby.NAME:
                logger.exception("深度为_{}_，名字为_{}__的button_control获取失败".format(loc[2],loc[1]))
            if loc[0]==Wby.AUTOMATIONID:
                logger.exception("深度为_{}_，名字为_{}__的button_control获取失败".format(loc[2],loc[1]))
    def get_edit_control(self,loc):
        try:
            if loc[0]==Wby.NAME:
                edit_control = auto.EditControl(searchDepth=loc[2], Name=loc[1])
                logger.info("深度为_{}_，名字为_{}__的edit_control获取成功".format(loc[2],loc[1]))
                return edit_control
            if loc[0]==Wby.AUTOMATIONID:
                edit_control=auto.EditControl(searchDepth=loc[2],AutomationId=loc[1])
                logger.info("深度为_{}_，id为_{}__的edit_control获取成功".format(loc[2],loc[1]))
                return edit_control
        except:
            if loc[0]==Wby.NAME:
                logger.exception("深度为_{}_，名字为_{}__的edit_control获取失败".format(loc[2],loc[1]))
            if loc[0]==Wby.AUTOMATIONID:
                logger.exception("深度为_{}_，名字为_{}__的edit_control获取失败".format(loc[2],loc[1]))
    def get_pane_control(self,loc):
        try:
            if loc[0]==Wby.NAME:
                pane_control = auto.PaneControl(searchDepth=loc[2], Name=loc[1])
                logger.info("深度为_{}_，名字为_{}__的pane_control获取成功".format(loc[2],loc[1]))
                return pane_control
            if loc[0]==Wby.AUTOMATIONID:
                pane_control=auto.PaneControl(searchDepth=loc[2],AutomationId=loc[1])
                logger.info("深度为_{}_，id为_{}__的Pane_control获取成功".format(loc[2],loc[1]))
                return pane_control
        except:
            if loc[0]==Wby.NAME:
                logger.exception("深度为_{}_，名字为_{}__的pane_control获取失败".format(loc[2],loc[1]))
            if loc[0]==Wby.AUTOMATIONID:
                logger.exception("深度为_{}_，名字为_{}__的pane_control获取失败".format(loc[2],loc[1]))
    def get_menuItem_control(self,loc):
        try:
            if loc[0]==Wby.NAME:
                menuItem_control = auto.MenuItemControl(searchDepth=loc[2], Name=loc[1])
                logger.info("深度为_{}_，名字为_{}__的menuItem_control获取成功".format(loc[2], loc[1]))
                return menuItem_control
            if loc[0]==Wby.AUTOMATIONID:
                menuItem_control = auto.MenuItemControl(searchDepth=loc[2],AutomationId=loc[1])
                logger.info("深度为_{}_，id为_{}__的menuItem_control获取成功".format(loc[2],loc[1]))
                return menuItem_control
        except:
            if loc[0]==Wby.NAME:
                logger.exception("深度为_{}_，名字为_{}__的menuItem_control获取失败".format(loc[2],loc[1]))
            if loc[0]==Wby.AUTOMATIONID:
                logger.exception("深度为_{}_，名字为_{}__的menuItem_control获取失败".format(loc[2],loc[1]))
    def get_image_control(self,loc):
        try:
            if loc[0]==Wby.NAME:
                image_control = auto.ImageControl(searchDepth=loc[2], Name=loc[1])
                logger.info("深度为_{}_，名字为_{}__的image_control获取成功".format(loc[2], loc[1]))
                return image_control
            if loc[0]==Wby.AUTOMATIONID:
                image_control=auto.ImageControl(searchDepth=loc[2],AutomationId=loc[1])
                logger.info("深度为_{}_，id为_{}__的image_control获取成功".format(loc[2],loc[1]))
                return image_control
        except:
            if loc[0]==Wby.NAME:
                logger.exception("深度为_{}_，名字为_{}__的image_control获取失败".format(loc[2],loc[2]))
            if loc[0]==Wby.AUTOMATIONID:
                logger.exception("深度为_{}_，名字为_{}__的image_control获取失败".format(loc[2],loc[2]))
    def click_next_control(self,loc,maxseconds=5,intervalseconds=1,wait_time=0.5):
        try:
            if loc[0]==Wby.NAME:
                button_control=self.get_button_control(loc).GetNextSiblingControl().Click(waitTime=wait_time)
                logger.info("深度为_{}_，名字为_{}__的下一个button_control点击成功".format(loc[2],loc[1]))
            if loc[0]==Wby.AUTOMATIONID:
                button_control=self.get_button_control(loc).GetNextSiblingControl().Click()
                logger.info("深度为_{}_，id为_{}__的下一个button_control点击成功".format(loc[2], loc[1]))
        except:
            if loc[0]==Wby.NAME:
                logger.exception("深度_{}_，名字_{}_的下一个button_control点击失败".format(loc[2],loc[1]))
            if loc[0]==Wby.AUTOMATIONID:
                logger.exception("深度_{}_,id_{}_的下一个button_control点击失败".format(loc[2],loc[1]))
    def click_first_child_control(self,loc,maxseconds=5,intervalseconds=1,wait_time=0.5):
        try:
            if loc[0]==Wby.NAME:
                control=self.get_pane_control(loc).GetFirstChildControl().Click(waitTime=wait_time)
                logger.info("深度为_{}_，名字为_{}__的第一个子control点击成功".format(loc[2],loc[1]))
            if loc[0]==Wby.AUTOMATIONID:
                control=self.get_pane_control(loc).GetFirstChildControl().Click()
                logger.info("深度为_{}_，id为_{}__的第一个子control点击成功".format(loc[2], loc[1]))
        except:
            if loc[0]==Wby.NAME:
                logger.exception("深度_{}_，名字_{}_的第一个子control点击失败".format(loc[2],loc[1]))
            if loc[0]==Wby.AUTOMATIONID:
                logger.exception("深度_{}_,id_{}_的第一个子control点击失败".format(loc[2],loc[1]))
    def click(self,loc,maxseconds=5,intervalseconds=0.5):
        try:
            if loc[0]==Wby.NAME:
                button_control=self.get_button_control(loc)
                if not button_control.Exists(maxSearchSeconds=maxseconds, searchIntervalSeconds=intervalseconds):
                    logger.info("{}_controll不存在".format(button_control))
                button_control.Click()
                logger.info("深度为_{}_，名字为_{}__的button_control点击成功".format(loc[2],loc[1]))
            if loc[0]==Wby.AUTOMATIONID:
                button_control=self.get_button_control(loc)
                if not button_control.Exists(maxSearchSeconds=maxseconds, searchIntervalSeconds=intervalseconds):
                    logger.info("{}_controll不存在".format(button_control))
                button_control.Click()
                logger.info("深度为_{}_，id为_{}__的button_control点击成功".format(loc[2], loc[1]))
        except:
            if loc[0]==Wby.NAME:
                logger.exception("深度_{}_，名字_{}_的button_control点击失败".format(loc[2],loc[1]))
            if loc[0]==Wby.AUTOMATIONID:
                logger.exception("深度_{}_,id_{}_的button_control点击失败".format(loc[2],loc[1]))
    def click_by_position(self,x,y):
        try:
            auto.Click(x,y)
            logger.info("x坐标_{}_，y坐标_{}_点击成功".format(x,y))
        except:
            logger.exception("x坐标_{}_，y坐标_{}_点击失败".format(x,y))
    def drag_drop(self,x1,y1,x2,y2):
        try:
            auto.DragDrop(x1,y1,x2,y2)
            logger.info("UiElement从x_{}_，y_{}_，拖动到x_{}_,y_{}_成功".format(x1,y1,x2,y2))
        except:
            logger.exception("UiElement从x_{}_，y_{}_，拖动到x_{}_,y_{}_成功".format(x1,y1,x2,y2))
    def senk_keys(self,loc,value,seconds=5,interval_seconds=0.5):
        try:
            if loc[0]==Wby.NAME:
                edit_control=self.get_edit_control(loc)
                if not edit_control.Exists(seconds,interval_seconds):
                    logger.info("深度_{}_，名字_{}_的edit_control获取失败".format(loc[2],loc[1]))
                edit_control.Click()
                self.clear_text(edit_control)
                edit_control.SendKeys(value)
                logger.info("深度_{}_，名字_{}_的edit_control发_{}_成功".format(loc[2],loc[1],value))
            if loc[0]==Wby.AUTOMATIONID:
                edit_control = self.get_edit_control(loc)
                if not edit_control.Exists(seconds, interval_seconds):
                    logger.info("深度_{}_，id_{}_的edit_control获取失败".format(loc[2],loc[1]))
                edit_control.Click()
                edit_control.SendKeys(value)
                logger.info("深度_{}_，id_{}_的edit_control发_{}_成功".format(loc[2],loc[1], value))
        except:
            if loc[0]==Wby.NAME:
                logger.exception("深度_{}_，name_{}_的edit_control发_{}_失败".format(loc[2],loc[1],value))
            if loc[0]==Wby.AUTOMATIONID:
                logger.exception("深度_{}_，id_{}_的edit_control发_{}_失败".format(loc[2],loc[1],value))
    def senk_key(self,key_word):
        try:
            auto.SendKey(key_word)
            logger.info("按下_{}_键成功".format(key_word))
        except:
            logger.exception("按下_{}_键失败".format(key_word))
    def clear_text(self,edit_control):
        try:
            # edit_control.Click()
            auto.SendKeys("{Ctrl}a{Delete}")
            logger.info("{}_edit_control中内容清除成功")
        except:
            logger.exception("{}_edit_control中内容清除失败")
    def close(self,loc,seconds=5,interval_seconds=0.5):
        try:
            windows_control = self.get_windows_control(loc)
            # if not windows_control.Exists(seconds, interval_seconds):
            #     logger.info("深度_{}_，名字_{}_的windows_control获取失败".format(loc[2],loc[1]))
            windows_control.GetWindowPattern().Close()
            logger.info("深度_{}_，名字_{}_的windows_control窗口关闭成功".format(loc[2],loc[1]))
        except:
            logger.exception("深度_{}_，名字_{}_的windows_control窗口关闭失败".format(loc[2],loc[1]))
    def close_exe(self):
        try:
            self.process.kill()
            logger.info("程序关闭成功")
        except:
            logger.exception("程序关闭失败")
    def get_edit_value(self,loc):
        try:
            if loc[0]==Wby.NAME:
                edit_control=self.get_edit_control(loc)
                value=edit_control.GetValuePattern().Value
                logger.info("深度_{}_，名字_{}_，的edit_control获_{}_文本成功".format(loc[2],loc[1],value))
                return value
            if loc[0]==Wby.AUTOMATIONID:
                edit_control=self.get_edit_control(loc)
                value=edit_control.GetValuePattern().Value
                logger.info("深度_{}_，名字_{}_，的edit_control获_{}_文本成功".format(loc[2],loc[1],value))
                return value
        except:
              if loc[0]==Wby.NAME:
                  logger.exception("深度_{}_，名字_{}_，的edit_control获_{}_文本失败".format(loc[2],loc[1]))
              if loc[0]==Wby.AUTOMATIONID:
                  logger.exception("深度_{}_，id_{}_，的edit_control获_{}_文本失败".format(loc[2],loc[1],value))
    def get_text_value(self,any_control,id=30093):
         try:
                value=any_control.GetPropertyValue(id)
                logger.info("{}_control的文本值获取成功为_{}".format(any_control,value))
                return value
         except:
                logger.exception("{}_control的文本值获取失败".format(any_control))
    def get_control_name(self,any_control,maxseconds=5,intervalseconds=0.02):
        try:
            if not any_control.Exists(maxSearchSeconds=maxseconds, searchIntervalSeconds=intervalseconds):
                logger.info("{}_controll不存在".format(any_control))
            name_value=any_control.Name
            logger.info("获_{}_的名字成功_{}_".format(any_control,name_value))
            return name_value
        except:
            logger.exception("获_{}_的名字失败".format(any_control))
    def get_all_child_control(self,any_control):
        try:
            list_control=any_control.GetChildren()
            logger.info("获_{}__control的所有子control成功_{}_".format(any_control,list_control))
        except:
            logger.exception("获_{}__control的所有子control失败".format(any_control))
    def get_firstChild_control(self,any_control):
        try:
            child_control=any_control.GetFirstChildControl()
            logger.info("获取child_contro_{}_成功".format(child_control))
            return child_control
        except:
            logger.exception("获取child_control失败")
    def get_previous_control(self,any_control):
        try:
            previous_control=any_control.GetPreviousSiblingControl()
            logger.info("获_{}_control的上一_{}_control成功".format(any_control,previous_control))
        except:
            logger.exception("获_{}_control的上一个control失败".format(any_control))
    def get_next_control(self,any_control):
        try:
            next_control=any_control.GetNextSiblingControl()
            logger.info("获_{}_control的下一_{}_control成功".format(any_control,next_control))
        except:
            logger.exception("获_{}_control的下一个control失败".format(any_control))
    def press_keyboard(self,key,any_control):
        try:
            any_control.SendKey(key)
            logger.info("_{}_按键成功".format(key))
        except:
            logger.exception("_{}_按键失败".format(key))
    def set_focus(self,any_control):
        try:
            any_control.SetFocus()
            logger.info("设置焦点聚集成功")
        except:
            logger.exception("设置焦点聚集失败")
    def wheel_down(self,any_control):
        try:
            any_control.WheelDown()
            logger.info("向下滚动滚轮成功")
        except:
            logger.exception("向下滚动滚轮失败")
    def wheel_up(self,any_control):
        try:
            any_control.WheelUp()
            logger.info("向上滚动滚轮成功")
        except:
            logger.exception("向上滚动滚轮失败")
    def set_clipboard_text(self,value):
        try:
            auto.SetClipboardText(value)
            logger.info("{}_设置成剪切板内容成功".format(value))
        except:
            logger.exception("_{}_设置成剪切板内容失败".format(value))
    def copy_from_clipboard(self):
        try:
            auto.SendKeys("{Ctrl}v")
            logger.info("从剪切板复制内容成功")
        except:
            logger.exception("从剪切板复制内容失败")
    def controll_exitst(self,anycontroll,maxseconds=5,intervalseconds=1):
        try:
            if not anycontroll.Exists(maxSearchSeconds=maxseconds,searchIntervalSeconds=intervalseconds):
                logger.info("{}_controll不存在".format(anycontroll))
        except:
            logger.exception("{}_controll不存在".format(anycontroll))
