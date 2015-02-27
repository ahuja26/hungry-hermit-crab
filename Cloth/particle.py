__author__ = 'rachinaahuja'

from OpenGL.GL import *

class ParticleClass():
    def __init__(self):
        self.pos=[0,0,0]
        self.vel=[0,0,0]
        self.force=[0,0,0]
        self.acc=[0,0,0]

    def draw_particle(self, pos):
        self.pos=pos
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

#separate method to update and set positions