# Hare.py
# Aidan Leung
# 2022-05-21
# A module for the hare

from graphics import *
from SpeechBubble import *

class HareLeft(SpeechBubbleL):
    """A class for defining attributes of the hare facing right"""
    def __init__(self):
        """Initialize position of the hare body parts"""
        self.head = Circle(Point(495, 315), 38)
        self.head.setFill(color_rgb(224, 208, 200))

        self.body = Oval(Point(500, 312), Point(620, 394))
        self.body.setFill(color_rgb(224, 208, 200))

        self.pupil1 = Circle(Point(473, 307), 6)
        self.pupil1.setFill("black")

        self.eyeBall1 = Circle(Point(470, 305), 2)
        self.eyeBall1.setFill("white")

        self.pupil2 = Circle(Point(501, 307), 6)
        self.pupil2.setFill("black")

        self.eyeBall2 = Circle(Point(499, 305), 2)
        self.eyeBall2.setFill("white")

        self.sleepEye1 = Line(Point(470, 305), Point(486, 305))

        self.sleepEye2 = Line(Point(498, 305), Point(514, 305))

        self.mouth = Oval(Point(480, 315), Point(507, 347))
        self.mouth.setFill("black")

        self.mouthCover = Oval(Point(476, 315), Point(514, 329))
        self.mouthCover.setFill(color_rgb(224, 208, 200))
        self.mouthCover.setOutline(color_rgb(224, 208, 200))

        self.ear1Ex = Oval(Point(465, 243), Point(485, 300))
        self.ear1Ex.setFill(color_rgb(224, 208, 200))

        self.ear1In = Oval(Point(471, 252), Point(479, 291))
        self.ear1In.setFill(color_rgb(255, 119, 255))

        self.ear2Ex = Oval(Point(507, 243), Point(527, 300))
        self.ear2Ex.setFill(color_rgb(224, 208, 200))

        self.ear2In = Oval(Point(513, 252), Point(521, 291))
        self.ear2In.setFill(color_rgb(255, 119, 255))

        self.hand = Circle(Point(493, 363), 12)
        self.hand.setFill(color_rgb(224, 208, 200))

        self.leg1 = Oval(Point(523, 375), Point(545, 408))
        self.leg1.setFill(color_rgb(224, 208, 200))

        self.leg2 = Oval(Point(553, 375), Point(575, 408))
        self.leg2.setFill(color_rgb(224, 208, 200))

        self.leg3 = Oval(Point(583, 375), Point(605, 408))
        self.leg3.setFill(color_rgb(224, 208, 200))

        self.tail = Circle(Point(627, 352), 14)
        self.tail.setFill(color_rgb(224, 208, 200))

    def draw(self, win):
        """Draws the hare on the graphics window"""
        self.tail.draw(win)
        self.leg1.draw(win)
        self.leg2.draw(win)
        self.leg3.draw(win) 
        self.ear1Ex.draw(win)
        self.ear1In.draw(win)
        self.ear2Ex.draw(win)
        self.ear2In.draw(win)
        self.body.draw(win)
        self.head.draw(win)
        self.pupil1.draw(win)
        self.eyeBall1.draw(win)
        self.pupil2.draw(win)
        self.eyeBall2.draw(win)
        self.mouth.draw(win)
        self.mouthCover.draw(win)
        self.hand.draw(win)

    def undraw(self):
        """Undraws the hare on the graphics window"""
        self.tail.undraw()
        self.leg1.undraw()
        self.leg2.undraw()
        self.leg3.undraw()
        self.ear1Ex.undraw()
        self.ear1In.undraw()
        self.ear2Ex.undraw()
        self.ear2In.undraw()
        self.body.undraw()
        self.head.undraw()
        self.pupil1.undraw()
        self.eyeBall1.undraw()
        self.pupil2.undraw()
        self.eyeBall2.undraw()
        self.mouth.undraw()
        self.mouthCover.undraw()
        self.hand.undraw()
        
    def move(self, dx, dy):
        """Moves the hare on the graphics window"""
        self.tail.move(dx, dy)
        self.hand.move(dx, dy)
        self.leg1.move(dx, dy)
        self.leg2.move(dx, dy)
        self.leg3.move(dx, dy)
        self.body.move(dx, dy)
        self.head.move(dx, dy)
        self.pupil1.move(dx, dy)
        self.eyeBall1.move(dx, dy)
        self.pupil2.move(dx, dy)
        self.eyeBall2.move(dx, dy)
        self.sleepEye1.move(dx, dy)
        self.sleepEye2.move(dx, dy)
        self.mouth.move(dx, dy)
        self.mouthCover.move(dx, dy)
        self.ear1Ex.move(dx, dy)
        self.ear1In.move(dx, dy)
        self.ear2Ex.move(dx, dy)
        self.ear2In.move(dx, dy)
    
    def sleep(self, win):
        """Allows the hare to sleep"""
        self.pupil1.undraw()
        self.eyeBall1.undraw()
        self.pupil2.undraw()
        self.eyeBall2.undraw()
        self.sleepEye1.draw(win)
        self.sleepEye2.draw(win)   
    
    def awake(self, win):
        """Allows the hare to wake up"""
        self.sleepEye1.undraw()
        self.sleepEye2.undraw()
        self.pupil1.draw(win)  
        self.eyeBall1.draw(win)  
        self.pupil2.draw(win)  
        self.eyeBall2.draw(win)  

    def setSurprised(self):
        """Switches the hare's expression to surprised"""
        self.mouthCover.undraw()
    
