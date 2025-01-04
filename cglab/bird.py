
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Global variables for animation
bird_x = -200  # Initial position of the bird (x-coordinate)
bird_y = 100   # Initial position of the bird (y-coordinate)
wing_angle = 0  # Angle for wing flapping
flap_direction = 1  # Direction of wing flap (1: up, -1: down)

# Function to initialize the OpenGL environment
def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)  # RGB display and double buffering
    glutInitWindowSize(800, 600)                # Window size
    glutInitWindowPosition(100, 100)            # Window position
    glutCreateWindow("Flying Bird Animation")   # Window title
    glClearColor(0.5, 0.8, 1.0, 1.0)            # Background color: sky blue
    gluOrtho2D(-400, 400, -300, 300)            # Set 2D orthographic projection

# Function to draw the bird's body
def draw_body():
    glColor3f(0, 0, 0)  # Black color for the body
    glBegin(GL_POLYGON)
    for angle in range(0, 360, 10):
        x = 30 * math.cos(math.radians(angle))
        y = 20 * math.sin(math.radians(angle))
        glVertex2f(x, y)
    glEnd()

# Function to draw a wing
def draw_wing(angle):
    glPushMatrix()
    glRotatef(angle, 0, 0, 1)  # Rotate the wing
    glBegin(GL_TRIANGLES)
    glColor3f(0.2, 0.2, 0.8)  # Dark blue color for wings
    glVertex2f(0, 0)
    glVertex2f(-40, -20)
    glVertex2f(-40, 20)
    glEnd()
    glPopMatrix()

# Function to draw the bird
def draw_bird():
    glPushMatrix()
    glTranslatef(bird_x, bird_y, 0)  # Move the bird
    draw_body()  # Draw the body
    draw_wing(wing_angle)  # Draw the right wing
    draw_wing(-wing_angle)  # Draw the left wing
    glPopMatrix()

# Function to draw the scene
def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    # Draw the bird
    draw_bird()

    glutSwapBuffers()  # Swap the buffers for animation

# Timer function for animation updates
def update(value):
    global bird_x, wing_angle, flap_direction

    # Move the bird horizontally
    bird_x += 2
    if bird_x > 400:  # Reset position when the bird moves off-screen
        bird_x = -400

    # Animate wing flapping
    wing_angle += 5 * flap_direction
    if wing_angle > 30 or wing_angle < -30:  # Reverse direction at limits
        flap_direction *= -1

    glutPostRedisplay()  # Request redraw
    glutTimerFunc(20, update, 0)  # Call update again after 20 ms

# Main function
def main():
    init()
    glutDisplayFunc(draw_scene)  # Set the display function
    glutTimerFunc(0, update, 0)  # Start the timer for animation
    glutMainLoop()  # Enter the main loop

main()
