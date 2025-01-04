# animation of a point with controls(translation)

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

speed=1
x=0
y=0
dx=1
dy=1

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("point animation")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glOrtho(-400,400,-400,400,-1,1)

def point():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(10.0)
    glPushMatrix()
    glTranslatef(x,y,0)
    glBegin(GL_POINTS)
    glVertex2f(50, 50)
    glEnd()
    glPopMatrix()
    glFlush()

def update():
    global x,y,speed,dx,dy

    #update position based on speed and direction
    x+=dx*speed
    y+=dy*speed

    #check for collision with boundaries
    if x>400 or x<-400:
        dx*=-1
    if y>400 or y<-400:
        dy*=-1
    glutPostRedisplay()

def keyboard(key,x1,y1):
    global speed,dx,dy

    #adjust speed
    if key ==b'w':
        speed+=1
    elif key==b's':
        speed=max(1,speed-1)
    #adjusting the direction 
    if key==b'i':
        dx=-1
    elif key==b'k':
        dx=1
    elif key==b'j':
        dy=-1
    elif key==b'l':
        dy=1

def display():
    point()

def main():
    init()
    glutDisplayFunc(display)
    glutIdleFunc(update)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

main()