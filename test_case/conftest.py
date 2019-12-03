import pytest
from test_page.new_prompt_page import NewPromptPage
from test_page.import_lateral_slice_do_page import ImportLateralSliceDoPage
from test_page.new_patient_page import NewPatientPage
from common.get_logger import Logger
logger=Logger().get_logger()
@pytest.fixture(scope="class")
def new_prompt_precess():
    precess = NewPromptPage("C:\Program Files (x86)\E-Ceph\E-Ceph.exe")
    logger.info("程序启动成功")
    yield precess
    precess.close_exe()
    logger.info("本次测试结束")
    logger.info("\n")
@pytest.fixture(scope="class")
def import_lateral_slice_do_precess():
    precess=ImportLateralSliceDoPage("D:\ACEImage\Debug\E-Ceph.exe")
    logger.info("程序启动成功")
    yield precess
    precess.close_exe()
    logger.info("本次测试结束")
    logger.info("\n")
@pytest.fixture()
def new_patient_precess():
    precess =NewPatientPage("D:\ACEImage\Debug\E-Ceph.exe")
    logger.info("程序启动成功")
    yield precess
    precess.close_exe()
    logger.info("本次测试结束")
    logger.info("\n")

