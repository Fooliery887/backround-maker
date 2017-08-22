import pygame
import random
from Scene import *
from sets import *

pygame.init()
#images path go here

class Buttons(pygame.sprite.Sprite):
    def __init__(self,game,img_default,img_hover,img_clicked,Xpos,Ypos,scene = None):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.s = scene
        self.img_d = img_default
        self.img_h = img_hover
        self.img_c = img_clicked
        self.size = (self.game.tilesize,self.game.tilesize)
        self.image = pygame.image.load(self.img_d).convert()
        self.image = pygame.transform.scale(self.image,self.size)
        self.rect = self.image.get_rect()
        self.rect.x = Xpos
        self.rect.y = Ypos
        self.rect.midtop = (Xpos,Ypos)
        self.clicked = False
        self.hover = False
        self.follow = False

        self.button_bool = True
    def update(self):
        self.hits_v_1()
        if self.follow:
            self.rect.x,self.rect.y = self.game.mpos
		
    def hits_v_1(self):
        if self.rect.x +self.rect.width > self.game.mpos[0] > self.rect.x and self.rect.y + self.rect.height > self.game.mpos[1] > self.rect.y:
            #print('woot woot')
            self.hover = True
            if not self.clicked:
                self.image = pygame.image.load(self.img_h)
                self.image = pygame.transform.scale(self.image,self.size)
            if self.clicked:
                self.image = pygame.image.load(self.img_c)
                self.image = pygame.transform.scale(self.image,self.size)
          
        else:
            self.hover = False
            if not self.clicked:
                self.image = pygame.image.load(self.img_h)
                self.image = pygame.transform.scale(self.image,self.size)
            if self.clicked:
                self.image = pygame.image.load(self.img_c)
                self.image = pygame.transform.scale(self.image,self.size)

    def drag_drop(self):
        if self.hover:
            if self.clicked:
                self.follows = True
        else:
            self.follows = False
    def button_scene(self):
        if self.clicked:
            self.s.button_page_turner()
            self.button_bool = False
        if not self.button_bool:
            self.game.screen.blit(self.s.image,(self.s.x,self.s.y))
    def button_events_mousedown(self,button_id):
        self.button = button_id
        
        #print('mouse button down at ' + str(self.game.mpos ))
        if self.button.hover:
            print('clicked')
            self.button.clicked = True
            #self.button1.follow = True
        else:
            self.button.clicked = False
            #self.button1.follow = False
    def button_events_mouseup(self,button_id):
        
        self.button = button_id
        self.button.clicked = False
    def button_is_clicked(self,button_id):
        self.button = button_id
        
        #print('mouse button down at ' + str(self.game.mpos ))
        if self.button.hover:
            #print('clicked')
            return True
        else:
            #print('miss')
            return False
    
    def button_is_unclicked(self,button_id):
        
        self.button = button_id
        self.button.clicked = False
    
            
            
        
        
        
