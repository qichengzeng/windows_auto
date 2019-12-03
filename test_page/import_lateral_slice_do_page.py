from common.base_method import BaseMethod
from test_locator.import_lateral_slice_do_locator import ImportLateralSliceDoLocator
from test_locator.start_dialog_locator import StartDialogLocator
class ImportLateralSliceDoPage(BaseMethod):
    def base_method(self):
        text_control = self.get_text_control(ImportLateralSliceDoLocator.prompt_slice__loc)
        act = self.get_control_name(text_control)
        self.close(ImportLateralSliceDoLocator.prompt_loc)
        return act
    def base_method_positive(self):
        text_control = self.get_text_control(ImportLateralSliceDoLocator.prompt_slice_positive_loc)
        act = self.get_control_name(text_control)
        self.close(ImportLateralSliceDoLocator.prompt_loc)
        return act
    def query_two_point_one(self):
        self.close(StartDialogLocator.dialog)
        self.click(ImportLateralSliceDoLocator.two_point_one_loc)
        act=self.base_method()
        return act
    def query_two_point_two(self):
        # self.click(StartDialogLocator.dialog)
        self.click(ImportLateralSliceDoLocator.two_point_tow_loc)
        act=self.base_method()
        return act
    def query_three_point_angle(self):
        # self.click(StartDialogLocator.dialog)
        self.click_next_control(ImportLateralSliceDoLocator.two_point_tow_loc)
        act=self.base_method()
        return act
    def query_four_point_move(self):
        # self.click(StartDialogLocator.dialog)
        self.click(ImportLateralSliceDoLocator.four_move_loc)
        act=self.base_method()
        return act
    def query_two_point_one_positive(self):
        self.click(ImportLateralSliceDoLocator.positive_loc)
        self.click(ImportLateralSliceDoLocator.two_point_one_loc)
        act=self.base_method_positive()
        return act
    def query_two_point_two_positive(self):
        # self.click(StartDialogLocator.dialog)
        self.click(ImportLateralSliceDoLocator.two_point_tow_loc)
        act=self.base_method_positive()
        return act
    def query_three_point_angle_positive(self):
        # self.click(StartDialogLocator.dialog)
        self.click_next_control(ImportLateralSliceDoLocator.two_point_tow_loc)
        act=self.base_method_positive()
        return act
    def query_four_point_move_positive(self):
        # self.click(StartDialogLocator.dialog)
        self.click(ImportLateralSliceDoLocator.four_move_loc)
        act=self.base_method_positive()
        return act