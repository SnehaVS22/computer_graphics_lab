#tap

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Tap rotation variables
tap_angle = 0  # Current angle of the tap
tap_state = "OFF"  # "ON" or "OFF"

# Water flow variables
water_y = 200  # Initial Y position of the water
water_speed = 2  # Speed of water flow
bucket_fill_height = 0  # Current height of water in the bucket
bucket_capacity = 150  # Maximum height of water in the bucket
bucket_filling = False  # Whether the bucket is being filled

def init():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Tap Filling a Bucket")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glOrtho(-400, 400, -300, 300, -1, 1)

def draw_tap():
    global tap_angle

    # Draw the tap
    glPushMatrix()
    glTranslatef(-200, 200, 0)  # Move to tap position
    glRotatef(tap_angle, 0, 0, 1)  # Rotate the tap
    glColor3f(0.6, 0.6, 0.6)  # Gray color for tap
    glBegin(GL_POLYGON)
    glVertex2f(-80, 0)
    glVertex2f(80, 0)
    glVertex2f(80, -10)
    glVertex2f(-80, -10)
    glEnd()
    glPopMatrix()


def draw_water():
    global water_y

    # Draw the water droplets
    if tap_state == "ON" and water_y > -150:
        glColor3f(0.0, 0.0, 1.0)  # Blue color for water
        glBegin(GL_POLYGON)
        for angle in range(0, 360, 10):
            rad = math.radians(angle)
            x = math.cos(rad) * 10
            y = math.sin(rad) * 10
            glVertex2f(x - 120, y + water_y)
        glEnd()

def draw_bucket():
    global bucket_fill_height

    # Draw the bucket
    glColor3f(0.5, 0.2, 0.0)  # Brown color for bucket
    glBegin(GL_LINE_LOOP)
    glVertex2f(-150, -150)
    glVertex2f(-150, -200)
    glVertex2f(150, -200)
    glVertex2f(150, -150)
    glEnd()

    # Draw the water inside the bucket
    if bucket_fill_height > 0:
        glColor3f(0.0, 0.0, 1.0)  # Blue color for water
        glBegin(GL_POLYGON)
        glVertex2f(-150, -200)
        glVertex2f(150, -200)
        glVertex2f(150, -200 + bucket_fill_height)
        glVertex2f(-150, -200 + bucket_fill_height)
        glEnd()

def update(value):
    global tap_angle, water_y, bucket_fill_height, bucket_filling

    if tap_state == "ON":
        # Rotate the tap to "ON" position
        if tap_angle < 45:
            tap_angle += 2

        # Animate the water flow
        water_y -= water_speed

        # Reset water droplet and fill the bucket
        if water_y < -150:
            water_y = 200
            if bucket_fill_height < bucket_capacity:
                bucket_fill_height += 5

    elif tap_state == "OFF":
        # Rotate the tap to "OFF" position
        if tap_angle > 0:
            tap_angle -= 2

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def keyboard(key, x, y):
    global tap_state

    if key == b'o':  # Turn tap ON
        tap_state = "ON"
    elif key == b'f':  # Turn tap OFF
        tap_state = "OFF"

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    draw_tap()
    draw_water()
    draw_bucket()

    glFlush()

def main():
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(16, update, 0)
    glutMainLoop()

main()