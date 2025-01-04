#program for drawing a square

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(100, 100)  # Set window position
    glutCreateWindow("Draw Square")
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Background color
    glOrtho(-400, 400, -400, 400, -1, 1)  # Set 2D orthographic projection

def draw_square():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glColor3f(0.0, 1.0, 0.0)  # Set color to green
    glBegin(GL_QUADS)  # Start drawing quadrilaterals
    glVertex2f(-100, -100)  # Bottom-left corner
    glVertex2f(100, -100)   # Bottom-right corner
    glVertex2f(100, 100)    # Top-right corner
    glVertex2f(-100, 100)   # Top-left corner
    glEnd()
    glFlush()  # Render the drawing

def display():
    draw_square()

def main():
    init()
    glutDisplayFunc(display)  # Register display callback
    glutMainLoop()  # Start the main loop

main()