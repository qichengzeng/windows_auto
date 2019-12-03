from common.base_method import BaseMethod
from test_locator.start_dialog_locator import StartDialogLocator
from test_locator.patient_measurement_information_locator import PatientMeasurementInformationLocator
from test_locator.patient_search_locator import PatientSearchLocator
from test_locator.open_locator import OpenLocator
class StartDialogPage(BaseMethod):
    def query_new_button(self):
        """验证启动对话框中的新建按钮"""
        self.click(StartDialogLocator.new_loc,15,1)
        windows_controll=self.get_windows_control(PatientMeasurementInformationLocator.dialog_loc)
        act=self.get_control_name(windows_controll)
        return act

    def query_patient_search_button(self):
        """验证启动对话框中的患者检索按钮"""
        self.click(StartDialogLocator.patient_search_loc,15,1)
        windows_controll=self.get_windows_control(PatientSearchLocator.dialog_loc)
        self.controll_exitst(windows_controll,20,1)
        act=self.get_control_name(windows_controll)
        return act
    def query_open_button(self):
        """验证启动对话框中的打开按钮"""
        self.click(StartDialogLocator.open_loc,15,1)
        text_controll=self.get_text_control(OpenLocator.file_name_loc)
        act=self.get_control_name(text_controll)
        return act