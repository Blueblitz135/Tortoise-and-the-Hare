# SpeechBubble.py
# Aidan Leung
# 2022-05-30
# The module for speech bubbles. The speech bubbles classes are to be inherited 
# by the tortoise, hare, and bird

from graphics import *

class SpeechBubbleL:
    """A class for speech bubbles used by animals facing left"""
    def drawSpeech(self, anchor, text, textSize, win):
        """Draws a speech bubble on the graphics window"""
        self.anchor = anchor

        self.bubbleTop = Oval(Point(anchor.getX() - 63, anchor.getY() - 50), 
                         Point(anchor.getX() + 63, anchor.getY() + 50))
        self.bubbleTop.setFill("white")
        self.bubbleTop.setOutline("white")

        self.bubbleBot = Polygon(Point(anchor.getX() + 56, anchor.getY() + 20), 
                            Point(anchor.getX() + 43, anchor.getY() + 30), 
                            Point(anchor.getX() + 71, anchor.getY() + 35))
        self.bubbleBot.setFill("white")
        self.bubbleBot.setOutline("white")

        self.speech = Text(anchor, text)
        self.speech.setSize(textSize)

        self.bubbleBot.draw(win)
        self.bubbleTop.draw(win)
        self.speech.draw(win)
    
    def undrawSpeech(self):
        """Undraws a speech bubble on the graphics window"""
        self.bubbleBot.undraw()
        self.bubbleTop.undraw()
        self.speech.undraw()
    
    def changeSpeech(self, text, textSize, win):
        """Changes the text of a speech bubble"""
        self.speech.undraw()

        self.speech = Text(self.anchor, text)
        self.speech.setSize(textSize)

        self.speech.draw(win)

class SpeechBubbleR:
    """A class for speech bubbles used by animals facing right"""
    def drawSpeech(self, anchor, text, textSize, win):
        """Draws a speech bubble on the graphics window"""
        self.bubbleTop = Oval(Point(anchor.getX() - 63, anchor.getY() - 50), 
                         Point(anchor.getX() + 63, anchor.getY() + 50))
        self.bubbleTop.setFill("white")
        self.bubbleTop.setOutline("white")

        self.bubbleBot = Polygon(Point(anchor.getX() - 56, anchor.getY() + 20), 
                            Point(anchor.getX() - 43, anchor.getY() + 30), 
                            Point(anchor.getX() - 71, anchor.getY() + 35))
        self.bubbleBot.setFill("white")
        self.bubbleBot.setOutline("white")

        self.speech = Text(anchor, text)
        self.speech.setSize(textSize)

        self.bubbleBot.draw(win)
        self.bubbleTop.draw(win)
        self.speech.draw(win)
    
    def undrawSpeech(self):
        """Undraws a speech bubble on the graphics window"""
        self.bubbleBot.undraw()
        self.bubbleTop.undraw()
        self.speech.undraw()
    
    def changeSpeech(self, text, textSize, win):
        """Changes the text of a speech bubble"""
        self.speech.undraw()
        self.speech = Text(self.bubbleTop.getCenter(), text)
        self.speech.setSize(textSize)

        self.speech.draw(win)
    
    def moveSpeech(self, dx, dy):
        """Moves a speech bubble on the graphics window"""
        self.speech.move(dx, dy)
        self.bubbleBot.move(dx, dy)
        self.bubbleTop.move(dx, dy)