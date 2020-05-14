import sys
import os
root_path = os.getcwd()
sys.path.append(f'{root_path}\\qt')
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5 import QtCore, QtGui, QtWidgets
from UI.Ui_main_window import Ui_MainWindow
from UI.Ui_login import Ui_LoginWindow
from UI.Ui_register import Ui_RegisterWindow
from utils.VerificationCode import WidgetCode
from utils.FramelessDialog import *


ABSOLUTE_PATH = os.path.dirname(__file__)
BACKGROUND_COLOR = '#F8F8FF'
TITLE_COLOR = '#F0E68C'
GLOBAL_BUTTON = """
#closeButton{
    max-width: 36px;
    max-height: 36px;
    font-size: 12px;
    font-family: "Webdings";
    qproperty-text: "r";
    border-radius: 10px;
}
#closeButton:hover{
    color: white;
    background: red;
}
#minButton{
    max-width: 36px;
    max-height: 36px;
    font-family: "Webdings";
    font-size: 12px;
    qproperty-text: "0";
    border-radius: 10px;
}
#minButton:hover{
    background: #F8F8FF;
}
"""


# 主窗口
class Main_window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main_window, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        # self.setWindowOpacity(0.9) # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 去掉窗口标题栏

        # widget美化
        Qss =  'QWidget#widget{background-color: %s;border-top-left-radius:10px;border-top-right-radius:10px}' % TITLE_COLOR
        Qss += 'QWidget#widget_2{background-color: #F5F5F5;border-bottom-left-radius:10px}' 
        Qss += 'QWidget#widget_3{background-color: %s;border-bottom-right-radius:10px}' % BACKGROUND_COLOR
        Qss += GLOBAL_BUTTON
        self.setStyleSheet(Qss) # 边框部分qss重载

        # 添加logo
        self.logo.setPixmap(QPixmap(f'{ABSOLUTE_PATH}/img/logo.png').scaled(self.logo.width(), self.logo.height()))

        self.minButton.clicked.connect(self.showMinimized)
        self.closeButton.clicked.connect(self.close)

    # 鼠标左键按下变小手
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(QtCore.Qt.OpenHandCursor))

    # 鼠标左键放开变回箭头      
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = False
            self.setCursor(QCursor(QtCore.Qt.ArrowCursor))

    # 鼠标拖动窗口
    def mouseMoveEvent(self, event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position) #更改窗口位置
            event.accept()


# 登陆窗口
class Login_window(QMainWindow, Ui_LoginWindow):
    def __init__(self, parent=None):
        super(Login_window, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        # self.setWindowOpacity(0.9) # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 去掉窗口标题栏
        self.pushButton_4.setObjectName('closeButton')
        self.pushButton_3.setObjectName('minButton')
        # widget美化
        Qss =  'QWidget#widget{background-color: %s;border-bottom-left-radius:10px;border-bottom-right-radius:10px}' % BACKGROUND_COLOR
        Qss += 'QWidget#widget_2{background-color: %s;border-top-left-radius:10px;border-top-right-radius:10px}' % TITLE_COLOR
        # 注册按钮
        Qss += 'QPushButton#pushButton_2{background-color: %s;border-radius:5px;}' % TITLE_COLOR
        Qss += 'QPushButton#pushButton_2:hover{background-color: %s;border-radius:5px;}' % TITLE_COLOR
        Qss += 'QPushButton#pushButton_2:pressed{background-color: %s;border-radius:5px;}' % TITLE_COLOR
        # 登陆按钮
        Qss += 'QPushButton#pushButton{background-color: %s;border-radius:5px;}' % TITLE_COLOR
        Qss += 'QPushButton#pushButton:hover{background-color: %s;border-radius:5px;}' % TITLE_COLOR
        Qss += 'QPushButton#pushButton:pressed{background-color: %s;border-radius:5px;}' % TITLE_COLOR
        Qss += GLOBAL_BUTTON
        self.setStyleSheet(Qss) # 边框部分qss重载

        self.pushButton.clicked.connect(self.btn_login)
        self.pushButton_2.clicked.connect(self.btn_register)
        self.pushButton_3.clicked.connect(self.showMinimized)
        self.pushButton_4.clicked.connect(self.close)
        self.code = WidgetCode(self.widget_3, minimumHeight=35, minimumWidth=80)  # 添加验证码

    # 登陆按钮事件
    def btn_login(self):
        # 验证码验证
        code_check = self.code.check(self.lineEdit_3.text())
        if not code_check:
            self.main_window = Main_window()
            self.main_window.show()
            self.close()
        else:
            self.warn_dialog = Warn_Dialog()
            self.warn_dialog.label.setText('验证码错误！')
            self.warn_dialog.show()

    # 注册按钮事件
    def btn_register(self):
        self.register_window = Register_window()
        self.register_window.show()
        self.close()

    # 鼠标左键按下变小手
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(QtCore.Qt.OpenHandCursor))

    # 鼠标左键放开变回箭头      
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = False
            self.setCursor(QCursor(QtCore.Qt.ArrowCursor))

    # 鼠标拖动窗口
    def mouseMoveEvent(self, event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position) #更改窗口位置
            event.accept()



# 注册窗口
class Register_window(QMainWindow, Ui_RegisterWindow):
    def __init__(self, parent=None):
        super(Register_window, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        # self.setWindowOpacity(0.9) # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 去掉窗口标题栏
        self.pushButton_4.setObjectName('closeButton')
        self.pushButton_3.setObjectName('minButton')
        # widget美化
        Qss =  'QWidget#widget{background-color: %s;border-bottom-left-radius:10px;border-bottom-right-radius:10px}' % BACKGROUND_COLOR
        Qss += 'QWidget#widget_3{background-color: %s;border-top-left-radius:10px;border-top-right-radius:10px}' % TITLE_COLOR
        # 注册按钮
        Qss += 'QPushButton#pushButton{background-color: %s;border-radius:5px;}' % TITLE_COLOR
        Qss += 'QPushButton#pushButton:hover{background-color: %s;border-radius:5px;}' % TITLE_COLOR
        Qss += 'QPushButton#pushButton:pressed{background-color: %s;border-radius:5px;}' % TITLE_COLOR
        Qss += GLOBAL_BUTTON
        self.setStyleSheet(Qss) # 边框部分qss重载

        self.pushButton.clicked.connect(self.btn_register)
        self.pushButton_3.clicked.connect(self.showMinimized)
        self.pushButton_4.clicked.connect(self.close)

    # 登陆按钮事件
    def btn_register(self):
        self.login_window = Login_window()
        self.login_window.show()
        self.close()

    # 鼠标左键按下变小手
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos()-self.pos() #获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(QtCore.Qt.OpenHandCursor))

    # 鼠标左键放开变回箭头      
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = False
            self.setCursor(QCursor(QtCore.Qt.ArrowCursor))

    # 鼠标拖动窗口
    def mouseMoveEvent(self, event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position) #更改窗口位置
            event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login_window = Login_window()
    login_window.show()

    sys.exit(app.exec_())