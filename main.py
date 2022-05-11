from cmu_graphics import *
import os
app.stepsPerSecond = 30
app.background = 'black'
track = Sound('https://wildwaga.scarletvoid.com/platformer/intro.mp3')
app.steps = 0
title = Label('',200,200,fill='white',font='orbitron',size=24)
title.dy = 0
title.moving = False
def onStep():
    if(app.steps == 60):
        track.play()
        title.opacity = 100
        title.value = 'Presented by Compute Games'
    elif(app.steps==372):
        title.opacity = 100
        title.value = 'A Platforming Shootem Up'
    elif(app.steps==692):
        title.opacity = 100
        title.value = 'Blue Guy is a Murderer'
        title.moving=True
    elif((title.opacity > 0) and (title.moving == False)):
        title.opacity -= 1
    elif(app.steps >= 692):
        title.dy += 0.1
    title.centerY += title.dy
    if(title.top >= 400):
        title.bottom=0
    if(app.steps==1350):
        os.system('python3 game.py')
        os.system('python\python.exe game.py')
        exit()
    app.steps+=1
cmu_graphics.run()