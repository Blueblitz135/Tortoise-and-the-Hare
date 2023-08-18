# StoryAnimation.py
# 2022-06-04
# This is an Animation of the story "The Tortoise and The Hare"

# Import libraries 
from graphics import *
from Tortoise import *
from Hare import *
from Tree import *
from Bird import *
from Story import *
import random
import os

# Initialize objects
tortoise = Tortoise()
hareR = HareRight()
hareL = HareLeft()
bird = Bird()
tree = Tree()
storyLine = Story("base") # Initial story lines are same for hare and tortoise

#-----------------------------------Frame 1-----------------------------------
# Set windows and background colour
WIDTH = 960
HEIGHT = 540

win1 = GraphWin("Frame 1", WIDTH, HEIGHT)
win1.setBackground(color_rgb(190, 214, 235))

# Set background
win1.setBackground(color_rgb(190, 214, 235))

# Draw trees in the background
tree.draw(win1)
dx = 0  # Counter used to determine how far apart the trees are
for i in range(7):
    # Duplicate to draw trees in the background
    dx += 110
    tree.duplicate(Point(100 + dx, 205), win1)

ground = Rectangle(Point(-1, 390), Point(960, 540))
ground.setFill(color_rgb(231, 164, 76))
ground.draw(win1)

# Set and draw turtle position
tortoise.move(-635, 189)
tortoise.draw(win1)

# Set and draw hare position
hareL.move(503, 116)
hareL.draw(win1)

## Animation: The tortoise and hare are introduced and the tortoise challenges
# the hare to a race
storyLine.drawNext(Point(480, 48), 20, win1)
time.sleep(3)

# Tortoise comes in 
tortoise.move(15, 0)
time.sleep(0.1)

# Next story line
storyLine.undraw()
storyLine.drawNext(Point(480, 48), 20, win1)

for i in range(9):
    # Tortoise continues walking
    tortoise.move(15, 0)
    time.sleep(0.7)

# Next story line
storyLine.undraw()
storyLine.drawNext(Point(480, 48), 20, win1)

for i in range(8):
    # Tortoise continues walking
    tortoise.move(15, 0)
    time.sleep(0.7)

for i in range(7):
    # Hare comes in
    hareL.move(-20, -8)
    time.sleep(0.1)
    hareL.move(-20, 8)
    time.sleep(0.1)

storyLine.undraw()

# Hare speaks
hareL.drawSpeech(Point(610, 357), "Ha! You're so\nslow!", 12, win1)
time.sleep(2)
hareL.changeSpeech("Do you ever get\nanywhere?", 12, win1)
time.sleep(2)
hareL.undrawSpeech()

# Tortoise responds
tortoise.drawSpeech(Point(336, 415), "Yes, I do", 12, win1)
time.sleep(2)
tortoise.changeSpeech("To prove it,\ndo you want to\nrace?", 12, win1)
time.sleep(2)

# Prompt user to continue
storyLine.drawNext(Point(480, 48), 20, win1)

# Transitions to next frame when user clicks anywhere on the screen
win1.getMouse()
win1.close()

#-----------------------------------Frame 2-----------------------------------
# Reset position of objects
tortoise = Tortoise()
hareR = HareRight()
hareL = HareLeft()

# Set windows and background colour
WIDTH = 960
HEIGHT = 540

win2 = GraphWin("Frame 2", WIDTH, HEIGHT)
win2.setBackground("black")

# Initiliaze variables
tortoiseText = Text(Point(230, 410), "Tortoise")
tortoiseText.setFill("white")
tortoiseText.setSize(20)

hareText = Text(Point(665, 410), "Hare")
hareText.setFill("white")
hareText.setSize(20)

selectionPrompt1 = Text(Point(480, 80), 
                        "Select which animal you want to race with:")
selectionPrompt1.setOutline("white")
selectionPrompt1.setSize(16)

selectionPrompt2 = Text(Point(480, 140), 
                        "Enter 'tortoise' or 'hare' and press 'enter'")
selectionPrompt2.setOutline("white")

controlText = Text(Point(209, 501), "Control for race: Press 'd' to move forward")
controlText.setFill("white")

infoText = Text(Point(735, 501), "Play with both animals to experience the full story!")
infoText.setFill("white")

inputBox = Entry(Point(480, 115), 20)

userSelection = ""

