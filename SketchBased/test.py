import maya.cmds as cmds
import maya.api.OpenMaya as om
import math

#OPTIMIZE UNNECESSARY VARIABLES
#drawn curve plus spans = num of joints, should be input
inp_spans=6
#this controls fidelity to shape of curve
res=10
spans=inp_spans*res

cmds.rebuildCurve('curve1', rt=0, s=spans)
#array of points on curve
#eps=['curve1.ep[0]','curve1.ep[1]','curve1.ep[2]','curve1.ep[3]','curve1.ep[4]','curve1.ep[5]','curve1.ep[6]']
eps=[]
for j in range(spans):
    prop='curve1.ep['+str(j)+']'
    eps.append(prop)

#array of joints

joints=['joint1','joint2','joint3','joint5','joint6','joint7']

for i in range(len(joints)-1):
    #end pts of curr bone
    root_pos=om.MVector(cmds.xform(joints[i], ws=1, t=1, q=1))
    end_pos=om.MVector(cmds.xform(joints[i+1], ws=1, t=1, q=1))
    
    joint_vec=end_pos-root_pos
    #end pts of corresponding curve span
    span_start_pos=om.MVector(cmds.xform(eps[i*res], ws=1, t=1, q=1))
    span_end_pos=om.MVector(cmds.xform(eps[(i*res)+1], ws=1, t=1, q=1))
    
    span_vec=span_end_pos-span_start_pos
    
    #get cos angle using normalized dot product
    cos_angle=joint_vec.normal()*span_vec.normal()
    if(cos_angle<1):
        rot_attr=joints[i]+'.rotateZ'
        curr_rot=cmds.getAttr(rot_attr)
        turn_angle=math.acos(cos_angle)
        turn_deg=turn_angle*180/math.pi
        
        cross=joint_vec.normal()^span_vec.normal()
        #if z is positive rotate clockwise
        if(cross.z>0):
            cmds.setAttr(rot_attr, curr_rot+turn_deg)
        elif(cross.z<0):
            cmds.setAttr(rot_attr, curr_rot-turn_deg)