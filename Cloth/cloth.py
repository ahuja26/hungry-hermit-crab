__author__ = 'rachinaaahuja'

import numpy as np

from particle import ParticleClass
from spring_force import Spring


class ClothSim():
    def __init__(self, w, num, m, dt):
        # set up cloth
        self.w = w
        #number of particles in a row
        self.num = num
        self.particles = []
        self.forces = []
        self.createLayout(w, num, m)
        self.dt=dt

    def createLayout(self, w, num, m):
        # draw grid of particles
        for x in range(-w / 2, w / 2, num):
            pTemp = []
            for z in range(-w / 2, w / 2, num):
                pTemp.append(ParticleClass([x, 0, z], m))
            self.particles.append(pTemp)

        #draw bottom right and left
        for i in range(0, num):
            for j in range(0, num):
                if j < num - 1:
                    self.forces.append(Spring(self.particles[i][j], self.particles[i][j + 1], 1.0, 1.0))
                if i < num - 1 and j < num - 1:
                    self.forces.append(Spring(self.particles[i][j], self.particles[i + 1][j + 1], 1.0, 1.0))
                if i < num - 1:
                    self.forces.append(Spring(self.particles[i][j], self.particles[i + 1][j], 1.0, 1.0))
                if i < num - 1 and j > 0:
                    self.forces.append(Spring(self.particles[i][j], self.particles[i + 1][j - 1], 1.0, 1.0))

    def draw(self):
        for row in self.particles:
            for particle in row:
                assert isinstance(particle, object)
                particle.draw()
        for spr in self.forces:
            spr.draw()

    def simulation_step(self):
        #clear forces
        for row in self.particles:
            for particle in row:
                assert isinstance(particle, object)
                particle.clear_force()
        #apply forces
        #gravity
        for row in self.particles:
            for particle in row:
                assert isinstance(particle, object)
                particle.force+=particle.mass*np.array([0,9.8,0])
        #spring forces
        for spr in self.forces:
            f1=-(spr.ks(np.linalg.norm(spr.p1.pos-spr.p2.pos)-spr.len))*((spr.p1.pos-spr.p2.pos)/np.linalg.norm((spr.p1.pos-spr.p2.pos)))
            f2=-f1
            spr.p1.force+=f1
            spr.p2.force+=f2
        #integration step
        self.verlets()

    def verlets(self):
        for row in self.particles:
            for particle in row:
                assert isinstance(particle, object)
                particle.acc=particle.force/particle.mass
                xprev=particle.prevpos
                xcurr=particle.pos
                xnext=(2*xcurr)-xprev+particle.acc*(dt*dt)
                particle.pos=xnext
