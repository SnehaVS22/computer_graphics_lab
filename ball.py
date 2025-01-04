#ball rolling down a slope

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Global variables for animation
change_x = 0   # Horizontal movement of the circle
change_y = 0   # Vertical movement of the circle
angle = 0      # Rotation angle of the circle

# Function to initialize the OpenGL environment
def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)  # RGB display and double buffering
    glutInitWindowPosition(500, 500)            # Window position
    glutInitWindowSize(500, 500)                # Window size
    glutCreateWindow("Rotating Circle on Slope with Line")  # Window title
    glClearColor(1, 1, 1, 1)                    # Background color: white
    gluOrtho2D(-400, 400, -400, 400)            # Set 2D orthographic projection

# Function to draw the slope and the rotating circle with the line
             # Clear the screen

def slope():
    # Draw the slope using lines
    glColor3f(1, 0, 0)                          # Red color for slope
    glBegin(GL_LINES)
    glVertex2f(-250, 250)                       # Start point of the slope
    glVertex2f(0, 0)                            # Middle point of the slope
    glVertex2f(0, 0)                            # Middle point to flat surface
    glVertex2f(250,0)                        # Flat surface
    glEnd()
    glFlush()

def ball():
    # Draw the rotating circle (wheel)
   
    glTranslatef(change_x, change_y, 0)         # Move the circle
    glRotatef(angle, 0, 0, 1)                   # Rotate the circle

    # Circle
                         # Circle as points
    glColor3f(1, 0, 1)
    glBegin(GL_LINE_STRIP)                               # Magenta color for circle
    r=30
    for i in range(1,361):
        x=r*math.cos(math.radians(i))  
        y=r*math.sin(math.radians(i)) 
        glVertex2f(x,y)                       # Increment angle
    glEnd()
    glFlush()

    # Rotating line from center to circumference
    glBegin(GL_LINES)
    glColor3f(0, 0, 1)                          # Blue color for the line
    glVertex2f(0, 0)                            # Start from the center
    glVertex2f(30, 0)                           # End at the circumference
    glEnd()
    glFlush()
                              # Swap the buffers for animation

def draw():
    global change_x, change_y, angle

    glClear(GL_COLOR_BUFFER_BIT)   
    glPushMatrix()
    slope()
    ball()
    glPopMatrix()
    glutSwapBuffers()
# Timer function for animation updates
def update(value):
    global change_x, change_y, angle

    # Update the horizontal position and rotation angle
    change_x += 1
    angle -= 3  # Counter-clockwise rotation

    # Handle the movement down the slope and on the flat surface
    if change_x >= 250:                         # If the circle reaches the end of the flat surface
        change_x = -250                         # Reset the position to start again
        change_y = 250                          # Reset to the top of the slope
    elif change_x <= 0:
        change_y -= 1                           # Move down the slope

    glutPostRedisplay()                         # Request redraw
    glutTimerFunc(10, update, 0)                # Call update function again after 10 ms

def display():
    draw()
# Main function
def main():
    init()
    glutDisplayFunc(display)                 # Set the display function
    glutTimerFunc(0, update, 0)                 # Start the timer for animation
    glutMainLoop()                              # Enter the main loop

main()