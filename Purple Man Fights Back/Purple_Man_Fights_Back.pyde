# Purple Man Fights Back 2017
# Code written by Dylan Webb
# Game artwork by Grey Larson, James Ninow, Edward Prutski, and Jake Soulier
# Soundtrack made by Evgeny Bekker

# setup

add_library("sound")

from Game import Game
from Player import Player
from Platform import Platform
from Enemy import Enemy
from Boss import Boss

def setup():
    size(500, 500)
    frameRate(60)
    
    #soundtrack
    global sf
    sf = SoundFile(this,"2017 VG Japan-1v7 5-17 Fade.mp3")

    # load images
    global bg1
    global bg2
    bg1 = loadImage("start.png")
    bg2 = loadImage("backPano.png")
    # player
    Player.heart = loadImage("heart.png")
    Player.shield = loadImage("shield.png")
    Player.playerL = loadImage("mainL.png")
    Player.playerR = loadImage("mainR.png")
    Player.bulletR = loadImage("bulletR.png")
    Player.bulletL = loadImage("bulletL.png")
    # boss
    Boss.bossImg1 = loadImage("boss1.png")
    Boss.bossImg2 = loadImage("boss2.png")
    Boss.bBullet = loadImage("bBullet.png")
    # platform
    Platform.stone1 = loadImage("stone1.png")
    Platform.stone2 = loadImage("stone2.png")
    Platform.tree = loadImage("tree.png")
    Platform.potion = loadImage("potion.png")
    Platform.spike = loadImage("spike.png")
    #enemies
    Enemy.eBullet = loadImage("eBullet.png")
    Enemy.walkerR = loadImage("walkerR.png")
    Enemy.walkerL = loadImage("walkerL.png")
    Enemy.jumper = loadImage("jumper.png")
    Enemy.shooter = loadImage("shooter.png")

# create objects

game = Game()

