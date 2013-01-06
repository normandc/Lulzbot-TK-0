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



# recompute, set view
App.activeDocument().recompute()
on=Gui.activeDocument().activeView().isAnimationEnabled()
Gui.activeDocument().activeView().setAnimationEnabled(False)
Gui.activeDocument().activeView().setCameraType("Perspective")
Gui.activeDocument().activeView().viewAxometric()
Gui.activeDocument().activeView().fitAll()
Gui.activeDocument().activeView().setAnimationEnabled(on)



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

# add threaded rods
Part.insert(os.path.join(path,"threaded_rod_0375-12_365mm.stp"),"TK0_Assembly")
Draft.move([FreeCAD.getDocument("TK0_Assembly").threaded_rod_0375_12_365mm],FreeCAD.Vector(-220,0,77),copy=True)
App.getDocument("TK0_Assembly").threaded_rod_0375_12_365mm.Placement=App.Placement(App.Vector(220,0,77),App.Rotation(0,0,0,1))

# add NamePlate
Part.insert(os.path.join(path,"NamePlate.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("NamePlate").ShapeColor = (1.0000,0.0000,0.0000)
App.getDocument("TK0_Assembly").NamePlate.Placement=App.Placement(App.Vector(0,-85.1,460),App.Rotation(0.707107,0,0,0.707107))

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
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("NamePlate"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("threaded_rod_0375_12_365mm"))
App.getDocument("TK0_Assembly").getObject("Z_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("threaded_rod_0375_12_365mm001"))


# recompute, set view
App.activeDocument().recompute()
on=Gui.activeDocument().activeView().isAnimationEnabled()
Gui.activeDocument().activeView().setAnimationEnabled(False)
Gui.activeDocument().activeView().setCameraType("Perspective")
Gui.activeDocument().activeView().viewAxometric()
Gui.activeDocument().activeView().fitAll()
Gui.activeDocument().activeView().setAnimationEnabled(on)


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

# add Bearing Holders
Part.insert(os.path.join(path,"Bearing_Holder.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("Bearing_Holder").ShapeColor = (1.0000,0.0000,0.0000)
App.getDocument("TK0_Assembly").Bearing_Holder.Placement=App.Placement(App.Vector(75,68.5,82),App.Rotation(0.707107,0,0,0.707107))
Draft.move([FreeCAD.getDocument("TK0_Assembly").Bearing_Holder],FreeCAD.Vector(-150,0,0),copy=True)
Draft.move([FreeCAD.getDocument("TK0_Assembly").Bearing_Holder],FreeCAD.Vector(0,0,0),copy=True)
App.getDocument("TK0_Assembly").Bearing_Holder002.Placement=App.Placement(App.Vector(75,-68.5,82),App.Rotation(-4.32964e-17,0.707107,0.707107,4.32964e-17))
Draft.move([FreeCAD.getDocument("TK0_Assembly").Bearing_Holder],FreeCAD.Vector(0,0,-77),copy=True)
App.getDocument("TK0_Assembly").Bearing_Holder003.Placement=App.Placement(App.Vector(-75,-68.5,82),App.Rotation(-4.32964e-17,0.707107,0.707107,4.32964e-17))

# add linear bearings
Part.insert(os.path.join(path,"LM10UU_LinearBearing.stp"),"TK0_Assembly")
App.getDocument("TK0_Assembly").LM10UU_LinearBearing.Placement = App.Placement(App.Vector(75,-52,70),App.Rotation(0,0,0.707107,0.707107))
Draft.move([FreeCAD.getDocument("TK0_Assembly").LM10UU_LinearBearing],FreeCAD.Vector(0,104,0),copy=True)
Draft.move([FreeCAD.getDocument("TK0_Assembly").LM10UU_LinearBearing],FreeCAD.Vector(-150,0,0),copy=True)
Draft.move([FreeCAD.getDocument("TK0_Assembly").LM10UU_LinearBearing],FreeCAD.Vector(-150,104,0),copy=True)

# add Y_Bed
Part.insert(os.path.join(path,"Y_Bed.stp"),"TK0_Assembly")
App.getDocument("TK0_Assembly").Y_Bed.Placement = App.Placement(App.Vector(0,0,85.17),App.Rotation(1,0,0,6.12303e-17))

# add Y_BeltMount
Part.insert(os.path.join(path,"Y_BeltMount.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("Y_BeltMount").ShapeColor = (1.0000,0.0000,0.0000)
App.getDocument("TK0_Assembly").Y_BeltMount.Placement = App.Placement(App.Vector(7,0,82),App.Rotation(0.707107,-0.707107,-0,0))

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
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Bearing_Holder"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Bearing_Holder001"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Bearing_Holder002"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Bearing_Holder003"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("LM10UU_LinearBearing"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("LM10UU_LinearBearing001"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("LM10UU_LinearBearing002"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("LM10UU_LinearBearing003"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Y_Bed"))
App.getDocument("TK0_Assembly").getObject("Y_Frame_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Y_BeltMount"))

# recompute, set view
App.activeDocument().recompute()
on=Gui.activeDocument().activeView().isAnimationEnabled()
Gui.activeDocument().activeView().setAnimationEnabled(False)
Gui.activeDocument().activeView().setCameraType("Perspective")
Gui.activeDocument().activeView().viewAxometric()
Gui.activeDocument().activeView().fitAll()
Gui.activeDocument().activeView().setAnimationEnabled(on)

##### CREATE X_ASSY #####

# add X_BearingForSpring
Part.insert(os.path.join(path,"X_BearingForSpring.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("X_BearingForSpring").ShapeColor = (1.0000,0.0000,0.0000)
xb = App.getDocument("TK0_Assembly").X_BearingForSpring
xb.Placement=App.Placement(App.Vector(238,57.50,228.50),App.Rotation(-0.707107,4.32964e-17,0.707107,4.32964e-17))

# add top Bearing_Holder
Draft.move([FreeCAD.getDocument("TK0_Assembly").Bearing_Holder],FreeCAD.Vector(0,0,0),copy=True)
App.getDocument("TK0_Assembly").Bearing_Holder004.Placement=App.Placement(App.Vector(238,0,250),App.Rotation(0,0,0.707107,0.707107))

# add bottom Bearing_Holder
Draft.move([FreeCAD.getDocument("TK0_Assembly").Bearing_Holder],FreeCAD.Vector(0,0,0),copy=True)
App.getDocument("TK0_Assembly").Bearing_Holder005.Placement=App.Placement(App.Vector(238,0,173),App.Rotation(0,0,0.707107,0.707107))

# add linear bearings
Draft.move([FreeCAD.getDocument("TK0_Assembly").LM10UU_LinearBearing],FreeCAD.Vector(0,0,0),copy=True)
App.getDocument("TK0_Assembly").LM10UU_LinearBearing004.Placement=App.Placement(App.Vector(250,0,266.5),App.Rotation(0,0.707107,0,0.707107))
Draft.move([FreeCAD.getDocument("TK0_Assembly").LM10UU_LinearBearing],FreeCAD.Vector(0,0,0),copy=True)
App.getDocument("TK0_Assembly").LM10UU_LinearBearing005.Placement=App.Placement(App.Vector(250,0,189.5),App.Rotation(0,0.707107,0,0.707107))

# add smooth rods
Draft.move([FreeCAD.getDocument("TK0_Assembly").smooth_rod_10x500mm],FreeCAD.Vector(0,0,0),copy=True)
App.getDocument("TK0_Assembly").smooth_rod_10x500mm004.Placement=App.Placement(App.Vector(-250,40,263.5),App.Rotation(0,0.707107,0,0.707107))
Draft.move([FreeCAD.getDocument("TK0_Assembly").smooth_rod_10x500mm],FreeCAD.Vector(0,0,0),copy=True)
App.getDocument("TK0_Assembly").smooth_rod_10x500mm005.Placement=App.Placement(App.Vector(-250,40,193.5),App.Rotation(0,0.707107,0,0.707107))

# copy bearing holders and linear bearings to the left side
Draft.rotate([FreeCAD.getDocument("TK0_Assembly").Bearing_Holder004,FreeCAD.getDocument("TK0_Assembly").Bearing_Holder005,FreeCAD.getDocument("TK0_Assembly").LM10UU_LinearBearing004,
FreeCAD.getDocument("TK0_Assembly").LM10UU_LinearBearing005],180.0,FreeCAD.Vector(0.0,0.0,0.0),axis=FreeCAD.Vector(0.0,0.0,1.0),copy=True)

# add X_MotorForSpring
Part.insert(os.path.join(path,"X_MotorForSpring.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("X_MotorForSpring").ShapeColor = (1.0000,0.0000,0.0000)
xm = App.getDocument("TK0_Assembly").X_MotorForSpring
xm.Placement=App.Placement(App.Vector(-238,57.50,228.50),App.Rotation(0.707107,0,0.707107,0))

# add bearing holders for X_Carriage
Draft.move([FreeCAD.getDocument("TK0_Assembly").Bearing_Holder],FreeCAD.Vector(0,0,0),copy=True)
bh1 = App.getDocument("TK0_Assembly").Bearing_Holder008
bh1.Placement=App.Placement(App.Vector(-50,28,263.50),App.Rotation(0.707107,4.32964e-17,0.707107,4.32964e-17))
Draft.move([FreeCAD.getDocument("TK0_Assembly").Bearing_Holder],FreeCAD.Vector(0,0,0),copy=True)
bh2 = App.getDocument("TK0_Assembly").Bearing_Holder009
bh2.Placement=App.Placement(App.Vector(-50,28,193.50),App.Rotation(0.707107,4.32964e-17,0.707107,4.32964e-17))
Draft.move([FreeCAD.getDocument("TK0_Assembly").Bearing_Holder],FreeCAD.Vector(0,0,0),copy=True)
bh3 = App.getDocument("TK0_Assembly").Bearing_Holder010
bh3.Placement=App.Placement(App.Vector(50,28,263.50),App.Rotation(-0.707107,-4.32964e-17,0.707107,4.32964e-17))
Draft.move([FreeCAD.getDocument("TK0_Assembly").Bearing_Holder],FreeCAD.Vector(0,0,0),copy=True)
bh4 = App.getDocument("TK0_Assembly").Bearing_Holder011
bh4.Placement=App.Placement(App.Vector(50,28,193.50),App.Rotation(-0.707107,-4.32964e-17,0.707107,4.32964e-17))

# add linear bearings
Draft.move([FreeCAD.getDocument("TK0_Assembly").LM10UU_LinearBearing],FreeCAD.Vector(0,0,-77),copy=True)
lb2 = App.getDocument("TK0_Assembly").LM10UU_LinearBearing008
lb2.Placement=App.Placement(App.Vector(33.5,40,263.5),App.Rotation(0,0,0,1))
Draft.move([FreeCAD.getDocument("TK0_Assembly").LM10UU_LinearBearing],FreeCAD.Vector(0,0,-77),copy=True)
App.getDocument("TK0_Assembly").LM10UU_LinearBearing009.Placement=App.Placement(App.Vector(33.5,40,193.5),App.Rotation(0,0,0,1))
Draft.move([FreeCAD.getDocument("TK0_Assembly").LM10UU_LinearBearing],FreeCAD.Vector(0,0,-77),copy=True)
App.getDocument("TK0_Assembly").LM10UU_LinearBearing010.Placement=App.Placement(App.Vector(-33.5,40,263.5),App.Rotation(0,0,0,1))
Draft.move([FreeCAD.getDocument("TK0_Assembly").LM10UU_LinearBearing],FreeCAD.Vector(0,0,-77),copy=True)
App.getDocument("TK0_Assembly").LM10UU_LinearBearing011.Placement=App.Placement(App.Vector(-33.5,40,193.5),App.Rotation(0,0,0,1))

# add NEMA-17 stepper motor
Draft.move([FreeCAD.getDocument("TK0_Assembly").NEMA_17_StepperMotor],FreeCAD.Vector(-220.132,0,4),copy=True)
App.getDocument("TK0_Assembly").NEMA_17_StepperMotor003.Placement=App.Placement(App.Vector(-216,104.5,228.5),App.Rotation(0.707107,0,0,0.707107))

# add X_Carriage
Part.insert(os.path.join(path,"X_Carriage.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("X_Carriage").ShapeColor = (1.0000,0.0000,0.0000)
xc = App.getDocument("TK0_Assembly").X_Carriage
xc.Placement=App.Placement(App.Vector(0,22,230.75),App.Rotation(-0.5,-0.5,-0.5,0.5))

# add X_SingleExtruderMount
Part.insert(os.path.join(path,"X_SingleExtruderMount.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("X_SingleExtruderMount").ShapeColor = (1.0000,0.0000,0.0000)
App.getDocument("TK0_Assembly").X_SingleExtruderMount.Placement=App.Placement(App.Vector(0,22,278.52),App.Rotation(4.32964e-17,-0.707107,0.707107,4.32964e-17))

# add X_Carriage_QuickGuide
Part.insert(os.path.join(path,"X_Carriage_QuickGuide.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("X_Carriage_QuickGuide").ShapeColor = (1.0000,0.0000,0.0000)
App.getDocument("TK0_Assembly").X_Carriage_QuickGuide.Placement=App.Placement(App.Vector(50,16,172.50),App.Rotation(4.32964e-17,0.707107,0.707107,4.32964e-17))

# add Z NutSprings
Part.insert(os.path.join(path,"Z_NutSpring.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("Z_NutSpring").ShapeColor = (1.0000,0.0000,0.0000)
App.getDocument("TK0_Assembly").Z_NutSpring.Placement=App.Placement(App.Vector(220,0,210.50),App.Rotation(0,0,0.707107,0.707107))
Draft.rotate([FreeCAD.getDocument("TK0_Assembly").Z_NutSpring],180.0,FreeCAD.Vector(0.0,0.0,0.0),axis=FreeCAD.Vector(0.0,0.0,1.0),copy=True)

# create X_Assy group to serve as sub-assembly and insert parts in the group
App.getDocument("TK0_Assembly").addObject("App::DocumentObjectGroup","X_Assy")
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("X_BearingForSpring"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Bearing_Holder004"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Bearing_Holder005"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("LM10UU_LinearBearing004"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("LM10UU_LinearBearing005"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("smooth_rod_10x500mm004"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("smooth_rod_10x500mm005"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Bearing_Holder006"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Bearing_Holder007"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("LM10UU_LinearBearing006"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("LM10UU_LinearBearing007"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("X_MotorForSpring"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("X_Carriage"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Bearing_Holder008"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Bearing_Holder009"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Bearing_Holder010"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Bearing_Holder011"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("LM10UU_LinearBearing008"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("LM10UU_LinearBearing009"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("LM10UU_LinearBearing010"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("LM10UU_LinearBearing011"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("NEMA_17_StepperMotor003"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("X_SingleExtruderMount"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("X_Carriage_QuickGuide"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Z_NutSpring"))
App.getDocument("TK0_Assembly").getObject("X_Assy").addObject(App.getDocument("TK0_Assembly").getObject("Z_NutSpring001"))

# recompute, set view
App.activeDocument().recompute()
on=Gui.activeDocument().activeView().isAnimationEnabled()
Gui.activeDocument().activeView().setAnimationEnabled(False)
Gui.activeDocument().activeView().setCameraType("Perspective")
Gui.activeDocument().activeView().viewAxometric()
Gui.activeDocument().activeView().fitAll()
Gui.activeDocument().activeView().setAnimationEnabled(on)

##### CREATE ELECTRONIC ENCLOSURE #####

# add ElectronicEnclosureBottom
Part.insert(os.path.join(path,"ElectronicEnclosureBottom.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("ElectronicEnclosureBottom").ShapeColor = (1.0000,0.0000,0.0000)
App.getDocument("TK0_Assembly").ElectronicEnclosureBottom.Placement=App.Placement(App.Vector(-270,0,100),App.Rotation(0.5,-0.5,-0.5,0.5))

# add ElectronicEnclosureStrainRelief
Part.insert(os.path.join(path,"ElectronicEnclosureStrainRelief.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("ElectronicEnclosureStrainRelief").ShapeColor = (1.0000,0.0000,0.0000)
App.getDocument("TK0_Assembly").ElectronicEnclosureStrainRelief.Placement=App.Placement(App.Vector(-280.5,0,49.7),App.Rotation(0.707107,-0.707107,4.32964e-17,4.32964e-17))

# add ElectronicEnclosureSDSlotSide
Part.insert(os.path.join(path,"ElectronicEnclosureSDSlotSide.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("ElectronicEnclosureSDSlotSide").ShapeColor = (1.0000,0.0000,0.0000)
App.getDocument("TK0_Assembly").ElectronicEnclosureSDSlotSide.Placement=App.Placement(App.Vector(-292.5,-85,100),App.Rotation(-0.5,0.5,0.5,0.5))

# add ElectronicEnclosurePowerCordSide
Part.insert(os.path.join(path,"ElectronicEnclosurePowerCordSide.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("ElectronicEnclosurePowerCordSide").ShapeColor = (1.0000,0.0000,0.0000)
App.getDocument("TK0_Assembly").ElectronicEnclosurePowerCordSide.Placement=App.Placement(App.Vector(-292.5,85,100),App.Rotation(0.5,-0.5,0.5,0.5))

# add ElectronicEnclosureStrainReliefSide
Part.insert(os.path.join(path,"ElectronicEnclosureStrainReliefSide.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("ElectronicEnclosureStrainReliefSide").ShapeColor = (1.0000,0.0000,0.0000)
App.getDocument("TK0_Assembly").ElectronicEnclosureStrainReliefSide.Placement=App.Placement(App.Vector(-292.5,0,27.5),App.Rotation(0,0,-0.707107,0.707107))

# add ElectronicEnclosureSwitchSide
Part.insert(os.path.join(path,"ElectronicEnclosureSwitchSide.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("ElectronicEnclosureSwitchSide").ShapeColor = (1.0000,0.0000,0.0000)
App.getDocument("TK0_Assembly").ElectronicEnclosureSwitchSide.Placement=App.Placement(App.Vector(-292.5,0,172.5),App.Rotation(-0.707107,-0.707107,4.32964e-17,-4.32964e-17))

# add ElectronicEnclosureTop
Part.insert(os.path.join(path,"ElectronicEnclosureTop.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("ElectronicEnclosureTop").ShapeColor = (1.0000,0.0000,0.0000)
App.getDocument("TK0_Assembly").ElectronicEnclosureTop.Placement=App.Placement(App.Vector(-310,0,100),App.Rotation(-0.5,0.5,0.5,-0.5))

# add rocker_switch
Part.insert(os.path.join(path,"rocker_switch.stp"),"TK0_Assembly")
FreeCADGui.getDocument("TK0_Assembly").getObject("rocker_switch").ShapeColor = (0.0000,0.0000,0.0000)
App.getDocument("TK0_Assembly").rocker_switch.Placement=App.Placement(App.Vector(-292.5,-56.5,172.5),App.Rotation(0,0,0,1))

# create ElectronicEnclosure group to serve as sub-assembly and insert parts in the group
App.getDocument("TK0_Assembly").addObject("App::DocumentObjectGroup","ElectronicEnclosure")
App.getDocument("TK0_Assembly").getObject("ElectronicEnclosure").addObject(App.getDocument("TK0_Assembly").getObject("ElectronicEnclosureBottom"))
App.getDocument("TK0_Assembly").getObject("ElectronicEnclosure").addObject(App.getDocument("TK0_Assembly").getObject("ElectronicEnclosureStrainRelief"))
App.getDocument("TK0_Assembly").getObject("ElectronicEnclosure").addObject(App.getDocument("TK0_Assembly").getObject("ElectronicEnclosureSDSlotSide"))
App.getDocument("TK0_Assembly").getObject("ElectronicEnclosure").addObject(App.getDocument("TK0_Assembly").getObject("ElectronicEnclosurePowerCordSide"))
App.getDocument("TK0_Assembly").getObject("ElectronicEnclosure").addObject(App.getDocument("TK0_Assembly").getObject("ElectronicEnclosureStrainReliefSide"))
App.getDocument("TK0_Assembly").getObject("ElectronicEnclosure").addObject(App.getDocument("TK0_Assembly").getObject("ElectronicEnclosureSwitchSide"))
App.getDocument("TK0_Assembly").getObject("ElectronicEnclosure").addObject(App.getDocument("TK0_Assembly").getObject("ElectronicEnclosureTop"))
App.getDocument("TK0_Assembly").getObject("ElectronicEnclosure").addObject(App.getDocument("TK0_Assembly").getObject("rocker_switch"))

##### FINISHING UP #####
# recompute, set view
App.activeDocument().recompute()
on=Gui.activeDocument().activeView().isAnimationEnabled()
Gui.activeDocument().activeView().setAnimationEnabled(False)
Gui.activeDocument().activeView().setCameraType("Perspective")
Gui.activeDocument().activeView().viewAxometric()
Gui.activeDocument().activeView().fitAll()
Gui.activeDocument().activeView().setAnimationEnabled(on)
