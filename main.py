# main.py

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_TRIANGLES)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glVertex3f(1.0, -1.0, 0.0)
    glEnd()
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutCreateWindow(b"OpenGL Window")
    glutDisplayFunc(display)
    glEnable(GL_DEPTH_TEST)
    glutMainLoop()


if __name__ == "__main__":
    main()
