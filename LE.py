from cmu_graphics import *
engine = ['from cmu_graphics import *','def addShapes(shape,shape2):','    required = 1',]
def write():
    title=app.getTextInput('Where to save file')
    with open(title + '.py', 'w') as f:
        f.write('\n'.join(engine))
app.width=800
app.height=800
app.rectColor='green'
app.start = Rect(0,0,64,64,fill=None)
app.corner=Rect(0,0,64,64,fill='green')
app.currentSprite = 0
app.ground = Group()
app.spawn = Rect(200-32,200-32,64,64,fill='green')
app.ground.add(app.spawn)
app.blockType='ground'
app.placingBlock=False
app.tempBlock = Rect(400-40,400-40,64,64,fill='green',visible=False)
app.startingTempBlock = Rect(400-40,400-40,64,64,fill=None)
cursor = Rect(400-40,400-40,64,64,fill=None,border='black')
def updateTemp():
    if(app.startingTempBlock.centerX<cursor.centerX):
        app.tempBlock.width=cursor.right-app.tempBlock.left
    elif(app.startingTempBlock.centerX>cursor.centerX):
        app.tempBlock.width=app.tempBlock.right-cursor.left
        app.tempBlock.left=cursor.left
    else:
        app.tempBlock.left=cursor.left
        app.tempBlock.width=cursor.width
    if(app.startingTempBlock.centerY<cursor.centerY):
        app.tempBlock.height=cursor.bottom-app.tempBlock.top
    elif(app.startingTempBlock.centerY>cursor.centerY):
        app.tempBlock.height=app.tempBlock.bottom-cursor.top
        app.tempBlock.top=cursor.top
    else:
        app.tempBlock.top=cursor.top
        app.tempBlock.height=cursor.height
def onKeyPress(key):
    if (key == 'w'):
        app.ground.centerY+=64
        app.tempBlock.centerY+=64
        app.startingTempBlock.centerY+=64
        updateTemp()
    if(key == 's'):
        app.ground.centerY-=64
        app.tempBlock.centerY-=64
        app.startingTempBlock.centerY-=64
        updateTemp()
    if(key == 'a'):
        app.ground.centerX+=64
        app.tempBlock.centerX+=64
        app.startingTempBlock.centerX+=64
        updateTemp()
    if(key == 'd'):
        app.ground.centerX-=64
        app.tempBlock.centerX-=64
        app.startingTempBlock.centerX-=64
        updateTemp()
    if(key == 'enter'):
        if(app.placingBlock==False):
            app.placingBlock=True
            app.startingTempBlock.centerX=cursor.centerX
            app.startingTempBlock.centerY=cursor.centerY
            app.tempBlock.width=64
            app.tempBlock.height=64
            app.tempBlock.centerX=cursor.centerX
            app.tempBlock.centerY=cursor.centerY
            app.tempBlock.visible=True
        else:
            app.placingBlock=False
            app.tempBlock.visible=False
            if (app.blockType == 'ground'):
                if (app.spawn.centerX<cursor.centerX):
                    if(app.spawn.centerY<cursor.centerY):
                        engine.append('    shape.add(Rect(' + str(abs(app.spawn.centerX-app.tempBlock.left)+(200)) + ',' + str(abs(app.spawn.centerY-app.tempBlock.top)+(200)) + ',' + str(app.tempBlock.width) + ',' + str(app.tempBlock.height) +',fill="' + app.rectColor + '"))')
                    else:
                        engine.append('    shape.add(Rect(' + str(abs(app.spawn.centerX-app.tempBlock.left)+(200)) + ',' + str((200)-abs(app.spawn.centerY-app.tempBlock.top)) + ',' + str(app.tempBlock.width) + ',' + str(app.tempBlock.height) +',fill="' + app.rectColor + '"))')
                else:
                    if(app.spawn.centerY<cursor.centerY):
                        engine.append('    shape.add(Rect(' + str((200)-abs(app.spawn.centerX-app.tempBlock.left)) + ',' + str(abs(app.spawn.centerY-app.tempBlock.top)+(200)) + ',' + str(app.tempBlock.width) + ',' + str(app.tempBlock.height) +',fill="' + app.rectColor + '"))')
                    else:
                        engine.append('    shape.add(Rect(' + str((200)-abs(app.spawn.centerX-app.tempBlock.left)) + ',' + str((200)-abs(app.spawn.centerY-app.tempBlock.top)) + ',' + str(app.tempBlock.width) + ',' + str(app.tempBlock.height) +',fill="' + app.rectColor + '"))')
            elif (app.blockType == 'death'):
                if (app.spawn.centerX<cursor.centerX):
                    if(app.spawn.centerY<cursor.centerY):
                        engine.append('    shape2.add(Rect(' + str(abs(app.spawn.centerX-app.tempBlock.left)+(200)) + ',' + str(abs(app.spawn.centerY-app.tempBlock.top)+(200)) + ',' + str(app.tempBlock.width) + ',' + str(app.tempBlock.height) +',fill="' + app.rectColor + '"))')
                    else:
                        engine.append('    shape2.add(Rect(' + str(abs(app.spawn.centerX-app.tempBlock.left)+(200)) + ',' + str((200)-abs(app.spawn.centerY-app.tempBlock.top)) + ',' + str(app.tempBlock.width) + ',' + str(app.tempBlock.height) +',fill="' + app.rectColor + '"))')
                else:
                    if(app.spawn.centerY<cursor.centerY):
                        engine.append('    shape2.add(Rect(' + str((200)-abs(app.spawn.centerX-app.tempBlock.left)) + ',' + str(abs(app.spawn.centerY-app.tempBlock.top)+(200)) + ',' + str(app.tempBlock.width) + ',' + str(app.tempBlock.height) +',fill="' + app.rectColor + '"))')
                    else:
                        engine.append('    shape2.add(Rect(' + str((200)-abs(app.spawn.centerX-app.tempBlock.left)) + ',' + str((200)-abs(app.spawn.centerY-app.tempBlock.top)) + ',' + str(app.tempBlock.width) + ',' + str(app.tempBlock.height) +',fill="' + app.rectColor + '"))')
            app.ground.add(Rect(app.startingTempBlock.left,app.startingTempBlock.top,app.tempBlock.width,app.tempBlock.height,fill=app.rectColor))
    if(key == '1'):
        app.rectColor='green'
        app.blockType = 'ground'
        app.corner.fill=app.rectColor
        app.tempBlock.fill='green'
    if(key == '2'):
        app.rectColor='red'
        app.blockType = 'death'
        app.corner.fill=app.rectColor
        app.tempBlock.fill='red'
def onKeyHold(keys):
    if(('tab' in keys) and ('s' in keys)):
        write()
cmu_graphics.run()