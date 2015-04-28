__author__ = 'rachinaahuja'

import maya.cmds as cmds
import maya.api.OpenMaya as om
import math

class SketchPose():
    def __init__(self):
        #selected joint chain
        self.joints=[]
        #current drawn curve
        self.curve='curve1'
        self.res=1
        self.spans=len(self.joints)-1*self.res

    def getSelectedJoints(self):
        self.joints=cmds.ls(sl=True,dag=True,ap=True,type="joint")
        print("got selected joints")
        print(self.joints)
        #set spans acc


    def getDrawnCurve(self):
        #have user select it for now
        selected_curve=cmds.listRelatives(cmds.ls(sl=True, dag=True, type='nurbsCurve'), parent=True)
        self.curve=selected_curve[0]
        print(self.curve)

    def drawCurve(self):
        cmds.setToolTo(cmds.curveSketchCtx( degree=3 ))

    def clearData(self):
        cmds.delete(self.curve)
        self.joints=[]

    def setRes(self, res):
        self.res=res
        print(self.res)

    def setKey(self):
        cmds.setKeyframe(at='rotateZ')

    def selectHierarchy(self):
        cmds.select(hi=True)

    def computePose(self):
        self.spans=(len(self.joints)-1)*self.res
        print(self.spans)
        cmds.rebuildCurve(self.curve, rt=0, s=self.spans)
        #array of points on curve
        #eps=['curve1.ep[0]','curve1.ep[1]','curve1.ep[2]','curve1.ep[3]','curve1.ep[4]','curve1.ep[5]','curve1.ep[6]']
        eps=[]
        for j in range(self.spans):
            prop=self.curve+'.ep['+str(j)+']'
            print(prop)
            eps.append(prop)

        for i in range(len(self.joints)-2):
            #end pts of curr bone
            root_pos=om.MVector(cmds.xform(self.joints[i], ws=1, t=1, q=1))
            end_pos=om.MVector(cmds.xform(self.joints[i+1], ws=1, t=1, q=1))

            joint_vec=end_pos-root_pos
            #end pts of corresponding curve span
            span_start_pos=om.MVector(cmds.xform(eps[i*self.res], ws=1, t=1, q=1))
            print(span_start_pos)
            span_end_pos=om.MVector(cmds.xform(eps[(i*self.res)+1], ws=1, t=1, q=1))

            span_vec=span_end_pos-span_start_pos

            #get cos angle using normalized dot product
            cos_angle=joint_vec.normal()*span_vec.normal()
            if(cos_angle<1):
                rot_attr=self.joints[i]+'.rotateZ'
                curr_rot=cmds.getAttr(rot_attr)
                turn_angle=math.acos(cos_angle)
                turn_deg=turn_angle*180/math.pi

                cross=joint_vec.normal()^span_vec.normal()
                #if z is positive rotate clockwise
                if(cross.z>0):
                    cmds.setAttr(rot_attr, curr_rot+turn_deg)
                elif(cross.z<0):
                    cmds.setAttr(rot_attr, curr_rot-turn_deg)
