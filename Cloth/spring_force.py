__author__ = 'rachinaaahuja'

from OpenGL.GL import *
from particle import ParticleClass

class Spring():
    def __init__(self, p1, p2, len, ks, kd):
        """
        :type p1: ParticleClass
        :type p2: ParticleClass
        """
        self.p1=p1
        self.p2=p2
        self.len=len
        self.ks=ks
        self.kd=kd

    def draw(self):
        glBegin(GL_LINES)
        glColor3f(0,1,0)
        glVertex3f(self.p1.pos[0],self.p1.pos[1],self.p1.pos[2])
        glVertex3f(self.p2.pos[0],self.p2.pos[1],self.p2.pos[2])
        glEnd()

    #method to apply the force