# Draw Tortoise and text
tortoise.move(-250, 40)
tortoise.draw(win2)
tortoiseText.draw(win2)

# Draw Hare and text
hareR.move(100, -20)
hareR.draw(win2)
hareText.draw(win2)

# Draw text prompts
selectionPrompt1.draw(win2)
selectionPrompt2.draw(win2)
controlText.draw(win2)
infoText.draw(win2)

# Draw entry box for user input
inputBox.draw(win2)

while True:
    # Prompt user to select an animal
    # Loop runs until user enters a valid input
    keyCheck = win2.getKey()

    if keyCheck == "Return":
        # If user presses enter key, the program will get the text 
        # and make sure it is lowercase
        userSelection = inputBox.getText().lower()

    if userSelection == "tortoise":
        # If user enters "tortoise", it will wink a speech bubble will appear
        tortoise.wink(win2)
        tortoise.drawSpeech(Point(466, 270), 
                            "Slow and steady\nwins the race!", 12, win2)
        break
    elif userSelection == "hare":
        # If user enters "hare", a speech bubble will appear
        hareR.drawSpeech(Point(849, 270), "I'm definetly\ngoing to win!",
                         12, win2)
        break

# Wait 3 seconds, then close window
time.sleep(3)
win2.close()


#-----------------------------------Frame 3-----------------------------------
# Initialize animal positions
tortoise = Tortoise()
hareR = HareRight()
bird = Bird()

# Set windows and background color
WIDTH = 960
HEIGHT = 540

win3 = GraphWin("Frame 3", WIDTH, HEIGHT)
win3.setBackground(color_rgb(190, 214, 235))

# Initialize variables 
ground = Rectangle(Point(-1, 345), Point(961, 541))
ground.setFill(color_rgb(231, 164, 76))

grass = Rectangle(Point(-1, 194), Point(961, 345))
grass.setFill(color_rgb(56, 118, 29))

startLine = Line(Point(295, 345), Point(295, 541))
startLine.setOutline(color_rgb(217, 217, 217))
startLine.setWidth(15)

# Image: (Nicepng, n.d.)
# Use of os: (nkmk, 2021)
bleachers1 = Image(Point(250, 210), 
                   os.path.dirname(os.path.abspath(__file__)) 
                   + "\Bleachers.png")

# Image: (Nicepng, n.d.)
# Use of os: (nkmk, 2021)
bleachers2 = Image(Point(710, 210), 
                   os.path.dirname(os.path.abspath(__file__)) 
                   + "\Bleachers.png")

# Image: (Equity, n.d.)
# Use of os: (nkmk, 2021)
cow = Image(Point(630, 160),
            os.path.dirname(os.path.abspath(__file__)) + "\Cow.png")

# Image: (Equity, n.d.)
# Use of os: (nkmk, 2021)
horse = Image(Point(218, 193), os.path.dirname(os.path.abspath(__file__))
              + "\Horse.png")

# Image: (Equity, n.d.)
# Use of os: (nkmk, 2021)
sheep = Image(Point(792, 210), os.path.dirname(os.path.abspath(__file__)) 
              + "\Sheep.png")

# Draw background
ground.draw(win3)
grass.draw(win3)
startLine.draw(win3)
bleachers1.draw(win3)
bleachers2.draw(win3)

# Draw animals
cow.draw(win3)
horse.draw(win3)
sheep.draw(win3)

bird.move(0, -60)
bird.draw(win3)

hareR.move(-430, 40)
hareR.draw(win3)

tortoise.move(-355, 200)
tortoise.draw(win3)

## Animation: The tortoise and the hare begin the race
storyLine.drawNext(Point(480, 36), 20, win3)
time.sleep(2)
storyLine.undraw()

# Bird announces the race
bird.drawSpeech(Point(375, 250), "Get ready for\nthe race!", 14, win3)
time.sleep(2)
bird.undrawSpeech()

# Tortoise and hare have a quick conversation before the race
tortoise.drawSpeech(Point(356, 444), "Good luck!", 14, win3)
time.sleep(1.5)
tortoise.undrawSpeech()

hareR.drawSpeech(Point(320, 312), "Ha! Won't\nneed it!", 14, win3)
time.sleep(2)
hareR.undrawSpeech()

