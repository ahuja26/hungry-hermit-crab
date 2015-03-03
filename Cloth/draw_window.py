__author__ = 'rachinaahuja'

from PyQt4.QtGui import *
from PyQt4 import QtCore
from PyQt4.QtOpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *

from cloth import ClothSim


class TestWidget(QGLWidget):
    def __init__(self, parent=None):
        super(TestWidget, self).__init__(parent)
        self.t = 0.0
        self.dt = 1.0 / 50
        self.myCloth = ClothSim(100, 10, 1.0, self.dt)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.draw_stuff)
        self.timer.start(100)


    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glRectf(-5, -5, 5, 5)
        self.myCloth.simulation_step()
        self.myCloth.draw()
        self.t += self.dt

    def draw_stuff(self):
        self.myCloth.simulation_step()
        self.myCloth.draw()
        self.updateGL()

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        # glViewport(0,0,w,h)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluPerspective(60.0, float(w) / float(h), 0.1, 1000.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        gluLookAt(60, -200, 0, -150, 0, 0, 0, 1, 0)
        glColor3f(0.0, 0.0, 1.0)

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()


if __name__ == '__main__':
    app = QApplication(["hi"])
    widget = TestWidget()
    widget.setWindowTitle("test window")
    widget.show()
    app.exec_()