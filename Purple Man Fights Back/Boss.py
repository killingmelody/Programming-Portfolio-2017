from Game import Game
from Enemy import Enemy

import random

class Boss(Game):
    
    #member variables
    
    #images
    bossImg1 = image
    bossImg2 = image
    bBullet = image
    
    #member
    lives = 0
    stage = 0
    begin = True
    action = False
    counter1 = 0
    counter2 = 0
    collide = False
    speed = 0
    stageLock = False
    
    #colors
    c1 = 0
    
    #location
    bX = 0
    bY = 0
    bW = 0
    bH = 0
    bulNum = 0
    bulArray = []
    bulX = []
    bulY = []
    bulOutArray = []
    bulW = 0
    bulH = 0
    bossNum = 0
    platNum = 0
    dir = 1
    
    def __init__(self,bNum,pNum):
        self.bossNum = bNum
        self.platNum = pNum
        if self.bossNum == 1:
            self.lives = 10
            self.bW = 128
            self.bH = 64
            self.bulNum = 6
            self.bulW = 10
            self.bulH = 10
            self.counter1 = 300
            self.speed = 2.5
        
    def display(self):
        #reset for if player died
        if Game.scrollDis >= (Game.saveDis - 5) and Game.scrollDis <= (Game.saveDis + 5):
            self.lives = 10
            self.stage = 0
            self.bW = 128
            self.bH = 64
            self.bulNum = 6
            self.bulW = 12
            self.bulH = 12
            self.counter1 = 300
            self.speed = 2.5
            Game.bEns = []
            Game.bossFight = False
        
        #load image
        if self.collide == False:
            image(self.bossImg1,self.bX,self.bY)
        else:
            image(self.bossImg2,self.bX,self.bY)
        
    
    def movement(self):
        if self.bossNum == 1:
            
            #position
            if self.stage == 0:
                self.bX = Game.screenW/2 - self.bW/2
                self.bY = -self.bH - 5
                self.stage = 1
                
            #lower
            elif self.stage == 1:
                if self.bY < (self.bH + 10):
                    self.bY += 1
                else:
                    #assign bullet starting xpos
                    self.bulArray = [int]*(self.bulNum + 6)
                    platW = Game.platArray[3 * self.platNum + 2]
                    i = 0
                    while i < self.bulNum + 6:
                        if i < self.bulNum:
                            self.bulArray[i] = platW*i*.2
                        elif i < self.bulNum + 2:
                            self.bulArray[i] = platW*(i - self.bulNum)*.5 + platW*.5*.25
                        elif i < self.bulNum + 4:
                            self.bulArray[i] = platW*((i - 2) - self.bulNum)*.5 + platW*.5*.5
                        elif i < self.bulNum + 6:
                            self.bulArray[i] = platW*((i - 4) - self.bulNum)*.5 + platW*.5*.75
                        i += 1 
                    self.bulOutArray = [0]*len(self.bulArray)
                    self.bulX = [int]*self.bulNum
                    self.bulY = [int]*self.bulNum
                    self.stage = 2
                    
            #move right and left and drop
            elif self.stage == 2:
                if self.counter1 > 0:
                    if (self.bX + self.bW) >= (Game.platArray[3 * self.platNum] + Game.scrollDis \
                                               + Game.platArray[3 * self.platNum + 2]) or \
                    self.bX <= (Game.platArray[3 * self.platNum] + Game.scrollDis):
                        self.dir *= - 1
                    self.bX += self.speed*self.dir
                    self.counter1 -= 1
                    self.collide = False
                else:
                    if (self.bY + self.bH - 1) <= Game.platArray[3 * self.platNum + 1] and self.action == False:
                        self.bY += self.speed*3
                        
                    elif self.bY > (self.bH + 10):
                        self.action = True
                        if self.counter2 > 40:
                            self.bY -= 2
                        else:
                            self.counter2 += 1
                    else:
                        self.counter1 = random.randint(Game.screenW/2,Game.screenW)
                        self.counter2 = 0
                        self.action = False
                        #changing stage
                        if self.stageLock == False:
                            if self.lives == 7 or self.lives == 4 or self.lives == 1:
                                self.action = False
                                self.speed += .5
                                self.collide = False
                                self.counter1 = 0
                                self.counter2 = 0
                                self.stage = 3
                        else:
                            if self.lives == 6 or self.lives == 3:
                                self.stageLock = False
                                
                        if self.lives == 0:
                            self.stage = 5
            
            #bullet mode
            elif self.stage == 3:
                self.c1 = 0
                #return to center
                if self.bX != Game.screenW/2 - self.bW/2:
                    if self.bX > Game.screenW/2 - self.bW/2:
                        self.bX -= 2
                    elif self.bX < Game.screenW/2 - self.bW/2:
                        self.bX += 2
                    if self.bX > Game.screenW/2 - self.bW/2 - 2 and self.bX < Game.screenW/2 - self.bW/2 + 2:
                        self.bX = Game.screenW/2 - self.bW/2
                        
                #fire bullets
                else:
                    if self.action == False:
                        #store bullets
                        i = 0
                        while i < self.bulNum:
                            self.bulX[i] = self.bulArray[i]
                            self.bulY[i] = 20*random.randint(-1,1) + 20
                            self.bulOutArray[i] = 0
                            i += 1
                        self.action = True
                    else:
                        #draw and move bullets
                        j = 0
                        while j < self.bulNum:
                            image(self.bBullet,self.bulX[j],self.bulY[j])
                            if self.counter1 % 4 == 0:
                                self.bulX[j] += 12*random.randint(-1,1)
                                self.bulY[j] += 12
                            #check for player collision
                            if (self.bulX[j] + self.bulW) >= Game.pX and self.bulX[j] <= (Game.pX + Game.pW):
                                if (self.bulY[j] + self.bulH) >= Game.pY and self.bulY[j] <= (Game.pY + Game.pH):
                                    Game.pHit = True
                            #check for off-screen collision
                            if self.bulY[j] > Game.platArray[3 * self.platNum + 1] and self.bulOutArray[j] == 0:
                                Game.bulCnt += 1
                                self.bulOutArray[j] = 1
                            j += 1
                        
                        #check if bullets are all off screen
                        if Game.bulCnt == self.bulNum:
                            self.counter2 += 1
                            Game.bulCnt = 0
                            self.action = False
                            
                    #change stage
                    if self.counter2 == 3:
                        self.counter1 = 250
                        self.counter2 = 0
                        self.bulNum += 2
                        self.bulX = [int]*self.bulNum
                        self.bulY = [int]*self.bulNum
                        #spawn enemies
                        Game.bEns = []
                        en1 = Enemy('patrol',self.platNum)
                        en2 = Enemy('patrol',self.platNum)
                        en3 = Enemy('patrol',self.platNum)
                        en4 = Enemy('patrol',self.platNum)
                        en5 = Enemy('patrol',self.platNum)
                        ens = [en1,en2,en3,en4,en5]
                        k = 0
                        while k < self.bulNum*.3:
                            Game.bEns.append(ens[k])
                            k += 1
                        if self.lives == 1:
                            self.stage = 4
                        else:
                            self.stageLock = True
                            self.stage = 2
                    self.counter1 += 1 #counter keeps bullets moving slowly
            
            #final stage
            elif self.stage == 4:
                if (self.bY + self.bH - 5) <= Game.platArray[3 * self.platNum + 1]:
                    self.collide = False
                    self.dir = 1
                    self.bY += self.speed*3
                        
                else:
                    if self.collide == False:
                        if (self.bX + self.bW) >= (Game.platArray[3 * self.platNum] + Game.scrollDis \
                                               + Game.platArray[3 * self.platNum + 2]) or \
                            self.bX <= (Game.platArray[3 * self.platNum] + Game.scrollDis):
                            self.dir *= - 1
                        self.bX += self.speed*self.dir
                    
                    else:
                        self.stage = 5
                        
            #death stage
            if self.stage == 5:
                if self.bY <= Game.screenW*1.5:
                    self.bY += .5
                else:
                    Game.stage = 0
                        
    def collision(self):
        if self.collide == False:
            self.c1 = 0
            if (Game.pX + Game.pW) >= self.bX and Game.pX <= (self.bX + self.bW) and \
                Game.pY <= (self.bY + self.bH):
                if (Game.pY + Game.pH - 8) >= self.bY:
                    Game.pHit = True
                elif (Game.pY + Game.pH) >= self.bY and self.lives > 0:
                    Game.gravity = 7
                    self.bX -= 1
                    self.lives -= 1
                    self.collide = True
            
        #boss health bar
        if self.lives > 0:
            stroke(0)
            fill(200,0,0)
            rect(10, Game.screenH - 20, Game.screenW*self.lives*.1 - 20, 10)