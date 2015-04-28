__author__ = 'rachinaahuja'

import pysideuic
import traceback
import xml.etree.ElementTree as xml
import maya.cmds as cmds
import maya.OpenMayaUI as omui

from PySide import QtCore
from PySide import QtGui
from cStringIO import StringIO
from shiboken import wrapInstance

from sketch_pose import SketchPose

#LOAD UI FILE WITH CORRECT PATH
ui_filename="C:\sketchTest.ui"
'''Get maya main window widget as python object
http://zurbrigg.com/maya-python/item/signals-and-slots-in-pyside
'''

def mayaMainWindow():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtGui.QWidget)

'''Nathan Horne's code for loading .ui file in PySide
http://nathanhorne.com/?p=451
'''
def loadUiType(uiFile):
    parsed=xml.parse(uiFile)
    widget_class=parsed.find('widget').get('class')
    form_class=parsed.find('class').text

    with open(uiFile,'r') as f:
        o=StringIO()
        frame={}

        pysideuic.compileUi(f, o, indent=0)
        pyc = compile(o.getvalue(),'<string>','exec')
        exec pyc in frame
        form_class = frame['Ui_%s'%form_class]
        base_class=eval('QtGui.%s'%widget_class)
    return form_class, base_class

form_class, base_class=loadUiType(ui_filename)

#MAIN UI CODE GOES HERE
class sketchBasedUI(base_class,form_class):
    def __init__(self, parent=mayaMainWindow()):
        super(sketchBasedUI, self).__init__(parent)
        self.setupUi(self)
        self.setObjectName('sketchBasedUI')
        self.dataObj=SketchPose()
        self.create()
        self.show()

    def connectInterface(self):
        ##ui signals to slots connection here
        self.btn_select_chain.clicked.connect(self.dataObj.getSelectedJoints)
        self.btn_draw_curve.clicked.connect(self.dataObj.drawCurve)
        self.btn_select_curve.clicked.connect(self.dataObj.getDrawnCurve)
        self.btn_go.clicked.connect(self.dataObj.computePose)
        self.slider_res.valueChanged.connect(self.dataObj.setRes)
        self.btn_key.clicked.connect(self.dataObj.setKey)
        self.btn_select_hi.clicked.connect(self.dataObj.selectHierarchy)

    def create(self):
        self.setWindowTitle('Sketch Based Posing')
        #create object for data
        self.connectInterface()

if __name__ == "__main__":

    try:
        sketchBasedUI.deleteLater()
    except:
        pass

    sbui = sketchBasedUI()

    try:
        sbui.create()
        sbui.show()
    except:
        sbui.deleteLater()
        traceback.print_exc()