# Race is about to start
bird.drawSpeech(Point(375, 250), "Ready,", 20, win3)
time.sleep(2)
bird.changeSpeech("Set,", 18, win3)
time.sleep(2)
bird.changeSpeech("Go!", 18, win3)

if userSelection == "hare":
    # This block of code excecutes if user selceted to race as hare
    # Initialize counters/accumulators
    stepCount = 0
    hareMoveControl = 0
    tortoiseMoveControl = 0
    audienceCheerControl = 0
    birdSpeechUndrawCheck = 1

    # Draw prompt for user to move hare
    storyLine.drawNext(Point(672, 390), 18, win3)

    while stepCount < 23:
        # Loop for user to move hare to the end of the screen
        # Checks for user input
        moveCheck = win3.checkKey()

        if stepCount == 7:
            # Undraw prompt after user moves hare a few times
            storyLine.undraw()

        if hareMoveControl == 1000:
            # Allow user to move the hare
            # The control limits how fast the user is able to move the hare
            if moveCheck == "d":
                hareR.move(20, -8)
                time.sleep(0.05)
                hareR.move(20, 8)
                stepCount += 1
                hareMoveControl = 0
        else:
            hareMoveControl += 1

        if tortoiseMoveControl == 5000:
            # The tortoise will automatically move
            # The control helps determine how fast it moves
            tortoise.move(8, 0)
            tortoiseMoveControl = 0

        if birdSpeechUndrawCheck > 0 and birdSpeechUndrawCheck < 30000:
            # This is a one time conditional statement that undraws the bird's 
            # speech bubble after a short time, timed by an accumulator
            birdSpeechUndrawCheck += 1
        elif birdSpeechUndrawCheck == 30000:
            bird.undrawSpeech()
            birdSpeechUndrawCheck = -1

        if audienceCheerControl == 8000:
            # Allows the animals in the background move up and down in a 
            # constant rhythm, timed by an accumulator
            cow.move(0, -10)
            horse.move(0, -10)
            sheep.move(0, -10)
        elif audienceCheerControl == 16000:
            cow.move(0, 10)
            horse.move(0, 10)
            sheep.move(0, 10)
            audienceCheerControl = 0
        
        tortoiseMoveControl += 1
        audienceCheerControl += 1

else:
    # This block of code excecutes if user selceted to race as hare
    # Initialize counters/accumulators
    stepCount = 0
    tortoiseMoveControl = 0
    hareMoveControl = 0
    audienceCheerControl = 0
    birdSpeechUndrawCheck = 1

    # Draw prompt for user to move tortoise
    storyLine.drawNext(Point(672, 494), 18, win3)

    while stepCount < 96:
        # Loop for user to move hare to the end of the screen
        # Check for user input
        moveCheck = win3.checkKey()

        if stepCount == 8:
            # Undraw prompt after user moves the tortoise a few times
            storyLine.undraw()

        # Allow user to move tortoise
        # The counter helps limit how fast the user is able to move the 
        # tortoise
        if tortoiseMoveControl == 2200: 
            # Allow user to move the tortoise
            # The control limits how fast the user can move the tortoise
            if moveCheck == "d":
                tortoise.move(10, 0)
                stepCount += 1
                tortoiseMoveControl = 0
        else:
            tortoiseMoveControl += 1

        if hareMoveControl == 1100:
            # The hare will automatically move
            # The control helps determine how fast it moves
            hareR.move(13, -8)
        elif hareMoveControl == 2200:
            hareR.move(13, 8)
            hareMoveControl = 0    

        if birdSpeechUndrawCheck > 0 and birdSpeechUndrawCheck < 30000:
            # This is a one time conditional statement that undraws the bird's 
            # speech bubble after a short time, timed by an accumulator
            birdSpeechUndrawCheck += 1
        elif birdSpeechUndrawCheck == 30000:
            bird.undrawSpeech()
            birdSpeechUndrawCheck = -1
        
        if audienceCheerControl == 8000:
            # Allows the animals in the background move up and down in a 
            # constant rhythm, timed by an accumulator
            cow.move(0, -10)
            horse.move(0, -10)
            sheep.move(0, -10)
        elif audienceCheerControl == 16000:
            cow.move(0, 10)
            horse.move(0, 10)
            sheep.move(0, 10)
            audienceCheerControl = 0
        
        hareMoveControl += 1
        audienceCheerControl += 1

