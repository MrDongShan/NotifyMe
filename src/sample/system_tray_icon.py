# 在系统托盘(菜单栏)中展示图标

from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon

from system_banner_notification import show_notification
import sys


def init():
    app = QApplication(sys.argv)

    # 创建托盘图标
    tray_icon = QSystemTrayIcon()
    tray_icon.setIcon(QIcon('../../data/img/icon.png'))  # 设置图标，需要自行准备一个图标文件 icon.png
    tray_icon.setVisible(True)

    # 创建菜单
    menu = QMenu()
    # 添加菜单项到菜单
    action_show_dialog = menu.addAction("通知")
    action_show_main_windows = menu.addAction("展示主窗口")
    action_quit = menu.addAction("退出")

    # 点击退出时退出应用程序
    action_quit.triggered.connect(app.quit)
    action_show_dialog.triggered.connect(send_msg)
    action_show_main_windows.triggered.connect(open_main_windows)

    # 将菜单设置给托盘图标
    tray_icon.setContextMenu(menu)

    # 应用程序主循环
    sys.exit(app.exec())


# 打开主窗口
def open_main_windows():
    print("coming")


# 发送通知
def send_msg():
    show_notification("会议提醒", "你的下一次会议将在 10 分钟后开始。")


def main():
    app = QApplication(sys.argv)
    init()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
