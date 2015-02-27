__author__ = 'rachinaahuja'

from PyQt4.QtGui import *
from PyQt4.QtOpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *

from particle import ParticleClass


class TestWidget(QGLWidget):
    def __init__(self, parent=None):
        super(TestWidget, self).__init__(parent)
        self.positions = []

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        gluLookAt(0, 5, 40, 0, 0, 0, 0, 1, 0)
        glColor3f(0.0, 0.0, 1.0)
        glRectf(-5, -5, 5, 5)
        for p in self.positions:
            particle = ParticleClass()
            particle.draw_particle(p)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        # glViewport(0,0,w,h)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluPerspective(60.0, float(w) / float(h), 0.1, 1000.0)

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # only initializing, find a better place for this :/
        self.positions = [(x, 0, z) for x in range(-50, 50, 10) for z in range(-50, 50, 10)]


if __name__ == '__main__':
    app = QApplication(["hi"])
    widget = TestWidget()
    widget.setWindowTitle("test window")
    widget.show()
    app.exec_()