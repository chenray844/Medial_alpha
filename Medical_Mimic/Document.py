# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 14:04:18 2015

@author: Raymond
"""
import vtk

class Document(object):
    def __init__(self, renderer, renderWindow):
        self.ren = renderer
        self.win = renderWindow
        
    def addSphereSource(self):
        values={'center':(0,0,0),'radius':1.0}
        # create sphere source
        source = vtk.vtkSphereSource()
        center = values.get('center',(0,0,0))
        radius = values.get('radius',1.0)
        source.SetCenter(center[0],center[1],center[2])
        source.SetRadius(radius)
        
        # create a mapper
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(source.GetOutputPort())
        
        # create an actor
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        
        self.ren.AddActor(actor)
        self.ren.ResetCamera()
        
        # render window
        self.win.Render()
        
        