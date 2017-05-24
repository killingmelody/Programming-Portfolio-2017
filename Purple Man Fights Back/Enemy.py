from Game import Game

import random

class Enemy(Game):
    # member variables
    
    #images
    eBullet = image
    walkerR = image
    walkerL = image
    jumper = image
    shooter = image

    #attributes
    eX = 0
    eY = 0
    eW = 0
    eH = 0
    death = False
    num = 0
    area = 0

    # for types of enemiesa
    type = str
    speed = 0
    dir = 0
    action = False

    # colors
    c1 = 0
    c2 = 0
    c3 = 0

    # shooting
    epX = []
    epY = []
    epW = 8
    epH = 8
    angleArray = []
    bulNum = 5

    def __init__(self, enemyType, number):
        self.type = enemyType
        self.num = number

        # for separate types of enemies
        if self.type == 'patrol':
            self.c1 = 0
            self.c2 = 255
            self.c3 = 255
            self.eH = 64
            self.eW = 17
            self.speed = 2
            self.dir = -1
        elif self.type == 'jump':
            self.c1 = 255
            self.c2 = 0
            self.c3 = 255
            self.eH = 45
            self.eW = 36
            self.dir = Game.platArray[3 * number + 1] - self.eH - 1
        elif self.type == 'shoot':
            self.c1 = 0
            self.c2 = 255
            self.c3 = 0
            self.eH = 30
            self.eW = 40
            self.action = False
            self.speed = 7
            self.angleArray = [1,0,-1,0,1,-1,-1,-1,0,-1]
            self.epX = [int]*self.bulNum
            self.epY = [int]*self.bulNum

        self.eX = Game.platArray[3 * number] + random.randint(0, (Game.platArray[3 * number + 2] - self.eW - 1))
        self.eY = Game.platArray[3 * number + 1] - self.eH - 1

    def display(self):
        if self.death == False:
            if self.type == 'patrol':
                if self.dir == 1:
                    image(self.walkerR,self.eX + Game.scrollDis,self.eY)
                else:
                    image(self.walkerL,self.eX + Game.scrollDis,self.eY)
            elif self.type == 'jump':
                image(self.jumper,self.eX + Game.scrollDis,self.eY)
            elif self.type == 'shoot':
                image(self.shooter,self.eX + Game.scrollDis,self.eY)
                
            #groups enemies into spawn areas
            self.area = Game.checkNum
        else:
            if self.area == Game.checkNum and Game.lives <= 0:
                self.death = False

    def collision(self):

        # player collision
        if (Game.pX + Game.pW) >= self.eX + Game.scrollDis and Game.pX <= (self.eX + Game.scrollDis + self.eW):
            if Game.pY <= self.eY + self.eH + 1:
                if (Game.pY + Game.pH - 8) >= self.eY and self.death == False:
                    Game.pHit = True
                elif (Game.pY + Game.pH) >= self.eY:
                    self.death = True

        # projectile collision
        if (Game.projY + Game.projH) >= self.eY and Game.projY <= (self.eY + self.eH + 1):
            if (Game.projX + Game.projW >= self.eX + Game.scrollDis) and \
                Game.projX <= (self.eX + Game.scrollDis + self.eW):
                if self.death == False:
                    self.death = True
                    Game.fire = False
                    
    def movement(self):
        if self.death == False:

            # patrolling
            if self.type == 'patrol':
                if self.eX <= Game.platArray[3 * self.num] or \
                        self.eX >= Game.platArray[3 * self.num] + Game.platArray[3 * self.num + 2] - self.eW:
                    self.dir *= - 1
                self.eX += self.speed * self.dir

            # jumping
            elif self.type == 'jump':
                if self.eY >= (self.dir - 2) and self.eY <= (self.dir + 2):
                    self.speed = 5.4
                self.eY -= self.speed
                self.speed -= .2

            # shooting
            elif self.type == 'shoot':
                if self.action == False:
                    
                    #generate loop
                    i = 0
                    while i < self.bulNum:
                        self.epX[i] = self.eX + self.eW/2 - self.epW/2 + Game.scrollDis
                        self.epY[i] = self.eY + self.eH/2 - self.epH/2
                        i+=1
                    self.action = True
                    
                else:
                    #position update loop
                    j = 0
                    while j < self.bulNum:
                        self.epX[j] += self.angleArray[2*j]*self.speed
                        self.epY[j] += self.angleArray[2*j+1]*self.speed
                        image(self.eBullet,self.epX[j],self.epY[j])

                        # check for player collision
                        if (self.epX[j] + self.epW) >= Game.pX and self.epX[j] <= (Game.pX + Game.pW):
                            if (self.epY[j] + self.epH) >= Game.pY and self.epY[j] <= (Game.pY + Game.pH):
                                Game.pHit = True
                                self.action = False
    
                        # time bound
                        if second()%2 == 0:
                            self.action = False
                            
                        j+=1
                