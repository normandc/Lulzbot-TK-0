import FreeCAD,Part
from FreeCAD import Base
import Draft
import os

# set STEP subdirectory for importing parts from
path=os.path.realpath(__file__)
path=os.path.dirname(path)
path=os.path.join(path,"STEP")

# create new document
App.newDocument("TK0_Assembly")

##### CREATE MAIN Z_FRAME #####

# add bottom front extrusion
Part.insert(os.path.join(path,"HFS5-2020x500mm.stp"),"TK0_Assembly")
hf1 = App.getDocument("TK0_Assembly").HFS5_2020x500mm
hf1.Placement.move(App.Vector(-250,-75.1,10))

# add upper front extrusion
Draft.move([FreeCAD.getDocument("TK0_Assembly").HFS5_2020x500mm],FreeCAD.Vector(0,0,480),copy=True)

# add front left upright extrusion
Draft.move([FreeCAD.getDocument("TK0_Assembly").HFS5_2020x500mm],FreeCAD.Vector(-260,0,0),copy=True)
hf2 = App.getDocument("TK0_Assembly").HFS5_2020x500mm002
hf2.Placement=App.Placement(App.Vector(-260,-75.1,0),App.Rotation(0,0.707107,0,-0.707107))

# add front right upright extrusion
Draft.move([FreeCAD.getDocument("TK0_Assembly").HFS5_2020x500mm002],FreeCAD.Vector(520,0,0),copy=True)

