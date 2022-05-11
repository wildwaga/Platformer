from cmu_graphics import *
import level
app.stepsPerSecond = 30
app.playerSprite = Group(Image ('./sprite/idle_0.png',200-32,200-32))
app.player = Rect(200-32,200-32,64,64,fill='white')
app.ground = Group()
app.death = Group()
level.addShapes(app.ground,app.death)
app.death.visible=True
app.player.centerY=200
app.coD = Rect(0,0,36,64,fill=None)
app.parts = Group()
app.playerState='idle'
app.player.dy=0
app.player.dx=0 
app.playerFrame=0
app.steps=0
app.stepsLastFrame=0
app.stepsFalling=0
app.playerOnGround=False
app.gun= Group(Image('./sprite/gun_0.png',app.player.left,app.player.top))
app.gunAngle = 0
app.gun.visible=False
app.bullets=Group()
app.track = Sound('https://wildwaga.scarletvoid.com/platformer/game.mp3')
def updateCoD():
    if(app.player.dy>0):
        app.coD.height=(app.player.dy)+64
        app.coD.top=app.player.top
    elif(app.player.dy<0):
        app.coD.height=(-app.player.dy)+64
        app.coD.bottom=app.player.bottom
    else:
        app.coD.top = app.player.top
        app.coD.height = 64
    if(app.player.dx>0):
        app.coD.width=(app.player.dx)+36
        app.coD.left=app.player.left+14
    elif(app.player.dx<0):
        app.coD.width=(-app.player.dx)+36
        app.coD.right=app.player.right-14
    else:
        app.coD.left=app.player.left+14
        app.coD.width=36
def makeParts(X,Y,amount,color,min,max):
    for i in range(amount):
        part = Circle(X,Y,randrange(min,max),fill=color)
        part.dy = randrange(-5,10)
        part.dx = randrange(-5,10)
        app.parts.add(part)
def killPlayer():
    Rect(0,0,400,400,fill='white')
    Label('Game Over',200,100,size=75)
    app.playerSprite.visible = False
    app.gun.visible = False
    makeParts(200,200,10,'red',5,15)
def onStep():
    if(app.player.hitsShape(app.death)):
        killPlayer()
    for bullet in app.bullets.children:
        if ((bullet.left>400) or (bullet.right<0) or (bullet.top>400) or (bullet.bottom<0)):
            app.bullets.remove(bullet)
        else:
            bullet.centerX += bullet.dx
            bullet.centerY += bullet.dy
    #app.track.play()
    updateCoD()
    if((app.coD.hitsShape(app.ground))):
        app.player.dy//=1
        app.player.dx//=1
        while ((app.ground.hits(app.player.left,app.player.top)) and (app.ground.hits(app.player.right,app.player.right))):
                app.ground.centerY-=10
                app.player.dy=0
                app.player.dx=0
        while (app.coD.hitsShape(app.ground)):
            if(app.player.dy>0):
                app.player.dy-=1
            if(app.player.dy<0):
                app.player.dy+=1
            if(app.player.dx>0):
                app.player.dx-=1
            if(app.player.dx<0):
                app.player.dx+=1
            updateCoD()
        app.ground.centerX-=app.player.dx
        app.ground.centerY+=app.player.dy
        app.death.centerX-=app.player.dx
        app.death.centerY+=app.player.dy
        app.playerSprite.left=app.player.left
        app.playerSprite.top=app.player.top
        app.playerOnGround=True
        app.stepsFalling=0
        if(app.playerState=='jump'):
            app.playerState='idle'
    else:
        app.ground.centerX-=app.player.dx
        app.ground.centerY-=(app.player.dy)
        app.death.centerX-=app.player.dx
        app.death.centerY-=(app.player.dy)
        app.playerSprite.left=app.player.left
        app.playerSprite.top=app.player.top
        app.stepsFalling+=10
    app.player.dy+=((0.65*(app.stepsFalling*0.01)))
    for part in app.parts.children:
        part.centerX+=part.dx
        part.centerY+=part.dy
        part.dy+=0.65
        part.dx//=1
        if(part.dx>0):
            part.dx-=0.3
        if(part.dx<0):
            part.dx+=0.3
        if(part.top>400):
            app.parts.remove(part)
    app.steps+=1
    app.playerSprite.toFront()
    if(app.stepsLastFrame==15):
        app.stepsLastFrame=0
        if (app.playerState=='idle'):
            if(app.playerFrame >= 7):
                app.playerFrame = 0
                app.playerSprite.clear()
                app.playerSprite.add(Image('./sprite/idle_' + str(app.playerFrame) + '.png',app.player.left,app.player.top))
            else:
                app.playerFrame += 1
                app.playerSprite.clear()
                app.playerSprite.add(Image('./sprite/idle_' + str(app.playerFrame) + '.png',app.player.left,app.player.top))
        if (app.playerState=='walk'):
            if(app.playerFrame >= 1):
                app.playerFrame = 0
                app.playerSprite.clear()
                app.playerSprite.add(Image('./sprite/walk_' + str(app.playerFrame) + '.png',app.player.left,app.player.top))
            else:
                app.playerFrame += 1
                app.playerSprite.clear()
                app.playerSprite.add(Image('./sprite/walk_' + str(app.playerFrame) + '.png',app.player.left,app.player.top))
        if (app.playerState=='jump'):
            if(app.playerFrame >= 0):
                app.playerFrame = 0
                app.playerSprite.clear()
                app.playerSprite.add(Image('./sprite/jump_' + str(app.playerFrame) + '.png',app.player.left,app.player.top))
    else:
        app.stepsLastFrame+=1
    app.parts.toFront()
