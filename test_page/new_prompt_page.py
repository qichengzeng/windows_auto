from common.base_method import BaseMethod
from test_locator.e_ceph_locator import ECephLocator
from test_locator.start_dialog_locator import StartDialogLocator
import time
class NewPromptPage(BaseMethod):
    def query_lateral_slice_prompt(self):
        """验证在没有新建患者时倒入侧光片提示功能"""
        self.close(StartDialogLocator.dialog,seconds=15,interval_seconds=1)
        self.click(ECephLocator.lateral_slice_introduction_loc)
        text_control=self.get_text_control(ECephLocator.new_prompt_loc)
        act=self.get_control_name(text_control)
        return act
    def query_positive_slice_prompt(self):
        """验证在没有新建患者时倒入正位光片提示功能"""
        # self.close(StartDialogLocator.dialog, seconds=15, interval_seconds=1)
        time.sleep(2)
        self.click_next_control(ECephLocator.lateral_slice_introduction_loc)
        text_control = self.get_text_control(ECephLocator.new_prompt_loc)
        act = self.get_control_name(text_control)
        return act
    def query_save_button_prompt(self):
        """验证在没有新建患者时点击保存按钮"""
        # self.close(StartDialogLocator.dialog, seconds=15, interval_seconds=1)
        time.sleep(2)
        self.click(ECephLocator.save_loc)
        text_control = self.get_text_control(ECephLocator.new_prompt_loc)
        act = self.get_control_name(text_control)
        return act