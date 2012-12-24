import FreeCAD,Part
from FreeCAD import Base
import Draft
import os

path=os.path.realpath(__file__)
path=os.path.dirname(path)
path=os.path.join(path,"STEP")

# create new document
App.newDocument("TK0_Assembly")

# add bottom front extrusion
Part.insert(os.path.join(path,"HFS5-2020x500mm.stp"),"TK0_Assembly")
hf1 = App.getDocument("TK0_Assembly").HFS5_2020x500mm
hf1.Placement.move(App.Vector(-250,-75,10))

# add upper front extrusion
Draft.move([FreeCAD.ActiveDocument.HFS5_2020x500mm],FreeCAD.Vector(0,0,480),copy=True)

# add front left upright extrusion
Draft.move([FreeCAD.ActiveDocument.HFS5_2020x500mm],FreeCAD.Vector(-260,0,0),copy=True)
hf2 = App.getDocument("TK0_Assembly").HFS5_2020x500mm002
hf2.Placement=App.Placement(App.Vector(-260,-75,0),App.Rotation(0,0.707107,0,-0.707107))

# add front right upright extrusion
Draft.move([FreeCAD.ActiveDocument.HFS5_2020x500mm002],FreeCAD.Vector(520,0,0),copy=True)

# add frame connectors
Part.insert(os.path.join(path,"FrameConnectors.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("FrameConnectors").ShapeColor = (1.0000,0.0000,0.0000)
Draft.move([FreeCAD.ActiveDocument.FrameConnectors],FreeCAD.Vector(0,0,0),copy=True)
Draft.move([FreeCAD.ActiveDocument.FrameConnectors],FreeCAD.Vector(0,0,0),copy=True)
Draft.move([FreeCAD.ActiveDocument.FrameConnectors],FreeCAD.Vector(0,0,0),copy=True)
fc1 = App.getDocument("TK0_Assembly").FrameConnectors
fc1.Placement=App.Placement(App.Vector(-270,-85,0),App.Rotation(0.707107,0,0,0.707107))
fc2 = App.getDocument("TK0_Assembly").FrameConnectors001
fc2.Placement=App.Placement(App.Vector(270,-89,0),App.Rotation(4.32964e-17,0.707107,0.707107,4.32964e-17))
fc3 = App.getDocument("TK0_Assembly").FrameConnectors002
fc3.Placement=App.Placement(App.Vector(-270,-89,500),App.Rotation(0.707107,0,0,-0.707107))
fc4 = App.getDocument("TK0_Assembly").FrameConnectors003
fc4.Placement=App.Placement(App.Vector(270,-85,500),App.Rotation(4.32964e-17,0.707107,-0.707107,-4.32964e-17))

# copy the front frame to the rear
Draft.rotate([FreeCAD.ActiveDocument.HFS5_2020x500mm,FreeCAD.ActiveDocument.HFS5_2020x500mm001,FreeCAD.ActiveDocument.HFS5_2020x500mm002,
FreeCAD.ActiveDocument.HFS5_2020x500mm003,FreeCAD.ActiveDocument.FrameConnectors,FreeCAD.ActiveDocument.FrameConnectors001,FreeCAD.ActiveDocument.FrameConnectors002,
FreeCAD.ActiveDocument.FrameConnectors003],180.0,FreeCAD.Vector(0.0,0.0,0.0),axis=FreeCAD.Vector(0.0,0.0,1.0),copy=True)

# add Z_top
Part.insert(os.path.join(path,"Z_top.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("Z_top").ShapeColor = (1.0000,0.0000,0.0000)
Draft.move([FreeCAD.ActiveDocument.Z_top],FreeCAD.Vector(0,0,0),copy=True)
App.getDocument("TK0_Assembly").Z_top.Placement=App.Placement(App.Vector(270,0,504),App.Rotation(0.707107,-0.707107,4.32964e-17,4.32964e-17))
App.getDocument("TK0_Assembly").Z_top001.Placement=App.Placement(App.Vector(-270,0,504),App.Rotation(-0.707107,-0.707107,4.32964e-17,4.32964e-17))

# add Z_MotorMount
Part.insert(os.path.join(path,"Z_MotorMount3.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("Z_MotorMount3").ShapeColor = (1.0000,0.0000,0.0000)
Draft.move([FreeCAD.ActiveDocument.Z_MotorMount3],FreeCAD.Vector(0,0,0),copy=True)
App.getDocument("TK0_Assembly").Z_MotorMount3.Placement=App.Placement(App.Vector(270,0,80),App.Rotation(0.5,-0.5,-0.5,0.5))
zm2 = App.getDocument("TK0_Assembly").Z_MotorMount
zm2.Placement=App.Placement(App.Vector(-270,0,80),App.Rotation(0.5,0.5,0.5,0.5))

# create Z_Frame_Assy group to serve as sub-assembly and insert parts in the group
App.getDocument("TK0_Assembly").addObject("App::DocumentObjectGroup","Z_Frame_Assy")
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("HFS5_2020x500mm"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("HFS5_2020x500mm001"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("HFS5_2020x500mm002"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("HFS5_2020x500mm003"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("FrameConnectors"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("FrameConnectors001"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("FrameConnectors002"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("FrameConnectors003"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("HFS5_2020x500mm004"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("HFS5_2020x500mm005"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("HFS5_2020x500mm006"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("HFS5_2020x500mm007"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("FrameConnectors004"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("FrameConnectors005"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("FrameConnectors006"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("FrameConnectors007"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Z_top"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Z_top001"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Z_MotorMount3"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Z_MotorMount"))

# recompute, set view
App.activeDocument().recompute()
on=Gui.activeDocument().activeView().isAnimationEnabled()
Gui.activeDocument().activeView().setAnimationEnabled(False)
Gui.activeDocument().activeView().setCameraType("Perspective")
Gui.activeDocument().activeView().viewAxometric()
Gui.activeDocument().activeView().fitAll()
Gui.activeDocument().activeView().setAnimationEnabled(on)