# Close window as soon as the tortoise reaches the end of the screen
win3.close()


#-----------------------------------Frame 4-----------------------------------
# Initialize animals and tree position
tortoise = Tortoise()
hareR = HareRight()
hareL = HareLeft()
tree = Tree()

# Set windows and background colour
WIDTH = 960
HEIGHT = 540

win4 = GraphWin("Frame 4", WIDTH, HEIGHT)
win4.setBackground(color_rgb(190, 214, 235))

# Initiliaze variables
grass = Rectangle(Point(-1, 240), Point(961, 360))
grass.setFill(color_rgb(56, 118, 29))

ground = Rectangle(Point(-1, 360), Point(961, 541))
ground.setFill(color_rgb(231, 164, 76))

# Image: (Equity, n.d.)
# Use of os: (nkmk, 2021)
pig = Image(Point(225, 287), 
            os.path.dirname(os.path.abspath(__file__)) + "\Pig.png")

bubbleTopPig = Oval(Point(313, 165), Point(440, 265))
bubbleTopPig.setFill("white")
bubbleTopPig.setOutline("white")

bubbleBotPig = Polygon(Point(321, 234), Point(326, 243), Point(298, 243))
bubbleBotPig.setFill("white")
bubbleBotPig.setOutline("white")

speechPig1 = Text(Point(376.5, 215), f"Go, {userSelection},\ngo!!")
speechPig1.setSize(16)

speechPig2 = Text(Point(376.5, 215), "Good luck!!")
speechPig2.setSize(16)

# Set background
ground.draw(win4)
grass.draw(win4)
tree.move(-120, -130)

dx = 0 # Counter used to determine how far apart the trees are
for i in range(8):
    # Draw trees in background
    dx += 110
    tree.duplicate(Point(100 + dx, 205), win4)

# Initialize tortoise and hare position
tortoise.move(-636, 189)
hareR.move(-664, 110)
hareL.move(-10, 110)

# Draw animals
pig.draw(win4)
tortoise.draw(win4)
hareR.draw(win4)

## Animation: Depending on user selection, the tortoise or the hare meets
## and talks to the pig 
if userSelection == "hare":
    # This block of code excecutes if user selceted to race as hare
    storyLine.drawNext(Point(625, 450), 20, win4)

    stepCount = 0
    while stepCount < 15:
        # Allow for user to move the hare
        keyCheck = win4.getKey()
        if keyCheck == "d":
            hareR.move(20, -8)
            time.sleep(0.05)
            hareR.move(20, 8)
            stepCount += 1
        
        if stepCount == 4:
            # Undraws prompt after the hare moves a bit
            storyLine.undraw()
    time.sleep(1)

    # Hare turns around to speak to pig
    hareR.undraw()
    hareL.draw(win4)

    # Pig speaks 
    bubbleTopPig.draw(win4)
    bubbleBotPig.draw(win4)
    speechPig1.draw(win4)
    time.sleep(2)
    bubbleTopPig.undraw()
    bubbleBotPig.undraw()
    speechPig1.undraw()

    # Hare speaks
    hareL.drawSpeech(Point(358, 370), "I'm too fast!\nThis is too easy!", 13, win4)
    time.sleep(2)
    hareL.changeSpeech("Look at me!", 14, win4)
    time.sleep(1.5)
    hareL.undrawSpeech()

    # Hare jumps around
    for i in range(3):
        hareL.move(-30, -18)
        hareR.move(-30, 0)
        time.sleep(0.1)
        hareL.move(-30, 18)
        hareR.move(-30, 0)
        time.sleep(0.1)

    time.sleep(1)
    hareL.undraw()
    hareR.draw(win4)
    time.sleep(0.2)
    
    for i in range(3):
        hareR.move(30, -18)
        hareL.move(30, 0)
        time.sleep(0.1)
        hareR.move(30, 18)
        hareL.move(30, 0)
        time.sleep(0.1)

    time.sleep(1)
    hareR.undraw()
    hareL.draw(win4)

    # Hare Speaks again
    hareL.drawSpeech(Point(358, 370), 
                     "The tortoise will\nnever catch up!", 13, win4)
    time.sleep(2)
    hareL.undrawSpeech()

    # Pig says good luck
    bubbleTopPig.draw(win4)
    bubbleBotPig.draw(win4)
    speechPig2.draw(win4)
    time.sleep(2)
    bubbleTopPig.undraw()
    bubbleBotPig.undraw()
    speechPig2.undraw()

    # Hare turns around and user takes control again
    hareL.undraw()
    hareR.draw(win4)

    # Prompt user to move the hare
    storyLine.drawNext(Point(800, 450), 20, win4)

    stepCount = 0
    while stepCount < 14:
        # Allows user to move hare
        keyCheck = win4.getKey()
        if keyCheck == "d":
            hareR.move(20, -8)
            time.sleep(0.05)
            hareR.move(20, 8)
            stepCount += 1

        if stepCount == 3:
            # Undraws prompt after a while
            storyLine.undraw()