class HareRight(SpeechBubbleR):
    """A class for defining attributes of the hare facing right"""
    def __init__(self):
        """Initialize position of the hare body parts"""
        self.head = Circle(Point(625, 315), 38)
        self.head.setFill(color_rgb(224, 208, 200))

        self.body = Oval(Point(500, 312), Point(620, 394))
        self.body.setFill(color_rgb(224, 208, 200))

        self.pupil1 = Circle(Point(647, 307), 6)
        self.pupil1.setFill("black")

        self.eyeBall1 = Circle(Point(650, 305), 2)
        self.eyeBall1.setFill("white")

        self.pupil2 = Circle(Point(619, 307), 6)
        self.pupil2.setFill("black")

        self.eyeBall2 = Circle(Point(621, 305), 2)
        self.eyeBall2.setFill("white")

        self.mouthHappy = Oval(Point(640, 315), Point(613, 347))
        self.mouthHappy.setFill("black")

        self.mouthCover = Oval(Point(644, 315), Point(606, 329))
        self.mouthCover.setFill(color_rgb(224, 208, 200))
        self.mouthCover.setOutline(color_rgb(224, 208, 200))

        self.mouthSad = Line(Point(608, 330), Point(640, 330))

        self.ear1Ex = Oval(Point(655, 243), Point(635, 300))
        self.ear1Ex.setFill(color_rgb(224, 208, 200))

        self.ear1In = Oval(Point(649, 252), Point(641, 291))
        self.ear1In.setFill(color_rgb(255, 119, 255))

        self.ear2Ex = Oval(Point(613, 243), Point(593, 300))
        self.ear2Ex.setFill(color_rgb(224, 208, 200))

        self.ear2In = Oval(Point(607, 252), Point(599, 291))
        self.ear2In.setFill(color_rgb(255, 119, 255))

        self.hand = Circle(Point(627, 363), 12)
        self.hand.setFill(color_rgb(224, 208, 200))

        self.leg1 = Oval(Point(597, 375), Point(575, 408))
        self.leg1.setFill(color_rgb(224, 208, 200))

        self.leg2 = Oval(Point(567, 375), Point(545, 408))
        self.leg2.setFill(color_rgb(224, 208, 200))

        self.leg3 = Oval(Point(537, 375), Point(515, 408))
        self.leg3.setFill(color_rgb(224, 208, 200))

        self.tail = Circle(Point(493, 352), 14)
        self.tail.setFill(color_rgb(224, 208, 200))

    def draw(self, win):
        """Draws the hare on the graphics window"""
        self.tail.draw(win)
        self.leg1.draw(win)
        self.leg2.draw(win)
        self.leg3.draw(win) 
        self.ear1Ex.draw(win)
        self.ear1In.draw(win)
        self.ear2Ex.draw(win)
        self.ear2In.draw(win)
        self.body.draw(win)
        self.head.draw(win)
        self.pupil1.draw(win)
        self.eyeBall1.draw(win)
        self.pupil2.draw(win)
        self.eyeBall2.draw(win)
        self.mouthHappy.draw(win)
        self.mouthCover.draw(win)
        self.hand.draw(win)

    def undraw(self):
        """Undraws the hare on the graphics window"""
        self.tail.undraw()
        self.leg1.undraw()
        self.leg2.undraw()
        self.leg3.undraw()
        self.ear1Ex.undraw()
        self.ear1In.undraw()
        self.ear2Ex.undraw()
        self.ear2In.undraw()
        self.body.undraw()
        self.head.undraw()
        self.pupil1.undraw()
        self.eyeBall1.undraw()
        self.pupil2.undraw()
        self.eyeBall2.undraw()
        self.mouthHappy.undraw()
        self.mouthCover.undraw()
        self.hand.undraw()

    def move(self, dx, dy):
        """Moves the hare on the graphics window"""
        self.tail.move(dx, dy)
        self.hand.move(dx, dy)
        self.leg1.move(dx, dy)
        self.leg2.move(dx, dy)
        self.leg3.move(dx, dy)
        self.body.move(dx, dy)
        self.head.move(dx, dy)
        self.pupil1.move(dx, dy)
        self.eyeBall1.move(dx, dy)
        self.pupil2.move(dx, dy)
        self.eyeBall2.move(dx, dy)
        self.mouthHappy.move(dx, dy)
        self.mouthCover.move(dx, dy)
        self.mouthSad.move(dx, dy)
        self.ear1Ex.move(dx, dy)
        self.ear1In.move(dx, dy)
        self.ear2Ex.move(dx, dy)
        self.ear2In.move(dx, dy)
    
    def setHappy(self, win):
        """Switches the hare's expression to happy"""
        self.mouthCover.draw(win)

    def setSurprised(self):
        """Switches the hare's expression to surprised"""
        self.mouthCover.undraw()