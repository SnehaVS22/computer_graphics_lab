#program for drawing a circle

from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

x=20
y=20

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("circle")
    glClearColor(0.0,0.0,0.1,0.0)
    glOrtho(-400,400,-400,400,-1,1)

def circle():
    global x,y
    r=50
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINE_STRIP) #GL_TRIANGLE_FAN to get filled circle
    glVertex2f(x,y)
    for i in range(0,360,1):#we can get half circle by changing the angle 360 
        glVertex2f(x+r*math.cos(math.radians(i)),y+r*math.sin(math.radians(i)))
    glEnd()
    glFlush()

def display():
    circle()

def main():
    init()
    glutDisplayFunc(display)
    glutMainLoop()

main()