else:
    # This block of code excecutes if user selceted to race as tortoise
    storyLine.drawNext(Point(625, 450), 20, win4)

    stepCount = 0
    while stepCount < 12:
    # Allow for user to move the tortoise
        keyCheck = win4.getKey()
        if keyCheck == "d":
            tortoise.move(20, 0)
            time.sleep(0.4)
            stepCount += 1

        if stepCount == 4:
            # Undraws prompt after the tortoise moves a bit
            storyLine.undraw()
    time.sleep(1)

    # Pig speaks 
    bubbleTopPig.draw(win4)
    bubbleBotPig.draw(win4)
    speechPig1.draw(win4)
    
    for i in range(3):
        # Tortoise moves while pig is speaking
        tortoise.move(20, 0)
        time.sleep(0.4)
    bubbleTopPig.undraw()
    bubbleBotPig.undraw()
    speechPig1.undraw()

    # Tortoise speaks and runs at the same time
    tortoise.drawSpeech(Point(358, 410), "Thank you!", 13, win4)
    for i in range(3):
        # Tortoise runs
        tortoise.move(20, 0)
        tortoise.moveSpeech(20, 0)
        time.sleep(0.5)
    tortoise.changeSpeech("I'll get\nthere soon!", 14, win4)
    for i in range(3):
        # Tortoise continues to run
        tortoise.move(20, 0)
        tortoise.moveSpeech(20, 0)
        time.sleep(0.5)
    tortoise.undrawSpeech()

    # Pig says good luck
    bubbleTopPig.draw(win4)
    bubbleBotPig.draw(win4)
    speechPig2.draw(win4)
    for i in range(3):
        # Tortoise continues to run
        tortoise.move(20, 0)
        time.sleep(0.5)
    bubbleTopPig.undraw()
    bubbleBotPig.undraw()
    speechPig2.undraw()

    # User is able to take control of moving the tortoise again
    # Prompt user to move the tortoise
    storyLine.drawNext(Point(625, 450), 20, win4)

    stepCount = 0
    while stepCount < 26:
        # Allows user to move the tortoise
        keyCheck = win4.getKey()
        if keyCheck == "d":
            tortoise.move(20, 0)
            time.sleep(0.4)
            stepCount += 1
        
        if stepCount == 4:
            # Undraws prompt after a while
            storyLine.undraw()

# Close window as soon as the tortoise reaches the end of the screen
win4.close()

#-----------------------------------Frame 5-----------------------------------
# Initialize positions of animals and tree
tortoise = Tortoise()
hareR = HareRight()
hareL = HareLeft()
tree = Tree()

# Set windows and background color
WIDTH = 960
HEIGHT = 540

win5 = GraphWin("Frame 4", WIDTH, HEIGHT)
win5.setBackground(color_rgb(242, 91, 36))

# Initiliaze variables
grass = Rectangle(Point(-1, 150), Point(961, 360))
grass.setFill(color_rgb(56, 118, 29))

ground = Rectangle(Point(-1, 360), Point(961, 541))
ground.setFill(color_rgb(231, 164, 76))

blackScreen = Rectangle(Point(0, 0), Point(960, 540))
blackScreen.setFill("black")

blackScreenText = Text(Point(480, 270), "A long while after...")
blackScreenText.setSize(30)
blackScreenText.setFill("White")

# Set tortoise and hare positions
tortoise.move(-615, 189)
hareR.move(-664, 110)
hareL.move(228, -141)

# Draw background
grass.draw(win5)
ground.draw(win5)
tree.move(-170, -200)

