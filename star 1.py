#star using two triangles 

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
    glBegin(GL_LINE_LOOP)
    glVertex2f(0,100)
    glVertex2f(-60,-50)
    glVertex2f(60,-50)
    glEnd()
    glFlush()
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-40, 20)  
    glVertex2f(40, 20)    
    glVertex2f(0, -80)  
    glEnd()
    glFlush()

def display():
    triangle()
    

def main():
    init()
    glutDisplayFunc(display)
    glutMainLoop()
main()
