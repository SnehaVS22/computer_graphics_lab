
#animation of triangle with control (translation)

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

x=0
y=0
speed=2
dx=1
dy=1

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("triangle animation")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glOrtho(-400,400,-400,400,-1,1)

def triangle():
    global x,y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,0.0)
    glPushMatrix()
    glTranslatef(x,y,0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-200,0)
    glVertex2f(200,0)
    glVertex2f(0,200)
    glEnd()
    glPopMatrix()
    glFlush()

def update():
    global x,y,speed,dx,dy
    x+=dx*speed
    y+=dy*speed
    if x>400 or x<-400:
        dx*=-1
    if y>400 or y<-400:
        dy*=-1
    glutPostRedisplay()

def keyboard(key,x1,y1):
    global speed,dx,dy
    if key==b'w':
        speed+=1
    elif key==b's':
        speed=max(1,speed-1)

    if key==b'i':
        dx=1
    elif key==b'k':
        dx=-1
    elif key==b'l':
        dy=-1
    elif key==b'j':
        dy=1


def display():
    triangle()

def main():
    init()
    glutDisplayFunc(display)
    glutIdleFunc(update)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

main()

#animation of triangle with control (translation)

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

x=0
y=0
speed=2
dx=1
dy=1

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("triangle animation")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glOrtho(-400,400,-400,400,-1,1)

def triangle():
    global x,y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,0.0)
    glPushMatrix()
    glTranslatef(x,y,0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-200,0)
    glVertex2f(200,0)
    glVertex2f(0,200)
    glEnd()
    glPopMatrix()
    glFlush()

def update():
    global x,y,speed,dx,dy
    x+=dx*speed
    y+=dy*speed
    if x>400 or x<-400:
        dx*=-1
    if y>400 or y<-400:
        dy*=-1
    glutPostRedisplay()

def keyboard(key,x1,y1):
    global speed,dx,dy
    if key==b'w':
        speed+=1
    elif key==b's':
        speed=max(1,speed-1)

    if key==b'i':
        dx=1
    elif key==b'k':
        dx=-1
    elif key==b'l':
        dy=-1
    elif key==b'j':
        dy=1


def display():
    triangle()

def main():
    init()
    glutDisplayFunc(display)
    glutIdleFunc(update)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

main()