dx = 0 # Counter used to determine how far apart the trees are
for i in range(9):
    # Draw trees in background
    dx += 110
    tree.duplicate(Point(100 + dx, 205), win5)

if userSelection == "hare":
    # Loop excecutes if user selection is hare
    hareR.draw(win5)
    storyLine.drawNext(Point(319, 276), 20, win5)
    for i in range(8):
        # Hare moves forward for a bit
        hareR.move(20, -8)
        time.sleep(0.18)
        hareR.move(20, 8)
        time.sleep(0.18)
    storyLine.undraw()

    storyLine = Story("hare")  # Diverge story line for hare

    storyLine.drawNext(Point(480, 276), 20, win5)
    for i in range(6):
        # Hare continues forward
        hareR.move(20, -8)
        time.sleep(0.18)
        hareR.move(20, 8)
        time.sleep(0.18)
    storyLine.undraw()

    # The Hare gets bored and decides to take a nap near the trees
    hareR.drawSpeech(Point(638, 384), "*Sigh*", 14, win5)
    time.sleep(1.5)

    hareR.changeSpeech("This is\nso boring", 14, win5)
    time.sleep(2)

    hareR.changeSpeech("The tortoise will\nnever catch up!", 13, win5)
    time.sleep(2)

    hareR.changeSpeech("I'm just going\nto take a nap", 14, win5)
    time.sleep(2)
    hareR.undrawSpeech()

    for i in range(11):
        # Hare moves over to the trees 
        hareR.move(30, -30)
        time.sleep(0.1)
        hareR.move(0, 7)
        time.sleep(0.1)
    time.sleep(1)

    # Hare turns around and sleeps
    hareR.undraw()
    hareL.draw(win5)
    time.sleep(1)

    hareL.sleep(win5)
    hareL.drawSpeech(Point(602, 123), "Z", 14, win5)
    time.sleep(1)
    hareL.changeSpeech("Zz", 14, win5)
    time.sleep(1)
    hareL.changeSpeech("Zzz", 14, win5)
    time.sleep(1)

    # Draw black screen with text
    blackScreen.draw(win5)
    blackScreenText.draw(win5)
    time.sleep(5)
    blackScreenText.undraw()
    blackScreen.undraw()

    # Back to the story scene and set background as night time
    win5.setBackground(color_rgb(11, 84, 148))

    # Hare wakes up 
    time.sleep(1)
    hareL.awake(win5)
    hareL.undrawSpeech()
    time.sleep(1.5)

    # Hare is surprised he slept for so long and tries to catch up
    hareL.setSurprised()
    hareL.drawSpeech(Point(602, 123), 
                     "Oh no! I slept\nfor too long!", 14, win5)
    time.sleep(2)
    hareL.changeSpeech("Can I still\nmake it?", 14, win5)
    time.sleep(2)

    hareL.undrawSpeech()
    hareL.undraw()
    hareR.draw(win5)
    hareR.setSurprised()

    # Hare hurries to finish the race
    for i in range(11):
        hareR.move(30, 30)
        time.sleep(0.1)
        hareR.move(0, -7)
        time.sleep(0.1)

else:
    # Loop excutes if user selection is tortoise
    tortoise.draw(win5)

    # Draw hare sleeping near the trees
    hareL.draw(win5)
    hareL.sleep(win5)
    hareL.drawSpeech(Point(602, 123), "Zzz", 14, win5)
    
    storyLine.drawNext(Point(319, 276), 20, win5)
    for i in range(6):
        # Tortoise continues moving foward
        tortoise.move(20, 0)
        time.sleep(0.6)
    storyLine.undraw()

    storyLine = Story("tortoise") # Diverge story line for tortoise

    storyLine.drawNext(Point(319, 276), 20, win5)
    # Tortoise continues moving forward
    for i in range(6):
        tortoise.move(20, 0)
        time.sleep(0.6)
    storyLine.undraw()

    # The tortoise is surprised to see the hare sleeping and takes advantage 
    # of the opportunity
    tortoise.setSurprisedFace(win5)
    tortoise.drawSpeech(Point(337, 425), "*Gasps*", 14, win5)
    time.sleep(1.5)
    tortoise.changeSpeech("The hare\nis asleep!", 14, win5)
    time.sleep(2)

    tortoise.setHappyFace(win5)
    tortoise.changeSpeech("This is my\nchance to win!", 14, win5)
    for i in range(5):
        # # Tortoise continues movgin forward
        tortoise.move(20, 0)
        tortoise.moveSpeech(20, 0)
        time.sleep(0.6)
    tortoise.undrawSpeech()

    # Draw prompt for user to move the tortoise
    storyLine.drawNext(Point(680, 452), 18, win5)

    stepCount = 0
    tortoiseMoveControl = 0
    while stepCount < 86:
        # Allows user to take control of tortoise again
        # Checks for user input from keyboard
        moveCheck = win5.checkKey()

        if stepCount == 8:
            # Undraws prompt after a while
            storyLine.undraw()

        if tortoiseMoveControl == 2000: 
            # Regulates how fast the user can move the tortoise
            if moveCheck == "d":
                # Checks for correct input
                tortoise.move(10, 0)
                stepCount += 1
                tortoiseMoveControl = 0
        else:
            tortoiseMoveControl += 1

