__author__ = 'rachinaahuja'

from PyQt4.QtGui import *
from PyQt4 import QtCore
from PyQt4.QtOpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *

from cloth import ClothSim

import sys


class GLWidget(QGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.setMinimumHeight(400)
        self.setMinimumWidth(600)
        self.t = 0.0
        self.dt = 1.0/10
        #arguments: width of cloth, number of particles per row, mass per particle, timestep
        self.myCloth = ClothSim(100, 10, 2.5, self.dt)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.draw_stuff)
        #needs to be same as timestep, this determines how often simulation is called
        self.timer.start(100)


    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # call with argument 0 for euler integration, 1 for semi implicit euler and 2 for verlet
        self.myCloth.simulation_step(1)
        self.myCloth.draw()
        self.t += self.dt

    def draw_stuff(self):
        #call with argument 0 for euler integration, 1 for semi implicit euler and 2 for verlet
        self.myCloth.simulation_step(1)
        self.myCloth.draw()
        self.updateGL()

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluPerspective(60.0, float(w) / float(h), 0.1, 1000.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        gluLookAt(60, -200, 0, -150, 0, 0, 0, 1, 0)


    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GLWidget()
    window.setWindowTitle("Mass Spring Cloth")
    window.show()
    app.exec_()