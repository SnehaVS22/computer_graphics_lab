#translate  of a triangle

from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Line translate")
    glClearColor(0.0,0.0,0.0,1.0)
    glOrtho(-400,400,-400,400,-1,1)

def triangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(20,30)
    glVertex2f(60,30)
    glVertex2f(40,60)
    glEnd()
    glFlush()

    #translate
    glPushMatrix()
    glTranslatef(30,40,0)
    glColor3f(1.0,0.0,1.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(20,30)
    glVertex2f(60,30)
    glVertex2f(40,60)
    glEnd()
    glPopMatrix()
    glFlush()

def display():
    triangle()

def main():
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()