# Close window as soon as the tortoise reaches the end of the screen
win5.close()

#---------------------------------Final Frame---------------------------------
# Initialize animal positions
tortoise = Tortoise()
hareR = HareRight()
bird = Bird()

# Set windows and background colour
WIDTH = 960
HEIGHT = 540

winF = GraphWin("Final Frame", WIDTH, HEIGHT)
winF.setBackground(color_rgb(11, 84, 148))

# Initialize objects
grass = Rectangle(Point(-1, 250), Point(961, 360))
grass.setFill(color_rgb(56, 118, 29))

ground = Rectangle(Point(-1, 360), Point(961, 540))
ground.setFill(color_rgb(231, 164, 76))

finishLine = Line(Point(480, 358), Point(548, 540))
finishLine.setOutline("white")
finishLine.setWidth(15)

tortoiseMovePrompt = Text(Point(378, 298), 
                          "Press 'd' to move and finish the race!")
tortoiseMovePrompt.setSize(18)

# Image: (Equity, n.d.)
# Use of os: (nkmk, 2021)
cow = Image(Point(328, 280),
            os.path.dirname(os.path.abspath(__file__)) + "\Cow.png")

# Image: (Equity, n.d.)
# Use of os: (nkmk, 2021)
horse = Image(Point(134, 280), os.path.dirname(os.path.abspath(__file__)) 
              + "\Horse.png")

# Image: (Equity, n.d.)
# Use of os: (nkmk, 2021)
sheep = Image(Point(540, 280), os.path.dirname(os.path.abspath(__file__)) 
              + "\Sheep.png")

bubbleTopHorse = Oval(Point(373, 131), Point(501, 231))
bubbleTopHorse.setFill("white")
bubbleTopHorse.setOutline("white")

bubbleBotHorse = Polygon(Point(381, 200), Point(390, 210), Point(352, 214))
bubbleBotHorse.setFill("white")
bubbleBotHorse.setOutline("white")

speechHorse1 = Text(Point(437, 181), "Go, Tortoise!")
speechHorse1.setSize(16)

speechHorse2 = Text(Point(437, 181), "Whoo!")
speechHorse2.setSize(16)

# Set background
ground.draw(winF)
finishLine.draw(winF)
grass.draw(winF)
for i in range(400):
    # Generate stars
    winF.plotPixel(random.randint(0, WIDTH), 
    random.randint(0, 250), "white")


# Set animal positions 
tortoise.move(-600, 189)
bird.move(303, -50)
hareR.move(-664, 110)

# Draw bird
bird.draw(winF)

## Animation: The race ends and the tortoise wins
## The animation for the hare is shorter as he misses out the ending because he
## slept too long
if userSelection == "hare":
    # Set tortoise position
    tortoise.move(760, 0)

    # Draw animals
    hareR.draw(winF)
    tortoise.draw(winF)
    cow.draw(winF)
    horse.draw(winF)
    sheep.draw(winF)

