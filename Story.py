# StoryLines.py
# Aidan Leung
# 2022-05-28
# The module for the storyline

from graphics import *

class Story:
    """This class contains the storyline of the animation"""
    def __init__(self, animal):
        """Initialize the set of story lines and line number"""
        self.animal = animal
        self.lineNum = -1
    
    # Store storyline that is used for both the hare and tortoise animations
    linesBase = [
    "This is the story of the tortoise and the hare...", 
    "Once upon a time, a tortoise was minding his own business", 
    "when suddenly, he was interrupted by a hare...", 
    "Tap anywhere on the screen to continue", 
    "The tortoise and the hare are at the starting line...",
    "Tap 'd' repeatedly to move forward!", 
    "Keep going!",
    "Continue!",
    "It's starting to get late in the day..."]  

    # Store storyline that is only used for the tortoise animation
    linesTortoise = [
    "the tortoise is nearing the end of the race...",
    "Almost there! Continue moving forward!", 
    "finish the race!", 
    "The hare showed up,\nbut it was too late..."]
    
    # Store storyline that is only used for the hare animation
    linesHare = [  
    "the hare is almost finished the race...",
    "The hare showed up,\nbut it was too late..."]

    # This function draws the proceeding storyline at a given point
    # The size of the text is manually set
    # The line number is automatically accumulated everytime
    def drawNext(self, anchor, size, win):
        """This function draws the proceeding story line at a given point;
        the size of the text is manually set;
        the line number is automatically accumulated everytime
        """
        self.lineNum += 1

        # Determines which set of story lines to use
        if self.animal == "base":
            self.line = Text(anchor, self.linesBase[self.lineNum])
        elif self.animal == "tortoise":
            self.line = Text(anchor, self.linesTortoise[self.lineNum])
        elif self.animal == "hare":
            self.line = Text(anchor, self.linesHare[self.lineNum])

        self.line.setSize(size)
        self.line.draw(win)
        

    def undraw(self):
        """Undraws current story line"""
        self.line.undraw()