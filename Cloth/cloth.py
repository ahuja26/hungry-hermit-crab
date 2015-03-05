__author__ = 'rachinaaahuja'

import numpy as np

from particle import ParticleClass
from spring_force import Spring


class ClothSim():
    def __init__(self, w, num, m, dt):
        # set up cloth
        self.w = w
        # number of particles in a row
        #note: mass is per particle
        self.num = num
        self.particles = []
        self.forces = []
        self.createLayout(w, num, m)
        self.dt = dt

    def createLayout(self, w, num, m):
        # draw grid of particles
        for x in range(-w / 2, w / 2, num):
            pTemp = []
            for z in range(-w / 2, w / 2, num):
                pTemp.append(ParticleClass([x, 0, z], m))
            self.particles.append(pTemp)

        # draw bottom right and left
        for i in range(0, num):
            for j in range(0, num):
                #structural springs
                if j < num - 1:
                    self.forces.append(Spring(self.particles[i][j], self.particles[i][j + 1], 10.0, 4.0))
                if i < num - 1:
                    self.forces.append(Spring(self.particles[i][j], self.particles[i + 1][j], 10.0, 4.0))
                #shear springs
                if i < num - 1 and j < num - 1:
                    self.forces.append(Spring(self.particles[i][j], self.particles[i + 1][j + 1], 10.0, 2.0))
                if i < num - 1 and j > 0:
                    self.forces.append(Spring(self.particles[i][j], self.particles[i + 1][j - 1], 10.0, 2.0))
                #bend springs
                if (i ==0 or i==(num-1)) and j < num - 2:
                    self.forces.append(Spring(self.particles[i][j],self.particles[i][j+2], 4.0, 2.0))
                if i<num-2 and (j==0 or j==(num-1)):
                    self.forces.append(Spring(self.particles[i][j],self.particles[i+2][j], 4.0, 2.0))

    def draw(self):
        for row in self.particles:
            for particle in row:
                assert isinstance(particle, object)
                particle.draw()
        for spr in self.forces:
            spr.draw()

    def simulation_step(self):
        # clear forces
        for row in self.particles:
            for particle in row:
                assert isinstance(particle, object)
                particle.clear_force()
        #apply forces
        #gravity
        for row in self.particles:
            for particle in row:
                assert isinstance(particle, object)
                particle.force += particle.mass * np.array([0, -9.8, 0])

        #spring forces
        for spr in self.forces:
            x=spr.p1.pos - spr.p2.pos
            temp1=(spr.p1.vel-spr.p2.vel)
            temp2=np.multiply(temp1,x)

            f1 = -((spr.ks * (np.linalg.norm(x) - spr.rest_len) +spr.kd*(temp2/np.linalg.norm(x))))
            force=np.multiply(f1,x)/np.linalg.norm(x)
            spr.p1.force += force
            spr.p2.force -= force
        #keep two end points static
        self.particles[0][0].force += -(self.particles[0][0].force)
        self.particles[0][self.num - 1].force += -(self.particles[0][self.num - 1].force)
        #integration step
        self.verlets()

    def verlets(self):

        for row in self.particles:
            for particle in row:
                assert isinstance(particle, object)
                particle.acc=particle.force / particle.mass
                xprev = particle.prevpos
                xcurr = particle.pos
                xnext = (2 * xcurr) - xprev + particle.acc * (self.dt * self.dt)
                particle.prevpos=particle.pos
                particle.pos=xnext
                #particle.vel=((np.linalg.norm(xnext)-np.linalg.norm(xcurr))*xnext/np.linalg.norm(xnext))/self.dt
                particle.vel=(xnext-xcurr)/self.dt

    def euler(self):
        for row in self.particles:
            for particle in row:
                assert isinstance(particle, object)
                particle.acc=particle.force / particle.mass
                vnext=particle.vel+particle.acc*self.dt
                xnext=particle.pos+vnext*self.dt
                particle.vel=vnext
                particle.pos=xnext




