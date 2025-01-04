#rotation of points with controls 

from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

angle=0
speed=2

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Rotate animation - point")
    glClearColor(0.0,0.0,0.0,1.0)
    glOrtho(-400,400,-400,400,-1,1)

def point():
    global angle

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(50,10)
    glEnd()

    glPushMatrix()
    glRotatef(angle,0,0,1)
    glColor3f(1.0,1.0,0.0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(50,10)
    glEnd()
    glPopMatrix()

    glFlush()

def update():
    global angle,speed
    angle+=speed
    if angle>=360:
        angle -= 360
    glutPostRedisplay()

def keyboard(key,x1,y1):
    global speed 
    if key==b'w':
        speed+=1
    elif key==b's':
        speed=max(1,speed-1)


def display():
    point()

def main():
    init()
    glutDisplayFunc(display)
    glutIdleFunc(update)
    glutKeyboardFunc(keyboard)
    glutMainLoop()
main()