# Platform(type,xpos,ypos,width,num)
# start
plat0 = Platform('safe', 50, 400, 400, 0)
plat1 = Platform('spike', -110, 330, 100, 1)
plat2 = Platform('pup', -290, 400, 100, 2)
plat3 = Platform('safe', 500, 350, 200, 3)
plat4 = Platform('safe', 400, 270, 100, 4)
plat5 = Platform('safe', 300, 190, 100, 5)
plat6 = Platform('safe', 100, 110, 200, 6)
plat7 = Platform('spike', 700, 375, 100, 7)
plat8 = Platform('safe', 800, 350, 200, 8)
plat9 = Platform('check', 900, 190, 200, 9)
# checkpoint1
plat10 = Platform('safe', 1200, 190, 100, 10)
plat11 = Platform('safe', 1300, 450, 100, 11)
plat12 = Platform('safe', 1400, 190, 100, 12)
plat13 = Platform('pup', 1500, 450, 100, 13)
plat14 = Platform('safe', 1600, 190, 100, 14)
plat15 = Platform('safe', 1700, 450, 100, 15)
plat16 = Platform('safe', 1800, 180, 200, 16)
plat17 = Platform('safe', 1850, 270, 100, 17)
plat18 = Platform('safe', 1850, 360, 100, 18)
plat19 = Platform('spike', 1500, 360, 100, 19)
plat20 = Platform('safe', 2360, 180, 120, 20)
plat21 = Platform('check', 2500, 320, 200, 21)
# checkpoint2
plat22 = Platform('safe', 2700, 470, 200, 22)
plat23 = Platform('safe', 3000, 470, 100, 23)
plat24 = Platform('safe', 3100, 400, 100, 24)
plat25 = Platform('safe', 3300, 400, 100, 25)
plat26 = Platform('safe', 3150, 330, 150, 26)
plat27 = Platform('spike', 3200, 400, 100, 27)
plat28 = Platform('spike', 2700, 230, 200, 28)
plat29 = Platform('safe', 2900, 230, 100, 29)
plat30 = Platform('spike', 2700, 100, 150, 30)
plat31 = Platform('safe', 2850, 100, 230, 31)
plat32 = Platform('pup', 3080, 100, 70, 32)
plat33 = Platform('spike', 3150, 100, 50, 33)
plat34 = Platform('spike', 2850, 20, 400, 34)
plat35 = Platform('safe', 3200, 100, 100, 35)
plat36 = Platform('safe', 3400, 230, 200, 36)
plat37 = Platform('check', 3800, 330, 200, 37)
#checkpoint3
plat38 = Platform('safe', 4000, 460, 50, 38)
plat39 = Platform('safe', 4200, 460, 50, 39)
plat40 = Platform('safe', 4400, 460, 50, 40)
plat41 = Platform('safe', 4600, 360, 50, 41)
plat42 = Platform('safe', 4400, 260, 50, 42)
plat43 = Platform('safe', 4200, 160, 50, 43)
plat44 = Platform('safe', 4400, 60, 50, 44)
plat45 = Platform('pup', 4600, 60, 50, 45)
plat46 = Platform('safe', 4800, 260, 50, 46)
plat47 = Platform('safe', 5000, 260, 50, 47)
plat48 = Platform('safe', 5200, 360, 50, 48)
plat49 = Platform('check', 5400, 460, 200, 49)
#checkpoint4
plat50 = Platform('safe', 5600, 460, 200, 50)
plat51 = Platform('spike', 5800, 460, 100, 51)
plat52 = Platform('safe', 5800, 370, 100, 52)
plat53 = Platform('safe', 5800, 280, 100, 53)
plat54 = Platform('safe', 6000, 140, 100, 54)
plat55 = Platform('safe', 6300, 140, 100, 55)
plat56 = Platform('safe', 6600, 140, 100, 56)
plat57 = Platform('spike', 6000, 240, 700, 57)
plat58 = Platform('safe', 6150, 320, 100, 58)
plat59 = Platform('safe', 6250, 320, 100, 59)
plat60 = Platform('safe', 6350, 320, 100, 60)
plat61 = Platform('safe', 6450, 320, 100, 61)
plat62 = Platform('safe', 6700, 360, 200, 62)
plat63 = Platform('pup', 6050, 320, 100, 63)
plat64 = Platform('safe', 6900, 450, 200, 64)
plat65 = Platform('safe', 6600, 360, 100, 65)
plat66 = Platform('check', 7300, 390, 200, 66)

#checkpoint5
plat67 = Platform('safe', 7600, 330, 100, 67)
plat68 = Platform('safe', 7800, 270, 100, 68)
plat69 = Platform('safe', 8000, 210, 100, 69)
plat70 = Platform('boss', 8200, 450, 460, 70)


plats = [plat0, plat1, plat2, plat3, plat4, plat5, plat6, plat7, plat8, plat9, plat10, plat11,\
         plat12, plat13, plat14, plat15, plat16, plat17, plat18, plat19, plat20, plat21, plat22,\
         plat23, plat24, plat25, plat26, plat27, plat28, plat29, plat30, plat31, plat32, plat33,\
         plat34, plat35, plat36, plat37, plat38, plat39, plat40, plat41, plat42, plat43, plat44,\
         plat45, plat46, plat47, plat48, plat49, plat50, plat51, plat52, plat53, plat54, plat55,\
         plat56, plat57, plat58, plat59, plat60, plat61, plat62, plat63, plat64, plat65, plat66,\
         plat67, plat68, plat69, plat70]

