# 在系统托盘(菜单栏)中展示图标,点击托盘图标，弹出窗口

import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QWidget

from main_windows import MainWindows


class SystemTray(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建托盘图标
        self.tray_icon = QSystemTrayIcon()
        self.tray_icon.setIcon(QIcon('../../data/img/icon.png'))  # 设置图标，需要自行准备一个图标文件 icon.png
        self.tray_icon.setVisible(True)

        # 创建窗口
        self.window = MainWindows()

        # 点击托盘图标时展示窗口
        def tray_icon_clicked(reason):
            if reason == QSystemTrayIcon.ActivationReason.Trigger:
                self.window.show_windows()

        # todo 如何优化掉这个方法，怎么做到触发的时候可以传参
        self.tray_icon.activated.connect(tray_icon_clicked)


def main():
    app = QApplication(sys.argv)
    st = SystemTray()
    # 应用程序主循环
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
