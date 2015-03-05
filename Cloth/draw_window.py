__author__ = 'rachinaahuja'

from PyQt4.QtGui import *
from PyQt4 import QtCore
from PyQt4.QtOpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *

from cloth import ClothSim

import sys
class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.gl_widget=GLWidget()
        #create slider for mass
        self.mass_slider=QSlider(QtCore.Qt.Horizontal)
        self.mass_slider.setRange(0,10.0)
        self.mass_slider.setSingleStep(0.2)
        #create slider for ks
        self.ks_slider=QSlider(QtCore.Qt.Horizontal)
        self.ks_slider.setRange(0,10.0)
        self.ks_slider.setSingleStep(0.2)
        #create slider for kd
        self.kd_slider=QSlider(QtCore.Qt.Horizontal)
        self.kd_slider.setRange(0,10.0)
        self.kd_slider.setSingleStep(0.2)
        #create slider for dt?

        #create layout
        main_layout=QVBoxLayout()
        main_layout.addWidget(self.gl_widget)
        main_layout.addWidget(self.mass_slider)
        main_layout.addWidget(self.ks_slider)
        main_layout.addWidget(self.kd_slider)
        self.setLayout(main_layout)


class GLWidget(QGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.setMinimumHeight(400)
        self.setMinimumWidth(600)
        self.t = 0.0
        self.dt = 1.0/10
        self.myCloth = ClothSim(100, 10, 2.0, self.dt)
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
    app = QApplication(sys.argv)
    window = Window()
    window.setWindowTitle("Mass Spring Cloth")
    window.show()
    app.exec_()