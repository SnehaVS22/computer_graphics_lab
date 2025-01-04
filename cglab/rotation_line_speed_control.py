#rotation of line with rotation speed conrol

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
    glutCreateWindow("Rotate animation - line")
    glClearColor(0.0,0.0,0.0,1.0)
    glOrtho(-400,400,-400,400,-1,1)

def line():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,0.0)
    glPushMatrix()
    glRotatef(angle,0,0,1)
    glBegin(GL_LINES)
    glVertex2f(100,0)
    glVertex2f(120,200)
    glEnd()
    glPopMatrix()
    glFlush()

def update():
    global angle,speed
    angle+=speed
    if angle>=360:
        angle=-360
    glutPostRedisplay()

def keyboard(key,x1,y1):
    global speed 
    if key==b'w':
        speed+=1
    elif key==b's':
        speed=max(1,speed-1)

def display():
    line()

def main():
    init()
    glutDisplayFunc(display)
    glutIdleFunc(update)
    glutKeyboardFunc(keyboard)
    glutMainLoop()
main()