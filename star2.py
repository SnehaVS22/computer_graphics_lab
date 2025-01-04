#star using  two triangle
#1 trianglr rotates in one direction while other in other direction
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

angle1 = 0  # Rotation angle for the first triangle
angle2 = 0  # Rotation angle for the second triangle (opposite direction)
speed = 0.5  # Speed of rotation

# Initialization function
def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Rotating Star")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(-400, 400, -400, 400, -1, 1)

# Function to draw a triangle
def draw_triangle():
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 100)
    glVertex2f(100, -100)
    glVertex2f(-100, -100)
    glEnd()

# Function to draw the star (two rotating triangles)
def draw_star():
    global angle1, angle2
    glClear(GL_COLOR_BUFFER_BIT)
    # Draw the first triangle (rotating in one direction)
    glPushMatrix()
    glRotatef(angle1, 0, 0, 1)  # Rotate the first triangle
    glColor3f(1, 0, 0)  # Red color
    draw_triangle()
    glPopMatrix()

    # Draw the second triangle (rotating in the opposite direction)
    glPushMatrix()
    glRotatef(angle2, 0, 0, 1)  # Rotate the second triangle
    glColor3f(0, 0, 1)  # Blue color
    draw_triangle()
    glPopMatrix()
    glutSwapBuffers()

# Update the angles for animation
def update():
    global angle1, angle2
    angle1 += speed  # Rotate first triangle clockwise
    angle2 -= speed  # Rotate second triangle counter-clockwise

    if angle1 > 360:
        angle1 -= 360
    if angle2 < -360:
        angle2 += 360

    glutPostRedisplay()  # Request a redraw
    glutTimerFunc(16, update, 0)  # Redraw every 16 ms (approximately 60 FPS)

# Display function
def display():
   
    draw_star()  # Draw the rotating star
   

# Main function
def main():
    init()
    glutDisplayFunc(display)
    glutTimerFunc(16, update, 0)
    glutMainLoop()

main()
