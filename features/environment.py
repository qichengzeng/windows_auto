from behave import *
from common.base_method import  BaseMethod
def before_scenario(context, scenario):
    context.precess=BaseMethod("C:\Program Files (x86)\E-Ceph\E-Ceph.exe")
    print("pass")
# def after_scenario(context, scenario):
#     context.precess.close_exe()
#     print("pass")