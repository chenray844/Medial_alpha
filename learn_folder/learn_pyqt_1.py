# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 12:53:41 2015

@author: Raymond
"""

import sys
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import QLabel, QVBoxLayout, QPushButton, QWidget, QApplication
from PyQt4.QtCore import QObject
app = QApplication(sys.argv)

widget = QWidget()
layout = QVBoxLayout()
label  = QLabel("HZJ Loves CRF!!!")
btn    = QPushButton("Exit")

layout.addWidget(label)
layout.addWidget(btn)
widget.setLayout(layout)

widget.show()

QObject.connect(btn, QtCore.SIGNAL("clicked()"), app, QtCore.SLOT("quit()"))

sys.exit(app.exec_())
