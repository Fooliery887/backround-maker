import pygame
import random
from sets import *
from pause import *

pygame.init()
tv = [pygame.image.load('Images/keep/tv1.jpg'),
      pygame.image.load('Images/keep/tv2.jpg'),
      pygame.image.load('Images/keep/tv3.jpg'),
      pygame.image.load('Images/keep/tv4.jpg'),
      pygame.image.load('Images/keep/tv5.jpg'),
      pygame.image.load('Images/keep/tv6.jpg'),
      pygame.image.load('Images/keep/tv7.jpg'),
      pygame.image.load('Images/keep/tv8.jpg')]
craft = []


class Scene: #this is primarery used for backround animation , or whole screen animation
    def __init__(self,game,animation_list,tile_size = 30):
        self.game = game
        self.tile_size = self.game.tilesize
        self.size = (self.game.tilesize,self.game.tilesize)
        self.last_update = 0
        self.last_update2 = 0
        self.current_frame = 0
        self.did_loop = 0
        self.p = Pause
        self.list = animation_list
        print('scene test' + str(self.list))
        self.last_in_list = len(self.list) -1
        self.re_image = self.last_in_list
        self.did_run = False
        self.did_run_e = False
        self.frame_update = 0
        #more init stuff
        self.go = True
        self.e1 = 100
        self.do_p = True
        self.angle = 0
        self.shrinkx = wth
        self.shrinky = hgt
        self.done_s = False
        self.ux = 0
        self.uy = 0
    def page_turner(self,times_loop = 1,scenex=0,sceney=0,fit_to_screen = True,built_in_effect = 1):
        self.scenex = scenex
        self.sceney = sceney
        if self.go:
            now = pygame.time.get_ticks()
            if now - self.last_update > 10:
                self.last_update = now
                if not self.did_run:
                    #print('frame 0')
                    self.frame_update += 1
                    self.image = self.list[0]
                    if fit_to_screen:
                        self.image = pygame.transform.scale(self.image,(wth,hgt))
                    if self.frame_update > 1:
                        self.did_run = True
                if self.did_run:
                    self.current_frame = (self.current_frame+1) % len(self.list)
                    #Pause.see_thru_pause(self)
                    self.image = self.list[self.current_frame]
                    if fit_to_screen:

                        self.image = pygame.transform.scale(self.image,(wth,hgt))
                    if self.do_p:
                        self.p.see_thru_pause(self)
                    #print(str(self.current_frame))
                    if self.current_frame == len(self.list) - 1:
                        self.did_loop += 1
                        #print('time it looped is ' + str(self.did_loop))
                        #self.current_frame = 0
                    
                    
            if self.did_loop < times_loop:
                
                
                self.game.screen.blit(self.image,(self.scenex,self.sceney))
            elif self.did_loop >= times_loop:
                if built_in_effect == 1:
                    self.do_p = False
                    now = pygame.time.get_ticks()
                    if now - self.last_update2 > 5:
                        self.last_update = now
                        self.Spin_out_end_effect()
                        self.ux += 5
                        self.uy += 5
                        
                    if self.go:
                        
                        self.game.screen.blit(self.image,(self.ux,self.uy))
                
    def running(self,time=1,scenex=0,sceney=0,fit_to_screen = True, use_tiles = False,tile_size = None):
        self.tile_size = self.game.tilesize
        
        now = pygame.time.get_ticks()
        if now - self.last_update > time:
            self.last_update = now
            #print(str(self.current_frame))
            
                
            
            if not self.did_run:
                
                self.image = self.list[0]
                if fit_to_screen:
                    self.image = pygame.transform.scale(self.image,(wth,hgt))
                if use_tiles:
                    self.image = pygame.transform.scale(self.image,self.size)
                self.frame_update += 1
                if self.frame_update > 0:
                    self.did_run = True
            else:
                self.current_frame = (self.current_frame+1) % len(self.list)
                self.image = self.list[self.current_frame]
                if fit_to_screen:
                    self.image = pygame.transform.scale(self.image,(wth,hgt))
                if use_tiles:
                    self.image = pygame.transform.scale(self.image,self.size)
            if self.current_frame == len(self.list):
                self.current_frame = 0
        self.game.screen.blit(self.image,(scenex,sceney))
    def button_page_turner(self,scenex=0,sceney=0,fit_to_screen = True):
        self.x = scenex
        self.y = sceney
        self.did_run = False
        if not self.did_run:
            if not self.did_run_e:
                self.image = self.list[0]
                if fit_to_screen:
                    self.image = pygame.transform.scale(self.image,(wth,hgt))
            else:
                self.current_frame = (self.current_frame + 1) % len(self.list)
                self.image = self.list[self.current_frame]
                if fit_to_screen:
                    self.image = pygame.transform.scale(self.image,(wth,hgt))

        #self.game.screen.blit(self.image,(scenex,sceney))
        self.did_run_e = True
        self.did_run = True            
        self.game.button1.clicked = False
    def button_running(self):
        pass
    
    def Spin_out_end_effect(self,spin = 100, test = True):
        #add this to your code in update after you call a page_turner
        #in new()
        #this will make the last image do a special effect - spin and shrink -
        self.angle += 1
        self.shrinkx -=10
        self.shrinky -= 10
        
        aa = 1
        #print('effect has run ')
        #print('angle is ' + str(aa))
        if self.go:
            self.image  = pygame.transform.rotate(self.image, self.angle)
            self.image = pygame.transform.scale(self.image,(self.shrinkx,self.shrinky))
            
            #print(str(self.scenex)+ '   ' +str(self.sceney))
        if self.shrinkx < 1:
            self.shrinkx = 1
            self.go = False
            
        if self.shrinky < 1:
            self.shrinky = 1
            self.go = False
        #self.image  = self.re_image = pygame.transform.rotate(self.image, aa)
        #self.image = pygame.transform.scale(self.image,(wth + 5,hgt + 5))
        #self.iamge = self.re_image = pygame.transform.scale(self.image,(wth + 5,hgt + 5 ))
    def make_tile_from_list(self,use_index):
        
        self.image = [use_index]
        #print(str(self.list))
        
        self.image = pygame.transform.scale(self.image,self.size)
        print('image returned')
        return self.image
class Surf(pygame.sprite.Sprite):
    def __init__(self,game,image,x,y,width = 30,hieght = 30):
        pygame.sprite.Sprite.__init__(self)
        
        self.game = game
        width = self.game.tilesize
        height = self.game.tilesize
        self.size = (width,hieght)
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.blit(image,(0,0))
        self.re_image = image
    def update(self):
        self.image = pygame.transform.scale(self.image,(self.game.tilesize,self.game.tilesize))
        self.image.blit(self.re_image,(0,0))
class Surf2(pygame.sprite.Sprite):
    def __init__(self,game,image,x,y,width = 300,hieght = 300):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.size = (width,hieght)
        self.image = pygame.Surface(self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.blit(image,(0,0))
        self.re_image = image
    def update(self):
        if self.game.drawgrid == False:
            self.image.blit(self.re_image,(0,0))
            self.game.all_sprites.draw(self.image)
class bug_fix1:
    pass
    
        
