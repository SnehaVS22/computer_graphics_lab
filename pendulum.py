#pendulum

from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

angle=45
d=-1
speed=0.01

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("clock")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(-400,400,-400,400,-1,1)

def bob():
    glColor3f(0,1,1)
    glPointSize(20)
    glBegin(GL_POINTS)
    x=150*math.sin(math.radians(angle))
    y=200-150*math.cos(math.radians(angle))
    glVertex2f(x,y)
    glEnd()
    glFlush()

def rod():
    glColor3f(0,0,1)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(0,200)
    x=150*math.sin(math.radians(angle))
    y=200-150*math.cos(math.radians(angle))
    glVertex2f(x,y)
    glEnd()
    glFlush()

def pivot():
    glColor3f(0,1,0)
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(0,200)
    glEnd()
    glFlush()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    pivot()
    rod()
    bob()
    glPopMatrix()     
    glutSwapBuffers()
    

def update(value):
    global angle,speed,d
    angle+=speed*d*100
    if angle>45 or angle<-45:
        d*=-1
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def keyboard(key,x,y):
    global angle,speed,d
    if key==b'+':
        speed+=0.01
    elif key==b'-':
        speed-=0.01
    


def display():
    draw()

def main():
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0,update,0)
    glutMainLoop()
main()