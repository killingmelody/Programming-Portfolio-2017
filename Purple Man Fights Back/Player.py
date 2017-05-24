from Game import Game

class Player(Game):
    
    #member variables
    
    #images
    heart = image
    shield = image
    bulletL = image
    bulletR = image
    playerL = image
    playerR = image
    
    #projectile
    speed = 12
    bAim = 0
    pCounter = 0
    bCounter = 0
    
    #warp
    warpCool = 0
    wAim = 0
    
    def __init__(self):
        pass
        
    def display(self):
        #player
        Game.pY -= Game.gravity
        if mouseX >= Game.pX and Game.lives > 0:
            image(self.playerR,Game.pX - 8,Game.pY)
        else:
            pass
            image(self.playerL,Game.pX - 8,Game.pY)
        
        if Game.jump == 0:
            Game.dir = 0
        
        #display shield
        if Game.pShield == True:
            image(self.shield,Game.pX + 3,Game.pY + 15)
        
        #mouseclick events
        if mousePressed == True and Game.lives > 0:
            
            #projectile
            if mouseButton == LEFT:
                if Game.fire == False:
                    if mouseX >= Game.pX:
                        self.bAim = 1
                    else:
                        self.bAim = -1
                    Game.projX = Game.pX + Game.pW/2
                    Game.projY = Game.pY + Game.pH/2
                    Game.fire = True
            #warp
            if mouseButton == RIGHT:
                if Game.pWarp == True and self.warpCool == 150:
                    if mouseX >= Game.pX:
                        self.wAim = 1
                    else:
                        self.wAim = -1
                    if Game.bossFight == True:
                        Game.pX += 100*self.wAim
                    else:
                        Game.scrollDis -= 100*self.wAim
                    self.warpCool = 0
            
        #warp cooldown
        if Game.pWarp == True:
            if self.warpCool < 150:
                self.warpCool += 3
            stroke(0)
            fill(255)
            rect(Game.screenW - 180, 50, self.warpCool, 5)
   
    def movement(self):
        
        #player
        if Game.jump == 0 and Game.lives > 0:
            if Game.aPress == True:
                Game.dir = 1
                if Game.bossFight == False:
                    Game.scrollDis += Game.dir*Game.scrollSpeed*60
            elif Game.dPress == True:
                Game.dir = -1
                if Game.bossFight == False:
                    Game.scrollDis += Game.dir*Game.scrollSpeed*60
            
        #boss condition movement
        if Game.bossFight == True:
            Game.pX += Game.scrollSpeed*40*Game.dir*-1
        
        #projectile
        if Game.fire == True:
            if self.bAim < 0:
                image(self.bulletL,Game.projX,Game.projY)
            else:
                image(self.bulletR,Game.projX,Game.projY)
            Game.projX += self.speed*self.bAim
            self.bCounter += 1
            if self.bCounter > 20:
                Game.fire = False
                self.bCounter = 0
        else:
            Game.projX = -10
            Game.projY = -10

    def hit(self):
        #display hearts
        i = 0
        while i < Game.lives:
            image(self.heart,i*31 + 20,40)
            i+=1
        
        #subtracts lives upon collision
        if Game.pHit == True:
            if self.pCounter == 0:
                if Game.pShield == False:
                    self.pCounter = 50
                    Game.lives -= 1
                    Game.jump = 0
                    Game.pHit = False
                
                #checks for shield
                else:
                    self.pCounter = 50
                    Game.pShield = False
              
            #provides timer to avoid immediate death  
            elif self.pCounter > 0:
                Game.pHit = False
        
        if self.pCounter > 0:
            self.pCounter -= 1
        
        #catches player and respawns
        if Game.pY > Game.screenH:
            if Game.lives > 1:
                Game.gravity = 0
                if Game.bossFight == False:
                    Game.pX = Game.spawnX
                    Game.pY = Game.spawnY
                    Game.scrollDis = Game.saveDis
                else:
                    Game.pX = Game.bSpawnX
                    Game.pY = Game.bSpawnY
            Game.pHit = True
        
        