#program for line drawing

from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("line")
    glClearColor(0.0,0.0,0.0,1.0)
    glOrtho(-400,400,-400,400,-1,1)

def line():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(40,50)
    glVertex2f(70,80)
    glEnd()
    glFlush()

def display():
    line()

def main():
    init()
    glutDisplayFunc(display)
    glutMainLoop()
    
main()
