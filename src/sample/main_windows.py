# 主窗口
# 点击按钮后，触发系统横幅通知

from PyQt6.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QInputDialog, QApplication)
import sys
from system_banner_notification import show_notification

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建一个按钮
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.send_msg)
        self.setGeometry(300, 300, 250, 150)
        self.show()

    def send_msg(self):
        show_notification("会议提醒", "你的下一次会议将在 10 分钟后开始。")


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
