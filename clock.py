#clock animation

from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

sec,mint,hr=0,0,0
def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("clock")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(-400,400,-400,400,-1,1)

def orbit():
    glColor3f(0,0,0)
    glBegin(GL_LINE_LOOP)
    for i in range(1,361):
        x=300*math.cos(math.radians(i))
        y=300*math.sin(math.radians(i))
        glVertex2f(x,y)
    glEnd()
    glFlush()
    glColor3f(0,0,0)
    glPointSize(5)
    glBegin(GL_POINTS)
    for i in range(1,361,30):
        x=270*math.cos(math.radians(i))
        y=270*math.sin(math.radians(i))
        glVertex2f(x,y)
    glEnd()
    glFlush()

def point():
    glColor3f(1,1,0)
    glBegin(GL_POINTS)
    glVertex2f(0,0)
    glEnd()
    glFlush()

def line(x):
    glColor3f(1,0,1)
    glLineWidth(4)
    glBegin(GL_LINES)
    glVertex2f(0,-15)
    glVertex2f(0,x)
    glEnd()
    glFlush()

def draw():
    global mint,sec,hr
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    orbit()
    glColor3f(0.0,1.0,0.0)
    glRotatef(sec,0,0,1)
    line(250)
    glPopMatrix()
    glPushMatrix()
    glColor3f(1.0,0.0,0.0)
    glRotatef(mint,0,0,1)
    line(200)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.0,0.0,1.0)
    glRotatef(hr,0,0,1)
    line(150)
    glPopMatrix()
    point()
    glutSwapBuffers()


def update(temp):
    global mint,sec,hr
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),update,int(0))
    sec-=10
    mint=sec/60
    hr=mint/60
  

def display():
    draw()

def main():
    init()
    glutDisplayFunc(display)
    glutTimerFunc(0,update,0)
    glutMainLoop()
main()