#!/usr/bin/env python
# encoding: utf-8
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from Ui_main import Ui_Form


class MainWindow(QtWidgets.QWidget, Ui_Form):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowStaysOnTopHint)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
