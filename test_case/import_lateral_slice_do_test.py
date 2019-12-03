from test_page.import_lateral_slice_do_page import ImportLateralSliceDoPage
from test_data.import_lateral_slice_do_data import three_point_angle_data,two_point_one_data,two_point_two_data,\
four_point_move_data,two_point_one_positive_data,two_point_two_positive_data,three_point_angle_positive_data,four_point_move_positive_data
import pytest
from common.get_logger import Logger
logger=Logger().get_logger()
@pytest.mark.usefixtures("import_lateral_slice_do_precess")
class TestImportLateralSliceDo:
    @pytest.mark.parametrize("data",two_point_one_data)
    def test_two_point_one(self,data,import_lateral_slice_do_precess):
        # """验证在没有新建患者倒入侧位片的提示功能"""
        logger.info("{}_用例开始测试".format(data["title"]))
        act = import_lateral_slice_do_precess.query_two_point_one()
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e

    @pytest.mark.parametrize("data", two_point_two_data)
    def test_two_point_two(self,data,import_lateral_slice_do_precess):
        # """验证在没有新建患者倒入侧位片的提示功能"""
        logger.info("{}_用例开始测试".format(data["title"]))
        act = import_lateral_slice_do_precess.query_two_point_two()
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e

    @pytest.mark.parametrize("data", three_point_angle_data)
    def test_three_point_angle(self,data,import_lateral_slice_do_precess):
        # """验证在没有新建患者倒入侧位片的提示功能"""
        logger.info("{}_用例开始测试".format(data["title"]))
        act = import_lateral_slice_do_precess.query_three_point_angle()
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e

    @pytest.mark.parametrize("data",four_point_move_data)
    def test_four_move_point(self,data,import_lateral_slice_do_precess):
        #"""验证在没有新建患者倒入侧位片的提示功能"""
        logger.info("{}_用例开始测试".format(data["title"]))
        act = import_lateral_slice_do_precess.query_four_point_move()
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e

    @pytest.mark.parametrize("data",two_point_one_positive_data)
    def test_two_point_one_positive(self, data, import_lateral_slice_do_precess):
        # """验证在没有新建患者倒入侧位片的提示功能"""
        logger.info("{}_用例开始测试".format(data["title"]))
        act = import_lateral_slice_do_precess.query_two_point_one_positive()
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e

    @pytest.mark.parametrize("data",two_point_two_positive_data)
    def test_two_point_two_positive(self, data, import_lateral_slice_do_precess):
        # """验证在没有新建患者倒入侧位片的提示功能"""
        logger.info("{}_用例开始测试".format(data["title"]))
        act = import_lateral_slice_do_precess.query_two_point_two_positive()
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e

    @pytest.mark.parametrize("data",three_point_angle_positive_data)
    def test_three_point_angle_positive(self, data, import_lateral_slice_do_precess):
        # """验证在没有新建患者倒入侧位片的提示功能"""
        logger.info("{}_用例开始测试".format(data["title"]))
        act = import_lateral_slice_do_precess.query_three_point_angle_positive()
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e

    @pytest.mark.parametrize("data",four_point_move_positive_data)
    def test_four_move_point_positive(self, data, import_lateral_slice_do_precess):
        # """验证在没有新建患者倒入侧位片的提示功能"""
        logger.info("{}_用例开始测试".format(data["title"]))
        act = import_lateral_slice_do_precess.query_four_point_move_positive()
        try:
            assert data["exp"] == act
            logger.info("{}_用例测试结束并且通过".format(data["title"]))
        except AssertionError as e:
            logger.exception("断言失败")
            raise e