# Enemy(type,num)--num matches platform it's on
# start
en1 = Enemy('patrol', 3)
en2 = Enemy('jump', 5)
en3 = Enemy('shoot', 6)
en4 = Enemy('patrol', 8)
# checkpoint1
en5 = Enemy('shoot', 11)
en6 = Enemy('shoot', 13)
en7 = Enemy('shoot', 15)
en8 = Enemy('shoot', 16)
en9 = Enemy('jump', 16)
en10 = Enemy('patrol', 20)
# checkpoint2
en11 = Enemy('shoot', 23)
en12 = Enemy('shoot', 25)
en13 = Enemy('patrol',26)
en14 = Enemy('jump', 29)
en15 = Enemy('jump', 29)
en16 = Enemy('patrol', 31)
en17 = Enemy('patrol', 31)
en18 = Enemy('patrol', 31)
en19 = Enemy('shoot', 36)
en20 = Enemy('patrol', 36)
#checkpoint3
en21 = Enemy('shoot', 40)
#checkpoint4
en22 = Enemy('jump', 50)
en23 = Enemy('patrol', 50)
en24 = Enemy('shoot', 58)
en25 = Enemy('shoot', 59)
en26 = Enemy('shoot', 60)
en27 = Enemy('shoot', 61)
en28 = Enemy('patrol', 62)
en29 = Enemy('patrol', 62)
en30 = Enemy('patrol', 62)
en31 = Enemy('patrol', 62)
en32 = Enemy('patrol', 64)
en33 = Enemy('patrol', 64)
en34 = Enemy('patrol', 64)
en35 = Enemy('patrol', 64)

ens = [en1, en2, en3, en4, en5, en6, en7, en8, en9, en10, en11, en12, en13, en14, en15, en16,\
       en17, en18, en19, en20, en21, en22, en23, en24, en25, en26, en27, en27, en28, en29, en30,\
       en31, en32, en33, en34, en35]

b1 = Boss(1, 70)

p1 = Player()

def draw():
    #play music
    if Game.cnt == 0:
        sf.play()
        Game.cnt = 14200
    Game.cnt -= 1
    
    #start and end screens
    if Game.stage == 0:
        image(bg1, 0, 0)
        if Game.bossFight == False:
            if mouseX > 80 and mouseX < 420 and mouseY > 246 and mouseY < 310:
                fill(255)
                if mousePressed == True:
                    Game.stage = 1
            else:
                fill(255, 140)
            textSize(64)
            text("Start Game", 80, 300)
        else:
            #credits
            fill(255)
            textSize(64)
            text("Purple Man\nFights Back", 80, Game.cred)
            fill(255, 140)
            text("Coding:", 80, Game.cred+300)
            textSize(50)
            text("Dylan Webb", 80, Game.cred+400)
            textSize(64)
            text("Artwork:", 80, Game.cred+600)
            textSize(50)
            text("Grey Larson", 80, Game.cred+700)
            text("James Ninow", 80, Game.cred+800)
            text("Edward Prutski", 80, Game.cred+900)
            text("Jake Soulier", 80, Game.cred+1000)
            textSize(64)
            text("Soundtrack:", 80, Game.cred+1200)
            textSize(50)
            text("Evgeny Bekker", 80, Game.cred+1300)
            fill(255)
            textSize(64)
            text("The End", 130, Game.cred+1700)
            if Game.cred > -(Game.screenH*2.5 + 175):
                Game.cred -= 1
    
    #main game
    if Game.stage == 1:
        image(bg2, floor(Game.scrollDis * .1) - 50, 0)
        for i in plats:
            i.jump()
        p1.movement()
        p1.display()
        p1.hit()
        for i in plats:
            i.collision()
            i.display()
        for i in ens:
            i.movement()
            i.display()
            i.collision()
        game.grav()
        game.gameOver()
        if Game.bossFight == True:
            b1.movement()
            b1.display()
            b1.collision()
            for i in Game.bEns:
                i.display()
                i.collision()
                i.movement()

def keyPressed():
    if key == 'a' or key == 'A':
        Game.aPress = True
    if key == 'd' or key == 'D':
        Game.dPress = True
    if key == 'w' or key == 'W':
        Game.wPress = True
    if key == ' ':
        Game.press = True
    if key == 'ESC':
        sys.close()

def keyReleased():
    if key == 'a' or key == 'A':
        Game.aPress = False
    if key == 'd' or key == 'D':
        Game.dPress = False
    if key == 'w' or key == 'W':
        Game.wPress = False
    if key == ' ':
        Game.press = False