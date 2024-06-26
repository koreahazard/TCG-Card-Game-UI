import math
import random
import tkinter as tk
import unittest

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from pyopengltk import OpenGLFrame

class LightningSegment:
    def __init__(self, start, end, brightness=1.0):
        self.start = start
        self.end = end
        self.brightness = brightness

def average(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def normalize(vector):
    length = (vector[0]**2 + vector[1]**2)**0.5
    return (vector[0] / length, vector[1] / length)

def perpendicular(vector):
    return (-vector[1], vector[0])

def rotate(vector, angle):
    x = vector[0] * math.cos(angle) - vector[1] * math.sin(angle)
    y = vector[0] * math.sin(angle) + vector[1] * math.cos(angle)
    return (x, y)

def random_float(min_val, max_val):
    return random.uniform(min_val, max_val)

def generate_lightning(start_point, end_point, maximum_offset, num_generations, branch_probability, length_scale):
    segment_list = [LightningSegment(start_point, end_point)]
    offset_amount = maximum_offset

    for generation in range(num_generations):
        for segment in segment_list[:]:
            segment_list.remove(segment)

            mid_point = average(segment.start, segment.end)
            direction = normalize((segment.end[0] - segment.start[0], segment.end[1] - segment.start[1]))
            normal = perpendicular(direction)

            mid_point = (mid_point[0] + normal[0] * random_float(-offset_amount, offset_amount),
                         mid_point[1] + normal[1] * random_float(-offset_amount, offset_amount))

            segment_list.append(LightningSegment(segment.start, mid_point, segment.brightness))
            segment_list.append(LightningSegment(mid_point, segment.end, segment.brightness))

            if generation % 2 == 0 and random.random() < branch_probability:
                branch_direction = rotate(direction, random_float(-math.pi / 2, math.pi / 2))
                split_end = (mid_point[0] + branch_direction[0] * length_scale,
                             mid_point[1] + branch_direction[1] * length_scale)

                segment_list.append(LightningSegment(mid_point, split_end, segment.brightness * 0.5))

        offset_amount /= 2.5

    return segment_list

class RectDrawingApp(OpenGLFrame):

    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.padding = 5
        self.inner_left = -30 + self.padding
        self.inner_right = 30 - self.padding
        self.inner_bottom = -45 + self.padding
        self.inner_top = 45 - self.padding

    def initgl(self):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        gluOrtho2D(-100.0, 100.0, -100.0, 100.0)

    def redraw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0)

        glBegin(GL_POLYGON)
        glVertex2f(self.inner_left, self.inner_bottom)
        glVertex2f(self.inner_right, self.inner_bottom)
        glVertex2f(self.inner_right, self.inner_top)
        glVertex2f(self.inner_left, self.inner_top)
        glEnd()

        lightning_segments = generate_lightning((self.inner_left - 10, self.inner_bottom - 10), (self.inner_right + 10, self.inner_bottom - 10), 10, 5, 0.2, 0.7)
        lightning_segments.extend(generate_lightning((self.inner_right + 10, self.inner_bottom - 10), (self.inner_right + 10, self.inner_top + 10), 10, 5, 0.2, 0.7))
        lightning_segments.extend(generate_lightning((self.inner_left - 10, self.inner_top + 10), (self.inner_right + 10, self.inner_top + 10), 10, 5, 0.2, 0.7))
        lightning_segments.extend(generate_lightning((self.inner_left - 10, self.inner_bottom - 10), (self.inner_left - 10, self.inner_top + 10), 10, 5, 0.2, 0.7))

        for segment in lightning_segments:
            self.draw_lightning_segment(segment)

        self.tkSwapBuffers()

    def draw_lightning_segment(self, segment):
        glLineWidth(3.0)
        neon_color = (0.0, 0.78, 0.34, segment.brightness)

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glColor4fv(neon_color)

        glBegin(GL_LINE_STRIP)
        glVertex2f(segment.start[0], segment.start[1])
        glVertex2f(segment.end[0], segment.end[1])
        glEnd()

        glDisable(GL_BLEND)

class TestAppWindow(unittest.TestCase):
    def test_lightning_border(self):
        root = tk.Tk()
        root.title("OpenGL Rectangle Drawing")

        app = RectDrawingApp(root, width=400, height=400)
        app.pack(side="top", fill="both", expand=True)
        app.animate = 1
        root.mainloop()

if __name__ == '__main__':
    unittest.main()
