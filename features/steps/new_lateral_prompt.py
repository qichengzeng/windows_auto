from behave import *
from test_locator.start_dialog_locator import StartDialogLocator
from test_locator.e_ceph_locator import ECephLocator
from time import sleep
@given(' 已经关闭启动对话框并准备点击“从侧位片导入”按钮')
def step_impl(context):
    context.precess.close(StartDialogLocator.dialog, seconds=15, interval_seconds=1)
@when('点击“从侧位片导入”按钮')
def step_impl(context):
    context.precess.click(ECephLocator.lateral_slice_introduction_loc)
    text_control = context.precess.get_text_control(ECephLocator.new_prompt_loc)
    context.act = context.precess.get_control_name(text_control)
    context.precess.close_exe()
@then('判断点击“从侧位片导入”按钮后是否出现“请先新建测量”提示')
def step_impl(context):
        assert  context.act=="请先新建测量"
