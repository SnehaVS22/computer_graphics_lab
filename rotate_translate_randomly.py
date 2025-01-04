#rotate in circle and translate randomly

from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys

Rangle=0
Rspeed=1
Tspeed=2
dx=1
dy=1
dr=1
x=0
y=0

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(100,100)
    glutCreateWindow("Translation of point")
    glClearColor(0.0,0.0,0.0,1.0)
    glOrtho(-400,400,-400,400,-1,1)

def point():
    global x,y,Rangle
    glClear(GL_COLOR_BUFFER_BIT)
    #Translation and rotation 
    glPushMatrix()
    glTranslatef(x,y,0)
    glRotatef(Rangle,0,0,1)
    glColor3f(0,1,0)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex2f(100,0)
    glEnd()
    glPopMatrix()
    glFlush()

def update():
    global Rangle,Rspeed,Tspeed,dx,dy,dr,x,y
    Rangle+=dr*Rspeed
    Rangle%=360
    
    x+=dx*Tspeed
    y+=dy*Tspeed

    if x>400 or x<-400:
        dx*=-1
    elif y>400 or y<-400:
        dy*=-1
    glutPostRedisplay()

def keyboard(key,x1,y1):
    global Rspeed,Tspeed,x,y,dx,dy,dr
    #speed control
    if key==b'w':
        Tspeed+=1
    elif key==b's':
        Tspeed=max(1,Tspeed-1)
    
    if key==b'd':
        Rspeed+=1
    elif key==b'a':
        Rspeed=max(1,Rspeed-1)

    #direction control
    if key==b'i':
        dx*=-1
    elif key==b'k':
        dy*=-1
    elif key==b'l':
        dr*=-1


def display():
    point()

def main():
    init()
    glutDisplayFunc(display)
    glutIdleFunc(update)
    glutKeyboardFunc(keyboard)
    glutMainLoop()
main()