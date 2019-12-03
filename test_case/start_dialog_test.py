from common.get_logger import Logger
from test_page.start_dialog_page import StartDialogPage
from test_data.start_dialog_data import new_data,patients_search_data,open_data
import pytest
logger=Logger().get_logger()
class TestStartDialog:
    @pytest.mark.parametrize("data",new_data)
    def test_new_button(self,data):
        """验证启动对话框中的新建按钮"""
        logger.info("{}_用例开始测试".format(data["title"]))
        precess=StartDialogPage("C:\Program Files (x86)\E-Ceph\E-Ceph.exe")
        act = precess.query_new_button()
        precess.close_exe()
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e

    @pytest.mark.parametrize("data",patients_search_data)
    def test_patient_search_button(self, data):
        """验证启动对话框中的患者查询按钮"""
        logger.info("{}_用例开始测试".format(data["title"]))
        precess= StartDialogPage("C:\Program Files (x86)\E-Ceph\E-Ceph.exe")
        act = precess.query_patient_search_button()
        precess.close_exe()
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e
    @pytest.mark.parametrize("data",open_data)
    def test_open_button(self, data):
        """验证启动对话框中的患者打开按钮"""
        logger.info("{}_用例开始测试".format(data["title"]))
        precess = StartDialogPage("C:\Program Files (x86)\E-Ceph\E-Ceph.exe")
        act = precess.query_open_button()
        precess.close_exe()
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e