#program for drawing a triangle

from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("triangle")
    glClearColor(0.0,0.0,0.0,1.0)
    glOrtho(-400,400,-400,400,-1,1)

def triangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_TRIANGLES) #GL_LINE_LOOP to draw a triangle that is not filled 
    glVertex2f(20,20)
    glVertex2f(60,20)
    glVertex2f(40,40)
    glEnd()
    glFlush()

def display():
    triangle()


def main():
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()

#program for drawing a inverted triangle

from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("triangle")
    glClearColor(0.0,0.0,0.0,1.0)
    glOrtho(-400,400,-400,400,-1,1)

def triangle():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(20,20)
    glVertex2f(60,20)
    glVertex2f(40,-40) #change the value here 
    glEnd()
    glFlush()

def display():
    triangle()


def main():
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()

