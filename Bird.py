# Bird.py
# Aidan Leung
# 2022-05-21
# A module for the bird

from graphics import *
from SpeechBubble import *

class Bird(SpeechBubbleL):
    """ A class for defining the bird's position and functions for 
    animating
    """
    def __init__(self):
        """Initialize position of the bird's body parts"""
        self.head = Circle(Point(480, 350), 20)
        self.head.setFill(color_rgb(255, 255, 0))

        self.body = Oval(Point(460, 363), Point(500, 414))
        self.body.setFill(color_rgb(255, 255, 0))

        self.pupil1 = Circle(Point(471, 347), 3)
        self.pupil1.setFill("black")

        self.eyeBall1 = Circle(Point(470, 346), 1)
        self.eyeBall1.setFill("white")

        self.pupil2 = Circle(Point(489, 347), 3)
        self.pupil2.setFill("black")

        self.eyeBall2 = Circle(Point(490, 346), 1)
        self.eyeBall2.setFill("white")

        self.beak = Polygon(Point(474, 358), Point(486, 358), Point(480, 377))
        self.beak.setFill(color_rgb(255, 153, 0))

        self.arm1 = Line(Point(460, 383), Point(445, 370))
        self.arm1.setWidth(2)

        self.arm2 = Line(Point(500, 383), Point(515, 370))
        self.arm2.setWidth(2)

        self.leg1 = Line(Point(469, 408), Point(464, 428))
        self.leg1.setWidth(2)

        self.leg2 = Line(Point(491, 408), Point(496, 428))
        self.leg2.setWidth(2)

    def draw(self, win):
        """Draw the bird on a graphics window"""
        self.body.draw(win)
        self.head.draw(win)
        self.arm1.draw(win)
        self.arm2.draw(win)
        self.pupil1.draw(win)
        self.eyeBall1.draw(win)
        self.pupil2.draw(win)
        self.eyeBall2.draw(win)
        self.leg1.draw(win)
        self.leg2.draw(win)
        self.beak.draw(win)
    
    def move(self, dx, dy):
        """Moves the bird to another position"""
        self.body.move(dx, dy)
        self.head.move(dx, dy)
        self.arm1.move(dx, dy)
        self.arm2.move(dx, dy)
        self.pupil1.move(dx, dy)
        self.eyeBall1.move(dx, dy)
        self.pupil2.move(dx, dy)
        self.eyeBall2.move(dx, dy)
        self.leg1.move(dx, dy)
        self.leg2.move(dx, dy)
        self.beak.move(dx, dy)