else:
    # Animation executes if the user chose to race as tortoise
    # Draw animals
    hareR.draw(winF)
    tortoise.draw(winF)
    cow.draw(winF)
    horse.draw(winF)
    sheep.draw(winF)

    # Horse cheers for the tortoise
    bubbleTopHorse.draw(winF)
    bubbleBotHorse.draw(winF)
    speechHorse1.draw(winF)

    # Tortoise comes in 
    for i in range(7):
        tortoise.move(20, 0)
        time.sleep(0.5)

    bubbleTopHorse.undraw()
    bubbleBotHorse.undraw()
    speechHorse1.undraw()

    # Bird also cheers for tortoise
    bird.drawSpeech(Point(680, 254), "You're almost\nthere!", 14, winF)
    time.sleep(2)
    
    # Draw prompt for moving tortoise
    storyLine.drawNext(Point(746, 452), 24, winF)

    stepCount = 0
    tortoiseMoveControl = 0
    hareMoveControl = 0
    audienceCheerControl = 0
    birdSpeechUndrawCheck = 1
    while stepCount < 62:
        # Allows user to take control of tortoise again
        # Check for user input
        moveCheck = winF.checkKey()

        if stepCount == 8:
            # Undraws prompt after a while
            storyLine.undraw()

        if tortoiseMoveControl == 2200: 
            # Allow user to move tortoise
            # The counter helps limit how fast the user is able to move the 
            # tortoise`
            if moveCheck == "d":
                tortoise.move(10, 0)
                stepCount += 1
                tortoiseMoveControl = 0
        else:
            tortoiseMoveControl += 1
        
        if audienceCheerControl == 8000:
            # A conditional statement that determines when the animals in the
            # background move up and down
            cow.move(0, -10)
            horse.move(0, -10)
            sheep.move(0, -10)
        elif audienceCheerControl == 16000:
            cow.move(0, 10)
            horse.move(0, 10)
            sheep.move(0, 10)
            audienceCheerControl = 0

        audienceCheerControl += 1
    
    # Undraw bird speech
    bird.undrawSpeech()

## Ending scene excecutes the same for both the hare and the tortoise paths
# Bird announces winner
bird.drawSpeech(Point(680, 254), "We have a\nwinner!!", 14, winF)
time.sleep(3)
bird.undrawSpeech()

# The tortoise is happy that he won, jumping up and down
tortoise.drawSpeech(Point(875, 412), "Yay!\nI win!", 16, winF)
for i in range(3):
    # Tortoise jumps up and down
    tortoise.move(0, -10)
    time.sleep(0.7)
    tortoise.move(0, 10)
    time.sleep(0.7)
tortoise.undrawSpeech()

storyLine.drawNext(Point(340, 441), 18, winF)
time.sleep(1.5)

# The hare finally arrives, but it's too late
for i in range(5):
    hareR.move(20, -8)
    time.sleep(0.18)
    hareR.move(20, 8)
    time.sleep(0.18)
storyLine.undraw()
hareR.setSurprised()
time.sleep(2)

# All the animals leave to celebrate for the tortoise
for i in range(10):
    # Animals move towards the tortoise
    cow.move(30, 20)
    horse.move(30, 20)
    sheep.move(30, 20)
    time.sleep(0.2)
time.sleep(1)

# The animals lift the tortoise up
for i in range(2):
    # Animals gather to lift the tortoise
    horse.move(40, 0)
    sheep.move(-40, 0)
    time.sleep(1)
time.sleep(1)
tortoise.move(0, -100)
time.sleep(1)

# The animals leave the hare alone
for i in range(9):
    tortoise.move(65, 0)
    horse.move(65, 0)
    sheep.move(65, 0)
    cow.move(65, 0)
    bird.move(65, 0)
    time.sleep(1)

# The hare moves to the middle of the screen
for i in range(8):
    hareR.move(20, -8)
    time.sleep(0.18)
    hareR.move(20, 8)
    time.sleep(0.18)
time.sleep(1)

# Hare gives moral of the story to end off the animation
hareR.setHappy(winF)
hareR.drawSpeech(Point(596, 376), "Welp, I admit\ndefeat", 14, winF)
time.sleep(3)

hareR.changeSpeech("I should have\nbeen humble", 12, winF)
time.sleep(3)

hareR.changeSpeech("I guess the\ntortoise was right", 12, winF)
time.sleep(3)

hareR.changeSpeech("Slow and steady\nwins the race!", 12, winF)
time.sleep(3)

hareR.changeSpeech("I hope you\nlearned a lesson", 12, winF)
time.sleep(2)

hareR.changeSpeech("from this story!", 12, winF)
time.sleep(3)

hareR.changeSpeech("Bye!", 16, winF)
time.sleep(3)

# Close window and end animation
winF.close()
