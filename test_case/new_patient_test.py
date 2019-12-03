from common.get_logger import Logger
from test_page.new_patient_page import NewPatientPage
from test_data.new_patient_data import query_prompt_name_data,query_prompt_birth_data,query_prompt_doctor_name_data,query_prompt_doctor_name_clear_data
import pytest
logger=Logger().get_logger()
@pytest.mark.usefixtures("new_patient_precess")
class TestNewPatient:
    @pytest.mark.parametrize("data",query_prompt_name_data)
    def test_new_patient_name(self,data,new_patient_precess):
        logger.info("{}_用例开始测试".format(data["title"]))
        act = new_patient_precess.query_prompt_name(data["key_word"],data["doctor_name"])
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e

    @pytest.mark.parametrize("data",query_prompt_birth_data)
    def test_new_patient_birth(self, data, new_patient_precess):
        logger.info("{}_用例开始测试".format(data["title"]))
        act = new_patient_precess.query_prompt_birth(data["name"], data["doctor_name"])
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e

    @pytest.mark.parametrize("data", query_prompt_doctor_name_data)
    def test_new_patient_doctor_name(self, data, new_patient_precess):
        logger.info("{}_用例开始测试".format(data["title"]))
        act = new_patient_precess.query_prompt_doctor_name(data["name"], data["key_word"])
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e

    @pytest.mark.parametrize("data", query_prompt_doctor_name_clear_data)
    def test_new_patient_doctor_name_clear(self, data, new_patient_precess):
        logger.info("{}_用例开始测试".format(data["title"]))
        act = new_patient_precess.query_doctor_name_clear(data["doctor_name"])
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e