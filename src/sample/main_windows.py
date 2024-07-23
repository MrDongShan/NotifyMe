# 主窗口
# 点击按钮后，触发系统横幅通知
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QWidget, QPushButton)

from system_banner_notification import show_notification


class MainWindows(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # 创建一个按钮
        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.send_msg)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowIcon(QIcon('../../data/img/icon.png'))
        self.setWindowTitle('窗口')

    def send_msg(self):
        show_notification("会议提醒", "你的下一次会议将在 10 分钟后开始。")

    def show_windows(self):
        # 置顶
        self.raise_()
        # 显示
        self.show()

def main():
    # app = QApplication(sys.argv)
    ex = MainWindows()
    # ex.show()
    # ex.top_windows()
    # sys.exit(app.exec())


if __name__ == '__main__':
    main()
