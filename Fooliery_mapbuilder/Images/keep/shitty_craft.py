import pygame, sys, random,os
from pygame.locals import *
from pygame import *



'''GAME DIMENTIONS'''



BLACK =(0,0,0)
BROWN = (153,76,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
RED = (255,000,000)
GREY = (50,50,50)
WHITE = (255,255,255)

TILESIZE  = 40
MAPWIDTH  = 25
MAPHEIGHT = 12


'''class Player(pygame.sprite.Sprite):
    
    
    
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load('player.png')
       
       
       self.pos = startpos
       
       self.rect = self.image.get_rect()
    def update(self):
       self.rect.center = self.pos'''

def secret():

    resources.append(SUM1)
    
        
        

    





cloudx = -200
cloudy = random.randint(0,MAPHEIGHT*TILESIZE)
cloudxx = -200
cloudyy = random.randint(0,MAPHEIGHT*TILESIZE)
birdx = -400
birdy = random.randint(0,MAPHEIGHT*TILESIZE)
invo = True

fpsClock = pygame.time.Clock()



DIRT   = 0
GRASS  = 1
WATER  = 2
COAL   = 3
LAVA   = 4
STONE  = 5
DIMOND = 6
CLOUD  = 7
BIRD   = 8
TREE   = 9
FIREDIMOND = 10
SUNSTONE = 11
CORNER = 12
CLOUD2 = 13
MSG = 14
PUMPKIN = 15
FLOWER = 16
STOVE = 17
FIRE = 18
SECRET = 19
SUM1 = 20

"""this is how to make a dictonary
linking colors to tiles"""

textures = {
           DIRT:  pygame.image.load('dirt.bmp'),
           GRASS: pygame.image.load('grass.png'),
           WATER: pygame.image.load('water.png'),
           COAL:  pygame.image.load('coal.png'),
           LAVA:  pygame.image.load('lava.png'),
           STONE: pygame.image.load('stone.png'),    
           DIMOND:pygame.image.load('dimond.png'),
           TREE:  pygame.image.load('tree.png'),
           CLOUD: pygame.image.load('cloud.png'),
           BIRD:  pygame.image.load('bird.png'),
           FIREDIMOND: pygame.image.load('firedimond.png'),
           SUNSTONE: pygame.image.load('sunstone.png'),
           CORNER: pygame.image.load('corner1.png'),
           CLOUD2: pygame.image.load('cloud2 (2).png'),
           MSG: pygame.image.load('msg.png'),
           PUMPKIN: pygame.image.load('pumpkin.png'),
           FLOWER:pygame.image.load('flower.png'),
           STOVE:pygame.image.load('stove.png'),
           FIRE: pygame.image.load('fire.png'),
           SECRET:pygame.image.load('secret.png'),
           SUM1: pygame.image.load('lala.png')
           
           
           
           
    }







inventory = {
    DIRT  :0,
    STONE :0,
    DIMOND:0,
    WATER :0,
    COAL  :0,
    LAVA  :0,
    GRASS :0,
    TREE  :0,
    FIREDIMOND:0,
    SUNSTONE:0,
    PUMPKIN:0,
    FLOWER:0,
    STOVE:0,
    FIRE:0,
    SECRET:0
    
    
    }
inventory2 = {
                


    
    }

craft = {
            FIREDIMOND: {LAVA: 2, DIMOND: 1},
            SUNSTONE: {STONE: 1, FIREDIMOND: 1},
            PUMPKIN: {DIRT: 5, GRASS: 1, WATER: 1},
            FLOWER: {DIRT: 1, WATER: 1},
            STOVE: {STONE:2},
            FIRE:{LAVA:1, TREE: 1},
            SECRET: {FIREDIMOND:1,SUNSTONE:1,PUMPKIN:1}


            
    }

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE + 50))
PLAYER = pygame.image.load('player.png')





ENEMY = pygame.image.load('enemy.png')

SUM = pygame.image.load('sum1.png')


playerPos = [0,1]
enemyPos =[0,0]
sumPos = [0,80]

resources = [DIRT,GRASS,WATER,COAL,LAVA,STONE,DIMOND,TREE,FIREDIMOND,SUNSTONE,PUMPKIN,FLOWER,STOVE,FIRE,SECRET]


'''a list representing our tilemap'''
tilemap = [ [DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)] 
    
currentTile = tilemap[playerPos[1]][playerPos[0]]
enemyTile = tilemap[enemyPos[1]][enemyPos[0]]

