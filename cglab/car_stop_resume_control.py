#car with control to stop and resume

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Globals for position, direction, speed, and control state
x1 = 0
y1 = 0
dx1 = 1
dy1 = 0
speed = 1
angle = 0
paused = False  # State to track if the car is paused

def init():
    """Initialize OpenGL settings."""
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Car Animation with Stop/Resume")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glOrtho(-400, 400, -400, 400, -1, 1)

def draw_body():
    """Draw the car body as a rectangle."""
    glColor3f(1, 0, 0)  # Red color
    glBegin(GL_QUADS)
    glVertex2f(-100, -50)
    glVertex2f(100, -50)
    glVertex2f(100, 50)
    glVertex2f(-100, 50)
    glEnd()

def draw_wheel(dx, dy):
    """Draw a wheel as a circle at a specified offset."""
    glColor3f(0, 0, 1)  # Blue color
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(dx, dy)  # Center of the wheel
    r = 20  # Radius of the wheel
    for i in range(361):
        x = dx + r * math.cos(math.radians(i))
        y = dy + r * math.sin(math.radians(i))
        glVertex2f(x, y)
    glEnd()
    # Draw the line indicating rotation
    glColor3f(1, 1, 0)  # Yellow color
    glBegin(GL_LINES)
    glVertex2f(dx, dy)
    glVertex2f(dx + r * math.cos(math.radians(angle)), dy + r * math.sin(math.radians(angle)))
    glEnd()

def draw_car():
    """Draw the car with body and wheels."""
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(x1, y1, 0)  # Translate the car
    draw_body()
    # Draw wheels relative to the car body
    draw_wheel(-70, -60)  # Left wheel
    draw_wheel(70, -60)   # Right wheel
    glPopMatrix()
    glutSwapBuffers()

def display():
    """Display callback to render the car."""
    
    draw_car()
  

def update(value):
    """Update the car's position."""
    global x1, y1, dx1, dy1, speed, angle, paused

    if not paused:
        # Update position based on direction and speed
        x1 += dx1 * speed
        y1 += dy1 * speed

        # Boundary check and bounce
        if x1 > 350 or x1 < -350:
            dx1 *= -1
        if y1 > 350 or y1 < -350:
            dy1 *= -1

    # Increment angle for wheel rotation
    angle +=5

    # Request redisplay and schedule the next update
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # Roughly 60 FPS

def keyboard(key, x, y):
    """Keyboard callback for controls."""
    global speed, dx1, dy1, angle, paused

    if key == b'w':  # Increase speed
        speed += 0.5
    elif key == b's':  # Decrease speed
        speed = max(0.5, speed - 0.5)
    elif key == b'a':  # Turn left
        angle -= 5
        dx1 = math.cos(math.radians(angle))
        dy1 = math.sin(math.radians(angle))
    elif key == b'd':  # Turn right
        angle += 5
        dx1 = math.cos(math.radians(angle))
        dy1 = math.sin(math.radians(angle))
    elif key == b'p':  # Pause
        paused = True
    elif key == b'r':  # Resume
        paused = False

def main():
    """Main function to initialize and run the program."""
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(16, update, 0)
    glutMainLoop()

main()
