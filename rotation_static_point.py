# rotation of a point static 

from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Rotate animation - point")
    glClearColor(0.0,0.0,0.0,1.0)
    glOrtho(-400,400,-400,400,-1,1)

def point():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(50,10)
    glEnd()
    glFlush()

    glPushMatrix()
    glColor3f(1.0,1.0,0.0)
    glPointSize(10)
    glRotatef(45,0,0,1)
    glBegin(GL_POINTS)
    glVertex2f(50,10)
    glEnd()
    glPopMatrix()
    glFlush()

def display():
    point()

def main():
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()