def onKeyHold(keys):
    if(('right' in keys) and ('left' in keys)):
        app.player.dx=0
        if(app.playerState!='idle'):
            app.stepsLastFrame=15
        if(app.playerState!='jump'):
            app.playerState='idle'
    elif('right' in keys):
        app.player.dx=4
        if(app.playerState!='walk'):
            app.stepsLastFrame=15
        if(app.playerState!='jump'):
            app.playerState='walk'
    elif('left' in keys):
        if(app.playerState!='walk'):
            app.stepsLastFrame=15
        if(app.playerState!='jump'):
            app.playerState='walk'
        app.player.dx=-4
    if(('up'in keys) and (app.playerOnGround == True)):
        app.playerState='jump'
        app.playerOnGround = False
        app.player.dy=-10
        app.ground.centerY+=10
        app.death.centerY+=10
        app.stepsLastFrame=15
def onKeyRelease(key):
    if(key!='up'):
        app.player.dx=0
        app.playerState='idle'
def onMouseMove(mouseX,mouseY):
    app.gunAngle = angleTo(200,200,mouseX,mouseY)
    newX, newY = getPointInDir(200,200,app.gunAngle,80)
    app.gun.centerX=newX
    app.gun.centerY=newY
    app.gun.rotateAngle = app.gunAngle-90
    if(app.gun.rotateAngle >=90):
        app.gun.clear()
        app.gun.add(Image('./sprite/gun_1.png',newX-32,newY-32,rotateAngle=app.gunAngle-90))
    else:
        app.gun.clear()
        app.gun.add(Image('./sprite/gun_0.png',newX-32,newY-32,rotateAngle=app.gunAngle-90))
    app.gun.visible = True
def onMousePress(mouseX,mouseY):
    onMouseMove(mouseX,mouseY)
    bullet = Rect(app.gun.centerX,app.gun.centerY,5,5,rotateAngle=app.gunAngle-90)
    centerX, centerY = getPointInDir(app.gun.centerX,app.gun.centerY,app.gunAngle,10)
    bullet.dy = centerY-app.gun.centerY
    bullet.dx = centerX-app.gun.centerX
    app.bullets.add(bullet)
    app.gun.toFront()
def onMouseDrag(mouseX,mouseY):
    onMouseMove(mouseX,mouseY)
cmu_graphics.run()