def dc(x1,y1,w1,h1,x2,y2,w2,h2):
    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
        return True
    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
        return True
    elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
        return True
    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
        return True
    else:
        return False
    




#ADDING A FONT FOR OUR INVENTORY
INVFONT =  pygame.font.Font(None,18)
INVFONT2 =  pygame.font.Font(None,40)
pygame.display.set_caption('S H I T T Y - C R A F T - 2D')
pygame.display.set_icon(pygame.image.load('player.png'))

pygame.mixer.music.load('gamemusic.mid')
pygame.mixer.music.play(100)
talk1=INVFONT2.render('KEY[x]=CONTROLS   |||   KEY[z]=defult screen',True,(WHITE))
SAYINGHELLO = INVFONT.render('place secret box on tile 1,1',1,(WHITE))
SAYINGHELLO2 = INVFONT.render('..',1,(WHITE))
birdTalk =INVFONT2.render(' PUT THE FIRE OUT QUICK',1,(WHITE))
#loop threw each row
for rw in range(MAPHEIGHT):
    for cl in range(MAPWIDTH):
        randomNumber = random.randint(0,25)
        if randomNumber == 0 or randomNumber == 6:
            tile = COAL
        elif randomNumber == 1 or randomNumber == 2 or randomNumber == 10 or randomNumber == 11:
            tile = STONE
        elif randomNumber == 3 or randomNumber == 4 or randomNumber == 5:
            tile = GRASS
        elif randomNumber == 7 or randomNumber == 8 or randomNumber == 12:
            tile = WATER
        elif randomNumber == 9 or randomNumber == 13:
            tile = LAVA
        elif randomNumber == 14:
            tile = DIMOND
        elif randomNumber == 15 or randomNumber == 16 or randomNumber == 17:
            tile = TREE
        else:
            tile = DIRT
            #set the positon in the tilemap to the randomly chosen tile
        
            
        
        tilemap[rw][cl] = tile
        tilemap[11][0] = CORNER

while True:
    
    
    
    DISPLAYSURF.fill(BLACK)
    for event in pygame.event.get():
       
        
            
            
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT and playerPos[0]< MAPWIDTH - 1:
                playerPos[0] += 1
            if event.key == K_LEFT and playerPos[0]> 0:
                playerPos[0] -= 1
            if event.key == K_UP and playerPos[1] > 0:
                playerPos[1] -= 1
            if event.key == K_DOWN and playerPos[1]< MAPHEIGHT - 1:
                playerPos[1] += 1
            if event.key == K_SPACE:
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                inventory[currentTile] += 1
                tilemap[playerPos[1]][playerPos[0]] = DIRT
            
            if event.key == K_z:
                invo = True
            if event.key ==K_x:
                invo = False

            
           


            
