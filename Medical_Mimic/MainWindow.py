# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 13:45:10 2015

@author: Raymond
"""

#import sys
import vtk

from PyQt4 import QtCore, QtGui
from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

from Document import Document
# Main window
class MainWindow(QtGui.QMainWindow):
    # init
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        
        self.frame = QtGui.QFrame()
        
        self.layout = QtGui.QVBoxLayout()
        # vtk widget for 3d viewer
        self.vtk3DWidget = QVTKRenderWindowInteractor(self.frame)
        self.layout.addWidget(self.vtk3DWidget)
        
        self.ren = vtk.vtkRenderer()
        self.win = self.vtk3DWidget.GetRenderWindow()
        self.vtk3DWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtk3DWidget.GetRenderWindow().GetInteractor()
        
        # initialize document
        self.doc = Document(self.ren, self.win)
        # create actions
        self.createActions()
        # add menu
        self.createMenus()
        
        # set center widget        
        self.frame.setLayout(self.layout)
        self.setCentralWidget(self.frame)
        
        self.show()
        # initialize vtk interactor
        self.iren.Initialize()
        
        
        
    def createActions(self):
        self.addSphereAct = QtGui.QAction("Add Sphere", self)
        
        # connect
        self.connect(self.addSphereAct, QtCore.SIGNAL('triggered()'),self, QtCore.SLOT('slotAddSphere()'))
        
    def createMenus(self):
        fileMenu = self.menuBar().addMenu("File")
        fileMenu.addAction(self.addSphereAct)
        
    @QtCore.pyqtSlot()
    def slotAddSphere(self):
        self.doc.addSphereSource()
        self.win.Render()
        

