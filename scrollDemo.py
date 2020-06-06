from pygame_functions import *

screenSize(600, 600)
setAutoUpdate(False)

setBackgroundImage("dungeonFloor.png")

testSprite = makeSprite("Main_Character_Front.png")
addSpriteImage(testSprite, "Main_Character_Left.png")
addSpriteImage(testSprite, "Main_Character_Right.png")

lander = makeSprite("landerCrash.png")

found = False

xPos = 900
yPos = 300
xSpeed = 0
ySpeed = 0

moveSprite(testSprite, 300, 300, True)

showSprite(testSprite)

nextFrame = clock()

game_over = makeLabel("You did it!", 150, 35, 200, "black", "Arial", "white")

start = makeLabel("Find and click on the crashed lander!", 40, 50, 250, "black", "Arial", "white")

showLabel(start)
pause(1500)
hideLabel(start)

frame = 0
while True:
    if not found:
        moveSprite(lander, xPos, yPos, True)
        showSprite(lander)

    if keyPressed("right"):
        changeSpriteImage(testSprite, 2)  # 0*8 because right animations are the 0th set in the sprite sheet
        scrollBackground(-5, 0)  # The player is moving right, so we scroll the background left
        xSpeed -= 5

    elif keyPressed("down"):
        changeSpriteImage(testSprite, 0)  # down facing animations are the 1st set
        scrollBackground(0, -5)
        ySpeed -= 5

    elif keyPressed("left"):
        changeSpriteImage(testSprite, 1)  # and so on
        scrollBackground(5, 0)
        xSpeed += 5

    elif keyPressed("up"):
        changeSpriteImage(testSprite, 0)
        scrollBackground(0, 5)
        ySpeed += 5

    else:
        changeSpriteImage(testSprite, 0)  # the static facing front look

    xPos += xSpeed
    xSpeed = 0
    yPos += ySpeed
    ySpeed = 0

    if spriteClicked(lander):
        showLabel(game_over)
        killSprite(lander)
        found = True
        pause(500)
        hideLabel(game_over)

    updateDisplay()
    tick(120)

endWait()