#REFRENCE FOR CONTROLS...CUZ THE DAMN LOOP FAILED MY ASS...SOMETIMES MANUAL IS BETTER
#the keys for placing blocks follows resourses:resources = [DIRT,GRASS,WATER,COAL,LAVA,STONE,DIMOND,TREE,FIREDIMOND,SUNSTONE]            
             
                
            if (event.key ==K_1):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[DIRT]>0:
                
                    inventory[DIRT] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = DIRT
                    inventory[currentTile] += 1
            if (event.key ==K_2):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[GRASS]>0:
                
                    inventory[GRASS] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = GRASS
                    inventory[currentTile] += 1
            if (event.key ==K_3):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[WATER]>0:
                
                    inventory[WATER] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = WATER
                    inventory[currentTile] += 1
            if (event.key ==K_4):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[COAL]>0:
                
                    inventory[COAL] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = COAL
                    inventory[currentTile] += 1
            if (event.key ==K_5):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[LAVA]>0:
                
                    inventory[LAVA] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = LAVA
                    inventory[currentTile] += 1
            if (event.key ==K_6):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[STONE]>0:
                
                    inventory[STONE] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = STONE
                    inventory[currentTile] += 1
            if (event.key ==K_7):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[DIMOND]>0:
                
                    inventory[DIMOND] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = DIMOND
                    inventory[currentTile] += 1
            if (event.key ==K_8):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[TREE]>0:
                
                    inventory[TREE] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = TREE
                    inventory[currentTile] += 1
             
            if (event.key ==K_9):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[FIREDIMOND]>0:
                
                    inventory[FIREDIMOND] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = FIREDIMOND
                    inventory[currentTile] += 1
            if (event.key ==K_0):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[SUNSTONE]>0:
                
                    inventory[SUNSTONE] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = SUNSTONE
                    inventory[currentTile] += 1
            if (event.key ==K_q):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[PUMPKIN]>0:
                
                    inventory[PUMPKIN] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = PUMPKIN
                    inventory[currentTile] += 1
            if (event.key ==K_w):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[FLOWER]>0:
                
                    inventory[FLOWER] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = FLOWER
                    inventory[currentTile] += 1
            if (event.key ==K_e):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[STOVE]>0:
                
                    inventory[STOVE] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = STOVE
                    inventory[currentTile] += 1

            if (event.key ==K_r):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[FIRE]>0:
                
                    inventory[FIRE] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = FIRE
                    inventory[currentTile] += 1

            if (event.key ==K_t):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[SECRET]>0:
                
                    inventory[SECRET] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = SECRET
                    inventory[currentTile] += 1
            if (event.key ==K_y):
                currentTile = tilemap[playerPos[1]][playerPos[0]]
                if inventory[SUM1]>0:
                
                    inventory[SUM1] -= 1
                    tilemap[playerPos[1]][playerPos[0]] = SUM1
                    inventory[currentTile] += 1

                    
                        
                            
                        

                        
            
            
            #hopefully this makes firedimond
            if pygame.mouse.get_pressed()[0]:
                if inventory[LAVA] >= craft[FIREDIMOND][LAVA] and inventory[DIMOND] >= craft[FIREDIMOND][DIMOND]:
                    if(event.key == K_9):
                        inventory[LAVA] -=2
                        inventory[DIMOND] -=1
                        inventory[FIREDIMOND] +=1
            if pygame.mouse.get_pressed()[0]:
                if inventory[STONE] >= craft[SUNSTONE][STONE] and inventory[FIREDIMOND] >= craft[SUNSTONE][FIREDIMOND]:
                    if(event.key == K_0):
                        inventory[STONE] -=1
                        inventory[FIREDIMOND] -=1
                        inventory[SUNSTONE] +=1
            if pygame.mouse.get_pressed()[0]:
                if inventory[DIRT] >= craft[PUMPKIN][DIRT] and inventory[GRASS] >= craft[PUMPKIN][GRASS] and inventory[WATER] >= craft[PUMPKIN][WATER]:
                    if(event.key == K_q):
                        inventory[DIRT] -=5
                        inventory[GRASS] -=1
                        inventory[WATER] -=1
                        inventory[PUMPKIN] +=1
            if pygame.mouse.get_pressed()[0]:
                if inventory[DIRT] >= craft[FLOWER][DIRT] and inventory[WATER] >= craft[FLOWER][WATER]:
                    if(event.key == K_w):
                        inventory[DIRT] -=1
                        inventory[WATER] -=1
                        inventory[FLOWER] +=1
            if pygame.mouse.get_pressed()[0]:
                if inventory[STONE] >= craft[STOVE][STONE]:
                    if(event.key == K_e):
                        inventory[STONE] -=2
                        inventory[STOVE] +=1

            if pygame.mouse.get_pressed()[0]:
                if inventory[LAVA] >= craft[FIRE][LAVA] and inventory[TREE] >= craft[FIRE][TREE]:
                    if(event.key == K_r):
                        inventory[LAVA] -=1
                        inventory[TREE] -=1
                        inventory[FIRE] +=1

            if pygame.mouse.get_pressed()[0]:
                if inventory[FIREDIMOND] >= craft[SECRET][FIREDIMOND] and inventory[SUNSTONE] >= craft[SECRET][SUNSTONE] and inventory[PUMPKIN] >= craft[SECRET][PUMPKIN]:
                    if(event.key == K_t):
                        inventory[FIREDIMOND] -=1
                        inventory[SUNSTONE] -=1
                        inventory[PUMPKIN]
                        inventory[SECRET] +=1


            
              
              
                
                
            
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]],(column*TILESIZE,row*TILESIZE))

    DISPLAYSURF.blit(PLAYER,(playerPos[0]*TILESIZE,playerPos[1]*TILESIZE))
    
    
    placePosition = 10

    if invo == True:
        for item in resources:
            DISPLAYSURF.blit(textures[item],(placePosition,MAPHEIGHT*40 + 5))

            placePosition += 10

            textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
            DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*40+5))
            placePosition += 50
    else:
         textObj = INVFONT.render('keys = dirt[1],grass[2],water[3],coal[4],lava[5],stone[6],dimond[7],tree[8],firedimond[9],sunstone[0],'
                                  'to craft place curser in screen, hold left click, press craft[key]',1,(WHITE))
         textObj2 = INVFONT.render('pumpkin[q],flower[w],stove[e],fire[r],secretbox[t]secretfunnbox[y]',1,(WHITE))
         
         DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT*40+5))
         DISPLAYSURF.blit(textObj2,(placePosition,MAPHEIGHT*40+25))
        
