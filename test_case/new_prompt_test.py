from common.get_logger import Logger
from test_page.new_prompt_page import NewPromptPage
from test_data.new_prompt_data import positive_data,lateral_data,save_data
import pytest
logger=Logger().get_logger()
@pytest.mark.usefixtures("new_prompt_precess")
class TestNewPrompt:
    @pytest.mark.parametrize("data",lateral_data)
    def test_lateral_slice_prompt(self,data,new_prompt_precess):
        """验证在没有新建患者倒入侧位片的提示功能"""
        logger.info("{}_用例开始测试".format(data["title"]))
        act = new_prompt_precess.query_lateral_slice_prompt()
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e

    @pytest.mark.parametrize("data",positive_data)
    def test_positive_slice_prompt(self, data,new_prompt_precess):
        """验证在没有新建患者倒入正位片的提示功能"""
        logger.info("{}_用例开始测试".format(data["title"]))
        act = new_prompt_precess.query_positive_slice_prompt()
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e

    @pytest.mark.parametrize("data", save_data)
    def test_save_prompt(self, data,new_prompt_precess):
        """验证在没有新建患者时点击保存按钮的提示功能"""
        logger.info("{}_用例开始测试".format(data["title"]))
        act =new_prompt_precess.query_save_button_prompt()
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e