# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 13:57:30 2015

@author: Raymond
"""

import sys
from PyQt4 import QtGui
from MainWindow import MainWindow

# run this app
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())