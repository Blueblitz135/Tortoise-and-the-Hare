# Tree.py
# Aidan Leung
# 2022-05-24
# A module for the trees

from graphics import *

class Tree:
    """A class for defining tree attributes and functions for animation"""
    def __init__(self):
        """Initialize tree position"""
        self.treeBranch = Rectangle(Point(80, 285), Point(120, 400))
        self.treeBranch.setFill(color_rgb(77, 44, 44))

        self.leaf1 = Circle(Point(44, 205), 38)
        self.leaf1.setFill(color_rgb(39, 78, 19)) 
        self.leaf1.setOutline(color_rgb(39, 78, 19))

        self.leaf2 = Circle(Point(156, 205), 38)
        self.leaf2.setFill(color_rgb(39, 78, 19))
        self.leaf2.setOutline(color_rgb(39, 78, 19))

        self.leaf3 = Circle(Point(100, 205), 38)
        self.leaf3.setFill(color_rgb(39, 78, 19))
        self.leaf3.setOutline(color_rgb(39, 78, 19))

        self.leaf4 = Circle(Point(68, 264), 38)
        self.leaf4.setFill(color_rgb(39, 78, 19))
        self.leaf4.setOutline(color_rgb(39, 78, 19))

        self.leaf5 = Circle(Point(132, 264), 38)
        self.leaf5.setFill(color_rgb(39, 78, 19))
        self.leaf5.setOutline(color_rgb(39, 78, 19))

        self.leaf6 = Circle(Point(100, 155), 45)
        self.leaf6.setFill(color_rgb(39, 78, 19))
        self.leaf6.setOutline(color_rgb(39, 78, 19))

    def draw(self, win):
        """Draws the tree on the graphics window"""
        self.treeBranch.draw(win)
        self.leaf1.draw(win)
        self.leaf2.draw(win)
        self.leaf3.draw(win)
        self.leaf4.draw(win)
        self.leaf5.draw(win)
        self.leaf6.draw(win)

    def move(self, dx, dy):
        """Moves the tree on the grpahics window"""
        self.treeBranch.move(dx, dy)
        self.leaf1.move(dx, dy)
        self.leaf2.move(dx, dy)
        self.leaf3.move(dx, dy)
        self.leaf4.move(dx, dy)
        self.leaf5.move(dx, dy)
        self.leaf6.move(dx, dy)

    def duplicate(self, anchor, win):
        """Duplicates the tree on the graphics window"""
        dx = anchor.getX() - 100
        dy = anchor.getY() - 205

        treeBranchC = self.treeBranch.clone()
        leaf1C = self.leaf1.clone()
        leaf2C = self.leaf2.clone()
        leaf3C = self.leaf3.clone()
        leaf4C = self.leaf4.clone()
        leaf5C = self.leaf5.clone()
        leaf6C = self.leaf6.clone()

        treeBranchC.move(dx, dy)
        leaf1C.move(dx, dy)
        leaf2C.move(dx, dy)
        leaf3C.move(dx, dy)
        leaf4C.move(dx, dy)
        leaf5C.move(dx, dy)
        leaf6C.move(dx, dy)

        treeBranchC.draw(win)
        leaf1C.draw(win)
        leaf2C.draw(win)
        leaf3C.draw(win)
        leaf4C.draw(win)
        leaf5C.draw(win)
        leaf6C.draw(win)
    