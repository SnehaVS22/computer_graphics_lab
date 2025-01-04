#scaling of a static triangle 

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

sx=1
sy=1
ss=0.1

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Scaling a Triangle")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glOrtho(-400, 400, -400, 400, -1, 1)

def triangle():
    global sx,sy,ss
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glScalef(sx, sy, 1.0)
    glColor3f(0.0,1.0,0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-100,-100) #if we give different values the shape may run around when scaled
    glVertex2f(100,-100)
    glVertex2f(0,100)
    glEnd()
    glPopMatrix()
    glFlush()
    

def keyboard(key, x, y):
    global sx,sy,ss
    if key == b'w':
        sx+=ss
    elif key == b's':
        sx=max(0.1,sx-ss)
    elif key == b'a':
        sy+=ss
    elif key == b'd':
        sy=max(0.1,sy-ss)
    glutPostRedisplay()

def display():
   triangle()

def main():
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard) 
    glutMainLoop()

main()