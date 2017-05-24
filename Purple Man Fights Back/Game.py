class Game():
    
    #global variables
    
    #screen scrolling
    scrollDis = 0
    saveDis = 0
    scrollSpeed = .06
    dir = 0
    screenW = 500
    screenH = 500
    stage = 0
    
    #player
    pW = 20
    pH = 61
    spawnX = screenW/2 - pW/2
    spawnY = 300
    bSpawnX = 0
    bSpawnY = 0
    pX = spawnX
    pY = spawnY
    pHit = False
    lives = 3
    maxLives = 3
    
    #powerups
    pJump = False
    pShield = False
    pWarp = False
    
    #projectile
    projX = 0
    projY = 0
    projW = 8
    projH = 6
    fire = False
    
    #gravity
    gravity = 0
    jump = 0
    
    #collisions
    numCollide = 0
    
    #platform
    platArray = []
    checkNum = 0
    pupNum = 0
    
    #keypresses
    aPress = False
    dPress = False
    wPress = False
    press = False
    
    #boss fight
    bossFight = False
    bulCnt = 0
    bEns = []
    credits = False
    
    #for music and credits
    cnt = 0
    cred = screenH*1.5
    
    def __init__(self):
        pass
        
    def grav(self):
        if Game.jump == 0 and Game.numCollide > 0:
            Game.gravity = 0
        else:
            Game.gravity -= .3
            
    def gameOver(self):
        #respawn if dead
        if Game.lives <= 0:
            Game.gravity = 0
            fill(200,0,0,100)
            rect(0,0,Game.screenW,Game.screenH)
            if mouseX > 105 and mouseX < 425 and mouseY > 246 and mouseY < 310:
                fill(255)
                if mousePressed == True:
                    Game.scrollDis = Game.saveDis
                    Game.pX = Game.spawnX
                    Game.pY = Game.spawnY
                    Game.lives = Game.maxLives
            else:
                fill(255, 140)
            textSize(64)
            text("Respawn?", 105, 300)
            
            