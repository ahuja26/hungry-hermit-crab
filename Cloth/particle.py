__author__ = 'rachinaahuja'

from OpenGL.GL import *

import numpy as np

class ParticleClass():
    def __init__(self, pos, mass):
        self.pos=np.array(pos)
        #self.vel=[0,0,0]
        self.force=np.array([0,0,0])
        self.acc=np.array([0,0,0])
        assert isinstance(mass, float)
        self.mass=mass

    def draw(self):
        glColor3f(0.6,0,0)
        glBegin(GL_QUADS)
        #front
        glVertex3f(self.pos[0]-1,self.pos[1]-1,self.pos[2]+1)
        glVertex3f(self.pos[0]+1,self.pos[1]-1,self.pos[2]+1)
        glVertex3f(self.pos[0]+1,self.pos[1]+1,self.pos[2]+1)
        glVertex3f(self.pos[0]-1,self.pos[1]+1,self.pos[2]+1)
        #top
        glVertex3f(self.pos[0]-1,self.pos[1]+1,self.pos[2]-1)
        glVertex3f(self.pos[0]-1,self.pos[1]+1,self.pos[2]+1)
        glVertex3f(self.pos[0]+1,self.pos[1]+1,self.pos[2]+1)
        glVertex3f(self.pos[0]+1,self.pos[1]+1,self.pos[2]-1)
        #left
        glVertex3f(self.pos[0]-1,self.pos[1]+1,self.pos[2]-1)
        glVertex3f(self.pos[0]-1,self.pos[1]-1,self.pos[2]-1)
        glVertex3f(self.pos[0]-1,self.pos[1]-1,self.pos[2]+1)
        glVertex3f(self.pos[0]-1,self.pos[1]+1,self.pos[2]+1)
        #bottom
        glVertex3f(self.pos[0]-1,self.pos[1]-1,self.pos[2]-1)
        glVertex3f(self.pos[0]-1,self.pos[1]-1,self.pos[2]+1)
        glVertex3f(self.pos[0]+1,self.pos[1]-1,self.pos[2]+1)
        glVertex3f(self.pos[0]+1,self.pos[1]-1,self.pos[2]-1)
        #right
        glVertex3f(self.pos[0]+1,self.pos[1]-1,self.pos[2]-1)
        glVertex3f(self.pos[0]+1,self.pos[1]-1,self.pos[2]+1)
        glVertex3f(self.pos[0]+1,self.pos[1]+1,self.pos[2]+1)
        glVertex3f(self.pos[0]+1,self.pos[1]+1,self.pos[2]-1)
        #back
        glVertex3f(self.pos[0]-1,self.pos[1]-1,self.pos[2]-1)
        glVertex3f(self.pos[0]+1,self.pos[1]-1,self.pos[2]-1)
        glVertex3f(self.pos[0]+1,self.pos[1]+1,self.pos[2]-1)
        glVertex3f(self.pos[0]-1,self.pos[1]+1,self.pos[2]-1)
        glEnd()

    def clear_force(self):
        self.force=[0,0,0]

    def set_pos(self, pos):
        self.pos=pos

    def set_acc(self, acc):
        self.acc=acc

#separate method to update and set positions