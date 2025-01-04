#program for drawing a rectangle

from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("rectangle")
    glClearColor(0.0,0.0,0.0,1.0)
    glOrtho(-400,400,-400,400,-1,1)

def rectangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_QUADS)
    glVertex2f(-70,-20)
    glVertex2f(70,-20)
    glVertex2f(70,20)
    glVertex2f(-70,20)
    glEnd()
    glFlush()

def display():
    rectangle()

def main():
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()