# add frame connectors
Part.insert(os.path.join(path,"FrameConnectors.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("FrameConnectors").ShapeColor = (1.0000,0.0000,0.0000)
Draft.move([FreeCAD.getDocument("TK0_Assembly").FrameConnectors],FreeCAD.Vector(0,0,0),copy=True)
Draft.move([FreeCAD.getDocument("TK0_Assembly").FrameConnectors],FreeCAD.Vector(0,0,0),copy=True)
Draft.move([FreeCAD.getDocument("TK0_Assembly").FrameConnectors],FreeCAD.Vector(0,0,0),copy=True)
fc1 = App.getDocument("TK0_Assembly").FrameConnectors
fc1.Placement=App.Placement(App.Vector(-270,-85.1,0),App.Rotation(0.707107,0,0,0.707107))
fc2 = App.getDocument("TK0_Assembly").FrameConnectors001
fc2.Placement=App.Placement(App.Vector(270,-89.1,0),App.Rotation(4.32964e-17,0.707107,0.707107,4.32964e-17))
fc3 = App.getDocument("TK0_Assembly").FrameConnectors002
fc3.Placement=App.Placement(App.Vector(-270,-89.1,500),App.Rotation(0.707107,0,0,-0.707107))
fc4 = App.getDocument("TK0_Assembly").FrameConnectors003
fc4.Placement=App.Placement(App.Vector(270,-85.1,500),App.Rotation(4.32964e-17,0.707107,-0.707107,-4.32964e-17))

# copy the front frame to the rear
Draft.rotate([FreeCAD.getDocument("TK0_Assembly").HFS5_2020x500mm,FreeCAD.getDocument("TK0_Assembly").HFS5_2020x500mm001,FreeCAD.getDocument("TK0_Assembly").HFS5_2020x500mm002,
FreeCAD.getDocument("TK0_Assembly").HFS5_2020x500mm003,FreeCAD.getDocument("TK0_Assembly").FrameConnectors,FreeCAD.getDocument("TK0_Assembly").FrameConnectors001,
FreeCAD.getDocument("TK0_Assembly").FrameConnectors002,FreeCAD.getDocument("TK0_Assembly").FrameConnectors003],180.0,FreeCAD.Vector(0.0,0.0,0.0),axis=FreeCAD.Vector(0.0,0.0,1.0),copy=True)

# add Z_top
Part.insert(os.path.join(path,"Z_top.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("Z_top").ShapeColor = (1.0000,0.0000,0.0000)
Draft.move([FreeCAD.getDocument("TK0_Assembly").Z_top],FreeCAD.Vector(0,0,0),copy=True)
App.getDocument("TK0_Assembly").Z_top.Placement=App.Placement(App.Vector(270,0,504),App.Rotation(0.707107,-0.707107,4.32964e-17,4.32964e-17))
App.getDocument("TK0_Assembly").Z_top001.Placement=App.Placement(App.Vector(-270,0,504),App.Rotation(-0.707107,-0.707107,4.32964e-17,4.32964e-17))

# add Z_MotorMount
Part.insert(os.path.join(path,"Z_MotorMount.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("Z_MotorMount").ShapeColor = (1.0000,0.0000,0.0000)
Draft.move([FreeCAD.getDocument("TK0_Assembly").Z_MotorMount],FreeCAD.Vector(0,0,0),copy=True)
App.getDocument("TK0_Assembly").Z_MotorMount.Placement=App.Placement(App.Vector(270,0,81),App.Rotation(0.5,-0.5,-0.5,0.5))
zm2 = App.getDocument("TK0_Assembly").Z_MotorMount001
zm2.Placement=App.Placement(App.Vector(-270,0,81),App.Rotation(0.5,0.5,0.5,0.5))

# add vertical smooth rods
Part.insert(os.path.join(path,"smooth_rod_10x500mm.stp"),"TK0_Assembly")
Draft.move([FreeCAD.getDocument("TK0_Assembly").smooth_rod_10x500mm],FreeCAD.Vector(-250,0,4),copy=True)
App.getDocument("TK0_Assembly").smooth_rod_10x500mm.Placement=App.Placement(App.Vector(250,0,4),App.Rotation(0,0,0,1))

# add NEMA-17 motors for Z-axis
Part.insert(os.path.join(path,"NEMA-17_StepperMotor.stp"),"TK0_Assembly")
Draft.move([FreeCAD.getDocument("TK0_Assembly").NEMA_17_StepperMotor],FreeCAD.Vector(-220.132,0,4),copy=True)
App.getDocument("TK0_Assembly").NEMA_17_StepperMotor.Placement=App.Placement(App.Vector(220.132,0,4),App.Rotation(0,0,0,1))

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
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Z_MotorMount"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Z_MotorMount001"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("smooth_rod_10x500mm"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("smooth_rod_10x500mm001"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("NEMA_17_StepperMotor"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("NEMA_17_StepperMotor001"))

##### CREATE Y_FRAME #####

# add right frontward extrusion
Draft.move([FreeCAD.getDocument("TK0_Assembly").HFS5_2020x500mm],FreeCAD.Vector(0,0,0),copy=True)
hf3 = App.getDocument("TK0_Assembly").HFS5_2020x500mm008
hf3.Placement=App.Placement(App.Vector(90,-250,30),App.Rotation(0,0,0.707107,0.707107))

# add left frontward extrusion
Draft.move([FreeCAD.getDocument("TK0_Assembly").HFS5_2020x500mm],FreeCAD.Vector(0,0,0),copy=True)
hf4 = App.getDocument("TK0_Assembly").HFS5_2020x500mm009
hf4.Placement=App.Placement(App.Vector(-90,-250,30),App.Rotation(0,0,0.707107,0.707107))

# add Y_Bearing
Part.insert(os.path.join(path,"Y_Bearing-4mmoffset.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("Y_Bearing_4mmoffset").ShapeColor = (1.0000,0.0000,0.0000)
yb = App.getDocument("TK0_Assembly").Y_Bearing_4mmoffset
yb.Placement=App.Placement(App.Vector(0,-254,0),App.Rotation(0,0.707107,0.707107,0))

# add Y_Motor
Part.insert(os.path.join(path,"Y_Motor.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("Y_Motor").ShapeColor = (1.0000,0.0000,0.0000)
ym = App.getDocument("TK0_Assembly").Y_Motor
ym.Placement=App.Placement(App.Vector(0,254,0),App.Rotation(0.707107,0,0,0.707107))

# add smooth rods
Draft.move([FreeCAD.getDocument("TK0_Assembly").smooth_rod_10x500mm],FreeCAD.Vector(0,0,0),copy=True)
App.getDocument("TK0_Assembly").smooth_rod_10x500mm002.Placement=App.Placement(App.Vector(75,-250,70),App.Rotation(-0.707107,0,0,0.707107))
Draft.move([FreeCAD.getDocument("TK0_Assembly").smooth_rod_10x500mm],FreeCAD.Vector(0,0,0),copy=True)
App.getDocument("TK0_Assembly").smooth_rod_10x500mm003.Placement=App.Placement(App.Vector(-75,-250,70),App.Rotation(-0.707107,0,0,0.707107))

# add NEMA-17 motor for Y-axis
Draft.move([FreeCAD.getDocument("TK0_Assembly").NEMA_17_StepperMotor],FreeCAD.Vector(0,0,0),copy=True)
App.getDocument("TK0_Assembly").NEMA_17_StepperMotor002.Placement=App.Placement(App.Vector(0,222.5,3.5),App.Rotation(0,0,0,1))

# add Y_FrameConnectors
Part.insert(os.path.join(path,"Y_FrameConnectorA.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("Y_FrameConnectorA").ShapeColor = (1.0000,0.0000,0.0000)
yfa = App.getDocument("TK0_Assembly").Y_FrameConnectorA
yfa.Placement=App.Placement(App.Vector(100,-75.1,20),App.Rotation(-0.707107,4.32964e-17,-0.707107,-4.32964e-17))
Draft.move([FreeCAD.getDocument("TK0_Assembly").Y_FrameConnectorA],FreeCAD.Vector(0,150.2,0),copy=True)

Part.insert(os.path.join(path,"Y_FrameConnectorB.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("Y_FrameConnectorB").ShapeColor = (1.0000,0.0000,0.0000)
yfb = App.getDocument("TK0_Assembly").Y_FrameConnectorB
yfb.Placement=App.Placement(App.Vector(90,-75.1,40),App.Rotation(0,0,0,1))
Draft.move([FreeCAD.getDocument("TK0_Assembly").Y_FrameConnectorB],FreeCAD.Vector(0,150.2,0),copy=True)

Draft.rotate([FreeCAD.getDocument("TK0_Assembly").Y_FrameConnectorA,FreeCAD.getDocument("TK0_Assembly").Y_FrameConnectorA001,FreeCAD.getDocument("TK0_Assembly").Y_FrameConnectorB,
FreeCAD.getDocument("TK0_Assembly").Y_FrameConnectorB001],180.0,FreeCAD.Vector(0.0,0.0,0.0),axis=FreeCAD.Vector(0.0,0.0,1.0),copy=True)

# create Y_Frame_Assy group to serve as sub-assembly and insert parts in the group
App.getDocument("TK0_Assembly").addObject("App::DocumentObjectGroup","Y_Frame_Assy")
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("HFS5_2020x500mm008"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("HFS5_2020x500mm009"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Y_Bearing_4mmoffset"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Y_Motor"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("smooth_rod_10x500mm002"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("smooth_rod_10x500mm003"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("NEMA_17_StepperMotor002"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Y_FrameConnectorA"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Y_FrameConnectorA001"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Y_FrameConnectorB"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Y_FrameConnectorB001"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Y_FrameConnectorA002"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Y_FrameConnectorA003"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Y_FrameConnectorB002"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Y_FrameConnectorB003"))

##### FINISHING UP #####
# recompute, set view
App.activeDocument().recompute()
on=Gui.activeDocument().activeView().isAnimationEnabled()
Gui.activeDocument().activeView().setAnimationEnabled(False)
Gui.activeDocument().activeView().setCameraType("Perspective")
Gui.activeDocument().activeView().viewAxometric()
Gui.activeDocument().activeView().fitAll()
Gui.activeDocument().activeView().setAnimationEnabled(on)
