__author__ = 'rachinaaahuja'

import numpy as np

from particle import ParticleClass
from spring_force import Spring


class ClothSim():
    def __init__(self, w, num, m):
        # set up cloth
        self.w = w
        #number of particles in a row
        self.num = num
        self.particles = []
        self.forces = []
        self.createLayout(w, num, m)

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
            f1=-(spr.ks(spr.p1.pos-spr.p2.pos-spr.len))
        #integration step