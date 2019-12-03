import subprocess
import uiautomation as auto
import time
import random
import os
import pyautogui
import sys
subprocess.Popen("C:\Program Files (x86)\E-Ceph\E-Ceph.exe")
window_control=auto.WindowControl(searchDepth=3,Name="启动对话框")
auto.ButtonControl(searchDepth=4,Name="新建").Click()
num=1
while num<=1:
    z_number = str(random.randint(1, 40))
    z_path_name =os.path.join("C:\data",z_number+".jpg")
    c_number = str(random.randint(1, 40))
    c_path_name =os.path.join("C:\data",c_number+".jpg")
    patient_number = auto.EditControl(searchDepth=4, AutomationId="1022").GetValuePattern().Value
    name="test_"+str(num)
    auto.EditControl(searchDepth=4, AutomationId="1021").GetValuePattern().SetValue(name)
    auto.PaneControl(searchDepth=4, AutomationId="1142").GetFirstChildControl().Click()
    auto.SendKey(0x25)
    auto.SendKey(0x0D)
    auto.EditControl(searchDepth=5, AutomationId="1001").GetValuePattern().SetValue("候志明")
    auto.ButtonControl(searchDepth=4, Name="确定").Click()
    auto.ButtonControl(searchDepth=4, Name=" 请选择X光片 ").Click()
    time.sleep(1.5)
    auto.EditControl(searchDepth=6, Name="文件名(N):").GetValuePattern().SetValue(c_path_name)
    auto.SendKey(0x0D)
    auto.Click(800,500)
    auto.Click(500,800)
    auto.ButtonControl(searchDepth=4, Name=" 请选择X光片 ").GetNextSiblingControl().Click()
    time.sleep(1.5)
    auto.EditControl(searchDepth=6, Name="文件名(N):").GetValuePattern().SetValue(z_path_name)
    auto.SendKey(0x0D)
    auto.SendKey(0x0D)
    auto.Click(600,400)
    auto.Click(300,600)
    auto.ButtonControl(searchDepth=4,Name=" 患者列表 ").Click()
    search_patient_name=auto.ButtonControl(searchDepth=4,Name="查找患者姓名")
    if not search_patient_name.Exists(maxSearchSeconds=60):
        print("查找失败")
    auto.TextControl(searchDepth=6,Name=patient_number).DoubleClick()
    auto.RadioButtonControl(searchDepth=6,Name="第二次测量").Click()
    auto.SendKey(0x0D)
    time.sleep(2)
    auto.ButtonControl(searchDepth=4, Name=" 请选择X光片 ").Click()
    time.sleep(1.5)
    auto.EditControl(searchDepth=6, Name="文件名(N):").GetValuePattern().SetValue(c_path_name)
    auto.SendKey(0x0D)
    auto.Click(800, 500)
    auto.Click(500, 800)
    auto.ButtonControl(searchDepth=4, Name=" 请选择X光片 ").GetNextSiblingControl().Click()
    time.sleep(1.5)
    auto.EditControl(searchDepth=6, Name="文件名(N):").GetValuePattern().SetValue(z_path_name)
    auto.SendKey(0x0D)
    auto.SendKey(0x0D)
    auto.Click(600,400)
    auto.Click(300,600)
    auto.ButtonControl(searchDepth=4,Name=" 保存当前文档").Click()
    time.sleep(4)
    auto.ButtonControl(searchDepth=4,Name="关闭").Click()
    # window_control= auto.WindowControl(searchDepth=3,Name="患者检索")
    # if not window_control.Exists():
    #     print("失败")
    auto.WindowControl(searchDepth=3,Name="患者检索").GetWindowPattern().Close()
    auto.ButtonControl(searchDepth=4,Name=" 创建新测量 ").Click()
    auto.SendKey(0x0D)
    time.sleep(3)
    num+=1