#resources = [DIRT,GRASS,WATER,COAL,LAVA,STONE,DIMOND,TREE,FIREDIMOND,SUNSTONE,PUMPKIN]
    
    
        

    DISPLAYSURF.blit(textures[CLOUD].convert_alpha(),(cloudx,cloudy))
    cloudx+=1
    if cloudx > MAPWIDTH*TILESIZE:
        cloudy = random.randint(0,MAPHEIGHT*TILESIZE)
        cloudx = -200


   
    DISPLAYSURF.blit(textures[BIRD].convert_alpha(),(birdx,birdy))
    birdx+=10
    
    if birdx > MAPWIDTH*TILESIZE:
        birdy = random.randint(0,MAPHEIGHT*TILESIZE)
        birdx = -10000

    DISPLAYSURF.blit((ENEMY.convert_alpha()),(enemyPos[0],enemyPos[1]))
    enemyPos[0] += 1
    
    if enemyPos[0] > MAPWIDTH*TILESIZE:
        enemyPos[1] = random.randint(0,MAPHEIGHT*TILESIZE)
        enemyPos[0] = -10
    if playerPos == [0,1]:
        DISPLAYSURF.blit(SAYINGHELLO,(enemyPos[0]+40,enemyPos[1]+10))
    
        
    if playerPos == [0,0] and SECRET == tilemap[0][0]:
        
        secretBlock = INVFONT.render('three blocks of fire surrounding [s/t] to summin a demon',1,(WHITE))
        DISPLAYSURF.blit(secretBlock,(enemyPos[0]+40,enemyPos[1]+10))
        #playerPos[0]*TILESIZE,playerPos[1]*TILESIZE
    if playerPos == [0,11]:
        DISPLAYSURF.blit(talk1,(playerPos[1],playerPos[1]))
    
     #SPECAIL EVENTS
    if tilemap[10][0] == FIRE and tilemap[10][1]== FIRE and tilemap[11][1]==FIRE:
        if event.type == KEYDOWN:
            if event.key == K_s:
        
        
                inventory[SUM1] = 99
        
                secret()
    if tilemap[10][0] == WATER and tilemap[10][1]== WATER and tilemap[11][1]==WATER:
        if event.type == KEYDOWN:
            if event.key == K_s:
                print('stuff')
        
        
    
    if tilemap[10][0] == FIRE and tilemap[10][1]== FIRE and tilemap[11][1]==FIRE:
        DISPLAYSURF.blit(birdTalk,(birdx,birdy))
        DISPLAYSURF.blit((SUM.convert_alpha()),(sumPos[0],sumPos[1]))
        sumPos[0] += 8
        if sumPos[0] > MAPWIDTH*TILESIZE:
            sumPos[1] = random.randint(0,MAPHEIGHT*TILESIZE)
            sumPos[0] = 0
    
    '''DISPLAYSURF.blit(textures[CLOUD2],(cloudxx,cloudyy))
    cloudxx+=4
    if cloudxx > MAPWIDTH*TILESIZE:
        cloudyy = random.randint(0,MAPHEIGHT*TILESIZE)
        cloudxx = -1000'''
    #tilemap[rw][cl] = tile

    '''player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    



        class enem(pygame.sprite.Sprite):
        image = pygame.image.load('enemy.png')
        image = image.convert_alpha()
        def __init__(self, startpos=(100,100)):
           pygame.sprite.Sprite.__init__(self,
                                  self.groups) 
           self.pos = startpos
           self.image = play.image 
           self.rect = self.image.get_rect()
        def update(self):
           self.rect.center = self.pos
       
    all_sprites.update()
    all_sprites.draw(DISPLAYSURF)'''
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
            pygame.image.save(DISPLAYSURF,"screenshot.png")
    pygame.display.flip()
    fpsClock.tick(24)

