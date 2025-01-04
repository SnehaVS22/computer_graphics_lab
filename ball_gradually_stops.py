
#ball same as above
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Globals for position, direction, speed, and control state
x1 = 0  # Position
y1 = 0
dx1 = 1  # Direction
dy1 = 0
speed = 5  # Initial speed
angle = 0  # Rotation angle for the ball

def init():
    """Initialize OpenGL settings."""
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Ball Animation with Gradual Stop")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(-400, 400, -400, 400, -1, 1)

def draw_ball():
    """Draw the ball as a circle with a rotating line."""
    glColor3f(0, 0, 1)  # Blue color for the ball
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)  # Center of the ball
    r = 50  # Radius of the ball
    for i in range(361):
        x = r * math.cos(math.radians(i))
        y = r * math.sin(math.radians(i))
        glVertex2f(x, y)
    glEnd()

    # Draw a line on the ball to indicate rotation
    glColor3f(1, 1, 0)  # Yellow color for the line
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(r * math.cos(math.radians(angle)), r * math.sin(math.radians(angle)))
    glEnd()

def display():
    """Display callback to render the ball."""
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(x1, y1, 0)  # Translate the ball
    draw_ball()
    glPopMatrix()
    glutSwapBuffers()

def update(value):
    """Update the ball's position and rotation."""
    global x1, y1, dx1, dy1, speed, angle

    # Update position based on direction and speed
    if speed > 0:
        x1 += dx1 * speed
        y1 += dy1 * speed

        # Gradually decrease speed
        speed -= 0.05  # Slowdown rate
        angle += 5  # Speed of rotation
        angle %= 360  # Keep angle within 0-360 degrees

        # Stop the ball completely if speed drops below a threshold
        if speed < 0.01:
            speed = 0

    # Boundary check and bounce
    if x1 > 350 or x1 < -350:
        dx1 *= -1
    if y1 > 350 or y1 < -350:
        dy1 *= -1

    # Request redisplay and schedule the next update
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # Roughly 60 FPS

def keyboard(key, x, y):
    """Keyboard callback for controls."""
    global speed, dx1, dy1, angle

    if key == b'r':  # Restart the ball
        speed = 5  # Reset speed to initial value
        angle = 0  # Reset rotation

def main():
    """Main function to initialize and run the program."""
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(16, update, 0)
    glutMainLoop()

main()
