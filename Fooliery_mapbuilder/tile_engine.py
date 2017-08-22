import pygame
import random
from sets import *
from misc import *
from Scene import *


class Map:
    def __init__(self,filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line)

        self.tilewht = len(self.data[0])
        self.tilehgt = len(self.data)
        self.wth = self.tilewht * tilesize
        self.hgt = self.tilehgt * tilesize
        
class Grid:
    def __init__(self,game,tile_size = 30,txt_file = None):
        self.game = game
        tile_size = self.game.tilesize
        self.tile_size = self.game.tilesize
        self.txt_file = txt_file
        try:
            self.framing1 = txt_file
        except:
            pass
        # seperater
        self.xlist = []
        self.ylist = []

        self.filler = []
        self.filler_holder = []
        
    def draw_grid(self):

        for i in range(0,wth + self.tile_size // 2,self.tile_size):
            pygame.draw.line(self.game.back_of.image,blue,(i,0),(i,hgt))
        for i in range(0,hgt + self.tile_size // 2,self.tile_size):
            pygame.draw.line(self.game.back_of.image,black,(0,i),(wth,i))

    def create_grid_cords(self):

        for i in range(0,wth,self.tile_size):
            x = i
            self.xlist.append(x)
        for i in range(0,hgt,self.tile_size):
            y = i
            self.ylist.append(y)
    def mouse_to_grid_check(self):
         self.check = True
         for row in self.xlist:#this is the x of the q
             for col in self.ylist:#this is the y of the q
                 if row +self.game.tilesize > self.game.mpos[0] > row and col + self.game.tilesizes > self.game.mpos[1] > col:
                    self.r = row
                    self.c = col
    def print_mousepos_grid(self):
        
        #print(self.r // self.tile_size,self.c // self.tile_size)
        pass
    
    def color_a_block_with_click(self):
        
        self.filler.append((self.r,self.c,self.tile_size,self.tile_size))
        #print(self.filler)

    def fill(self,color):
        for i in self.filler:
            pygame.draw.rect(self.game.screen,color,i)
    def test_blocks(self,color,length_x,length_y,total,block_x,block_y,fill = False):
        
        
        for i in range(total):
            if not fill:
                pygame.draw.rect(self.game.screen,color,(block_x * self.tile_size,block_y * self.tile_size,self.tile_size,self.tile_size),5)
                block_x += length_x
                block_y += length_y
            else:
                pygame.draw.rect(self.game.screen,color,(block_x * self.tile_size,block_y * self.tile_size,self.tile_size,self.tile_size))
                block_x += length_x
                block_y += length_y
    
            
        
        
class Wall(pygame.sprite.Sprite):


    def __init__(self,game, x, y,tile_size ,img = None, color = white, does_collide = False,collider_group = None,do_kill = False):
        """ Constructor function """
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        tilesize = self.game.tilesize
        self.tile_size = tile_size
        # Make a BLUE wall, of the size specified in the parameters
        if img == None:
            self.image = pygame.Surface((self.tile_size,self.tile_size))
            self.image.fill(color)
            self.color = color
        else:
            try:
                self.image = pygame.image.load(img)
                self.image = pygame.transform.scale(self.image,(self.tile_size,self.tile_size))
                self.game.back_of.blit(self.image,(x,y))
                #print('back_of')
                try:
                    self.game.back_of.re_image.blit(self.image,(x,y))
                    
                except:
                    pass
            except:
                self.image = pygame.Surface((self.tile_size,self.tile_size))
                self.image.fill(color)
                self.color = color
                self.game.back_of.blit(self.image,(0,0))
                
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.y = self.y * self.tile_size
        self.rect.x = self.x * self.tile_size
        self.do_collide = does_collide
        self.collider_group = collider_group
        self.wallx = self.rect.x
        self.wally = self.rect.y
    def update(self):
        if self.do_collide:
            hits = pygame.sprite.spritecollide(self,self.collider_group,Bool)
            if hits:
                #print('wall has had a collizion')
                pass
  

 
class build_wall:
    def __init__(self,game, x, y,x_to,y_to,length,tile_size = 30,img = None,color = black,does_collide = False,collider_group = None,do_kill = False):
        self.game = game
        tilesize = self.game.tilesize
        endx = 0
        endy = 0
        self.img = img
        for i in range(length):
            if self.img == None:
                w = Wall(self.game,x,y,tile_size,None,color)
            else:
                try:
                    w = Wall(self.game,x,y,tile_size,self.img)
                except:
                    w = Wall(self.game,x,y,tile_size,None,color)
                
            self.game.all_sprites.add(w)
            if endx < x_to:
                endx +=1
                x += 1
            if endy < y_to:
                endy += 1
                y += 1
class build_with_click:
    def __init__(self,game,tilesize=30,scene = None):
        self.game = game
        self.s = scene
        tilesize = self.game.tilesize
        self.tile_size = tilesize
        self.xlist = []
        self.ylist = []

        self.filler = []
        self.filler_holder = []

        self.var_for_fill = 0
        for i in range(0,wth,self.tile_size):
            x = i
            self.xlist.append(x)
            
        for i in range(0,hgt,self.tile_size):
            y = i
            self.ylist.append(y)
        #print(self.xlist)
        #print(self.ylist)
    def update(self):
        
        #print('updateing....')
        for row in self.xlist:#this is the x of the q
             for col in self.ylist:#this is the y of the q
                 if row +self.tile_size > self.game.mpos[0] > row and col + self.game.tilesize > self.game.mpos[1] > col:
                    self.r = row // self.game.tilesize
                    #print('getting erritated...')
                    self.c = col // self.game.tilesize
                    #print(self.r // self.tile_size,self.c//self.tile_size)

    def place_tile_sprite(self,img = None, color = green):
        self.update()
        self.tile_size = self.game.tilesize
        if self.game.click_check:
            if self.s == None:
                #print('appending to filler at ' + str(self.r),str(self.c))
                w = Wall(self.game,self.r,self.c,self.tile_size,self.game.aa)
                self.game.all_sprites.add(w)
                #print(self.game.all_sprites)
            else:
                
                #print('next')
                s = self.s
                self.filler.append(s)
                
            #print(self.filler)
            
            #self.game.all_sprites.add(w)
            #self.game.all_sprites.draw(self.game.screen)
            #print(self.filler)
    def fill(self,image = 0):
        
        if self.game.click_check:
            if self.s == None:
                for i in self.filler:
                    #print(i)
                    self.game.all_sprites.add(self.w)
            else:
                #print('fill')
                ax = self.r
                ay = self.r
                x  = self.r * self.game.tilesize
                y = self.c * self.game.tilesize
                
                self.update()
                self.view = pygame.image.load(craft[self.game.mousefill_image])
                print(str(craft[self.game.mousefill_image]))
                self.view = pygame.transform.scale(self.view,(self.game.tilesize,self.game.tilesize))
                print('self.game.tilesize')
                print(str(self.game.tilesize))
                #self.filler[self.var_for_fill].running(5,x,y,False,True)
                surf = Surf(self.game,self.view,x,y)
                self.game.all_sprites.add(surf)
                #self.game.back_of.image.blit(surf.image)
                self.var_for_fill += 1
                #print(self.r,self.c)
            
            self.game.click_check = False

