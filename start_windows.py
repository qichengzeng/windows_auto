import subprocess
import uiautomation as auto
import time
subprocess.Popen("C:\Program Files (x86)\E-Ceph\E-Ceph.exe")
window_control=auto.WindowControl(searchDepth=3,Name="启动对话框")
if window_control.Exists(maxSearchSeconds=15):
    pass
auto.ButtonControl(searchDepth=4,Name="新建").Click()
num=1
while num<=50:
    auto.EditControl(searchDepth=4, AutomationId="1021").SendKeys("曾奇成")
    auto.PaneControl(searchDepth=4, AutomationId="1142").GetFirstChildControl().Click()
    auto.SendKey(0x25)
    auto.SendKey(0x0D)
    auto.EditControl(searchDepth=5, AutomationId="1001").SendKeys("候志明")
    auto.ButtonControl(searchDepth=4, Name="确定").Click()
    auto.ButtonControl(searchDepth=4, Name=" 请选择X光片 ").Click()
    # auto.SetClipboardText("E:\侧位片.jpg")
    # path_name=auto.GetClipboardText()
    # auto.EditControl(searchDepth=6,Name="文件名(N):").Click()
    auto.EditControl(searchDepth=6, Name="文件名(N):").SendKeys("E:\侧位片.jpg")
    # auto.ButtonControl(searchDepth=4, Name="打开(O)").Click()
    auto.SendKey(0x0D)
    auto.ButtonControl(searchDepth=4, Name=" 请选择X光片 ").GetNextSiblingControl().Click()
    # auto.SetClipboardText("E:\正位片.jpg")
    # path_name=auto.GetClipboardText()
    # auto.EditControl(searchDepth=6,Name="文件名(N):").Click()
    auto.EditControl(searchDepth=6, Name="文件名(N):").SendKeys("E:\正位片.jpg")
    # auto.ButtonControl(searchDepth=4, Name="打开(O)").Click()
    auto.SendKey(0x0D)
    auto.ButtonControl(searchDepth=4, Name=" 创建新测量 ").Click()
    auto.ButtonControl(searchDepth=3, Name="是(Y)").Click()
    time.sleep(3)
    num+=1
