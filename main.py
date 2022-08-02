import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import getopt
import requests
import base64
import json
import re
#import qdarkstyle
from QCandyUi import CandyWindow
import 日历


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())#黑色主题美化
    ui = 日历.Ui_MainWindow()
    ui.setupUi(MainWindow)
    #MainWindow = CandyWindow.createWindow(MainWindow, 'blue')
    MainWindow.show()
    #ui.pushButton.clicked.connect(search)
    sys.exit(app.exec_())
