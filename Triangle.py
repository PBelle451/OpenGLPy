from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    Triangle()
    glutSwapBuffers()

def Triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)
    glVertex2f(-0.5, -0.5)
    glColor3f(1, 0, 0)
    glVertex2f(0.5, -0.5)
    glColor3f(0, 0, 1)
    glVertex2f(0.0, 0.5)
    glEnd()

if __name__ == '__main__':
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(860, 600)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow(b"Triangulo do Balacobaco em Python")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutMainLoop()