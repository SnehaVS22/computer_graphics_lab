#program to draw a polygon

from OpenGL.GL import*
from OpenGL.GLUT import*
from OpenGL.GLUT import*
import sys

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("polygon")
    glClearColor(0.0,0.0,0.1,0.0)
    glOrtho(-400,400,-400,400,-1,1)

def polygon():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,0.1,0.1)
    glBegin(GL_POLYGON)
    glVertex2f(-200,-200)
    glVertex2f(200,-200)
    glVertex2f(200,200)
    glVertex2f(200,300)
    glVertex2f(-200,200)
    glEnd()
    glFlush()

def display():
    polygon()

def main():
    init()
    glutDisplayFunc(display)
    glutMainLoop()

main()
