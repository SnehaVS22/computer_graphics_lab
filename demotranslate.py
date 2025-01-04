
#program to translate a point

from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Translation of point")
    glClearColor(0.0,0.0,0.0,1.0)
    glOrtho(-400,400,-400,400,-1,1)

def point():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2f(50,50)
    glEnd()
    glFlush()

    #Translation 
    glPushMatrix()
    glTranslatef(60,70,0)
    glColor3f(0,1,0)
    glBegin(GL_POINTS)
    glVertex2f(50,50)
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
