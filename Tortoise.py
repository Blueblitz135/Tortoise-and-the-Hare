# Tortoise.py
# 2022-05-21
# A module for the tortoise

from graphics import *
from SpeechBubble import *

class Tortoise(SpeechBubbleR):
    """ A class for defining the tortoise's position and functions for 
    animating
    """
    def __init__(self):
        """Initilize position of the tortoise's body parts"""
        self.shellTop = Polygon(Point(433, 218), Point(528, 218), 
                                Point(560, 295), Point(401, 295))
                                
        self.shellTop.setFill(color_rgb(106, 168, 79))

        self.shellBot1 = Rectangle(Point(400, 286), Point(448, 302))
        self.shellBot1.setFill("white")

        self.shellBot2 = Rectangle(Point(448, 283), Point(512, 305))
        self.shellBot2.setFill("white")

        self.shellBot3 = Rectangle(Point(512, 286), Point(560, 302))
        self.shellBot3.setFill("white")

        self.neck = Polygon(Point(541, 284), Point(582, 281), Point(586, 301), 
                    Point(545, 304))
        self.neck.setFill(color_rgb(255, 217, 102))

        self.head = Oval(Point(575, 255), Point(635, 307))
        self.head.setFill(color_rgb(255, 217, 102))

        self.pupil = Circle(Point(615, 272), 6)
        self.pupil.setFill("black")

        self.eyeBall = Circle(Point(616, 272), 3)
        self.eyeBall.setFill("white")
        
        self.winkEye = Text(Point(615, 272), ">")
        self.winkEye.setSize(16)

        self.leg1 = Polygon(Point(395, 316), Point(405, 294), Point(428, 303), 
                            Point(417, 325))
        self.leg1.setFill(color_rgb(255, 217, 102))

        self.leg2 = Polygon(Point(440, 327), Point(463, 320), Point(455, 303), 
                            Point(425, 300))
        self.leg2.setFill(color_rgb(255, 217, 102))

        self.leg3 = Polygon(Point(498, 316), Point(508, 294), Point(531, 303), 
                            Point(520, 325))
        self.leg3.setFill(color_rgb(255, 217, 102))

        self.leg4 = Polygon(Point(543, 327), Point(566, 320), Point(558, 303), 
                            Point(528, 300))
        self.leg4.setFill(color_rgb(255, 217, 102))

        self.tail = Polygon(Point(376, 271), Point(409, 276), Point(407, 290), 
                            Point(374, 285))
        self.tail.setFill(color_rgb(255, 217, 102))

        self.happyMouth = Text(Point(613, 291), "w")
        self.happyMouth.setSize(14)

        self.surprisedMouth = Circle(Point(613, 291), 9)
        self.surprisedMouth.setFill("black")

        self.stripe1 = Line(Point(425, 237), Point(536, 237))

        self.stripe2 = Line(Point(420, 254), Point(541, 254))

        self.stripe3 = Line(Point(412, 270), Point(549, 270))
        
        self.stripe4 = Line(Point(460, 220), Point(450, 283))

        self.stripe5 = Line(Point(500, 220), Point(510, 283))

    # Define Functions
    def draw(self, win):
        """Draw the tortoise on a graphics window"""
        self.tail.draw(win)
        self.neck.draw(win)
        self.leg1.draw(win)
        self.leg2.draw(win)
        self.leg3.draw(win) 
        self.leg4.draw(win)
        self.shellTop.draw(win)
        self.shellBot1.draw(win)
        self.shellBot2.draw(win)
        self.shellBot3.draw(win)
        self.head.draw(win)
        self.pupil.draw(win)
        self.eyeBall.draw(win)
        self.stripe1.draw(win)
        self.stripe2.draw(win)
        self.stripe3.draw(win)
        self.stripe4.draw(win)
        self.stripe5.draw(win)
        self.happyMouth.draw(win)

    def move(self, dx, dy):
        """Draw the tortoise on a graphics window"""
        self.tail.move(dx, dy)
        self.neck.move(dx, dy)
        self.leg1.move(dx, dy)
        self.leg2.move(dx, dy)
        self.leg3.move(dx, dy)
        self.leg4.move(dx, dy)
        self.shellTop.move(dx, dy)
        self.shellBot1.move(dx, dy)
        self.shellBot2.move(dx, dy)
        self.shellBot3.move(dx, dy)
        self.head.move(dx, dy)
        self.pupil.move(dx, dy)
        self.eyeBall.move(dx, dy)
        self.winkEye.move(dx, dy)
        self.happyMouth.move(dx, dy)
        self.surprisedMouth.move(dx, dy)
        self.stripe1.move(dx, dy)
        self.stripe2.move(dx, dy)
        self.stripe3.move(dx, dy)
        self.stripe4.move(dx, dy)
        self.stripe5.move(dx, dy)
    
    def setSurprisedFace(self, win):
        """Changes the tortoise's expression to surprised"""
        self.happyMouth.undraw()
        self.surprisedMouth.draw(win)
    
    def setHappyFace(self, win):
        """Changes the tortoise's expression to happy"""
        self.happyMouth.draw(win)
        self.surprisedMouth.undraw()

    def wink(self, win):
        """Allows the tortoise to wink"""
        self.pupil.undraw()
        self.eyeBall.undraw()
        self.winkEye.draw(win)
    
    def unwink(self, win):
        """Allows the toprtoise go back to its normal eye"""
        self.winkEye.undraw()
        self.pupil.draw(win)
        self.eyeBall.draw(win)