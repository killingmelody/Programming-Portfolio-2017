from Game import Game

import random

class Platform(Game):

    # member variables
    
    #images
    tree = image
    stone1 = image
    stone2 = image
    potion = image
    spike = image
    
    #attributes
    tempX = 0
    platX = 0
    platY = 0
    platW = 0
    platH = 0
    type = str
    platNum = 0
    
    #powerups
    pup = False
    pupNum = 0

    # for collision function
    topBound = False
    sideBound = False

    def __init__(self, platType, platX, platY, platW, number):
        Game.platArray.extend((0,0,0))
        self.tempX = platX
        self.platY = platY
        self.platW = platW
        self.platH = 20
        Game.platArray[3*number] = platX
        Game.platArray[3*number+1] = platY
        Game.platArray[3*number+2] = platW
        self.type = platType
        self.platNum = number
        
        #setup platform type
        if platType == 'pup' or platType == 'check':
            self.pup = True

    def display(self):
        #render platforms
        self.platX = self.tempX + Game.scrollDis
        i = 0
        while i < self.platW:
            if self.type == 'boss':
                image(self.stone2,self.platX + i,self.platY)
            else:
                image(self.stone1,self.platX + i,self.platY)
            i += 20

    def collision(self):
        # check for top-collision with platform using boundaries
        if (Game.pY + Game.pH) <= self.platY and (Game.pY + Game.pH) >= (self.platY - abs(Game.gravity) * 2.5) and \
            Game.pX >= (self.platX - Game.pW) and Game.pX <= (self.platX + self.platW):
            if self.topBound == False:
                Game.numCollide += 1
            self.topBound = True
                
            #check for spikes
            if self.type == 'spike':
                Game.pHit = True
                if Game.lives > 1:
                    Game.scrollDis = Game.saveDis
                    Game.gravity = 0
                    Game.pX = Game.spawnX
                    Game.pY = Game.spawnY
                
                          
        else:
            if self.topBound == True:
                Game.numCollide -= 1
            self.topBound = False
            
        #display controls at beginning platform
        if self.platNum == 0 and self.topBound == True:
            fill(255,140)
            textSize(32)
            text("Use WASD to move", 100, 300)
            
        #check for powerup
        if self.type == 'pup':
            if self.pup == True:
                image(self.potion,self.platX + self.platW/2 - 5,self.platY - 16)
                if self.topBound == True and (Game.pX + Game.pW/2) > (self.platX + self.platW/2 - 5) and \
                        (Game.pX + Game.pW/2) < (self.platX + self.platW/2 + 5):
                    #powerup order
                    if Game.pupNum == 0:
                        Game.pJump = True
                    elif Game.pupNum == 1:
                        Game.maxLives = 4
                        Game.lives = 4
                    elif Game.pupNum == 2:
                        Game.pWarp = True
                    elif Game.pupNum == 3:
                        Game.maxLives = 5
                        Game.lives = 5
                    else:
                        Game.pShield = True
                    Game.pupNum += 1
                    self.pup = False
            else:
                if self.topBound == True:
                    fill(255,140)
                    textSize(32)
                    if Game.pupNum == 1:
                        text("Press space in midair \nto double jump", 80, 100)
                    elif Game.pupNum == 3:
                        text("Right click to warp \nover short distances", 80, 170)
                    elif Game.pupNum == 5:
                        text("Shields absorb \none damage", 80, 100)
        #boss platform
        elif self.type == 'boss':
            if Game.bossFight == False:
                if (Game.pX + Game.pW/2) > (self.platX + self.platW/2 - 5) and \
                        (Game.pX + Game.pW/2) < (self.platX + self.platW/2 + 5):
                    Game.lives = Game.maxLives
                    Game.pShield = True
                    Game.bSpawnX = self.platX + 30
                    Game.bSpawnY = self.platY - Game.pH - 30
                    Game.bossFight = True
                image(self.potion,self.platX + self.platW/2 - 5,self.platY - 16)
                    
        #checkpoint platform
        elif self.type == 'check':
            if self.topBound == True:
                if self.pup == True:
                    if Game.pX > (self.platX) and \
                        Game.pX < (self.platX + self.platW):
                        Game.lives = Game.maxLives
                        Game.spawnY = (self.platY - Game.pH) - 50
                        Game.saveDis = Game.scrollDis
                        Game.checkNum += 1
                        self.pup = False
                else:
                    fill(255,140)
                    textSize(32)
                    text("Checkpoint", 165, 100)
            image(self.tree,self.platX + 20,self.platY - 80)
            
        elif self.type == 'spike':
            j = 0
            while j < self.platW:
                image(self.spike,self.platX + j,self.platY - 26)
                j += 10

        # check for bound and jumping to activate gravity or not
        if Game.jump == 0 and self.topBound == True and self.type != 'spike':
            Game.pY = (self.platY - Game.pH)

    def jump(self):
        if Game.wPress == True:
            if (Game.pY + Game.pH) == self.platY and Game.jump == 0:
                Game.gravity = 7
                Game.jump = 1
        #double jump
        if Game.press == True:
            if Game.pJump == True and Game.jump == 1:
                Game.gravity = 7
                Game.jump = 2
                    
        # checks for whether or not character has landed
        if Game.jump > 0:
            #allows for strafing
            if Game.aPress == True:
                    Game.dir = 1
            elif Game.dPress == True:
                    Game.dir = -1
            if Game.gravity < 0 and self.topBound == True:
                Game.jump = 0
            if Game.bossFight == False:
                Game.scrollDis += Game.dir*Game.scrollSpeed