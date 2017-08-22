import pygame
import random
from sets import *
from sheet import *
pygame.init()


class Make_sprite(pygame.sprite.Sprite):
    
    def __init__(self,game,x,y,go = False):
        pygame.sprite.Sprite.__init__(self)
        self. go = go
        self.game = game
        
        #self.sqr = sqr 
        
        self.image = pygame.image.load('images/Magic_button_grey.png')
        self.re_image = self.image
        self.rect = self.image.get_rect()
        
        self.w = self.rect.width
        self.h = self.rect.height
        self.rect.center = (x,y)
        self.sqr = pygame.Surface((20,20))
        self.image.blit(self.sqr,(self.rect.width // 2, self.rect.height // 2))

        #init stuff here
       
        self.current_frame = 0
        self.last_update = 0
        
    def Spin_death(self,angle = 1,spin = 100, test = True):
        if not self.go:
            
            self.image  = pygame.transform.rotate(self.image, angle + 1)
            self.image  = self.re_image = pygame.transform.rotate(self.image, angle)
            self.image = pygame.transform.scale(self.image,(self.w + 5,self.h + 5))
            self.iamge = self.re_image = pygame.transform.scale(self.image,(self.w + 5,self.h + 5 ))
            if not test:
                self.go = True
        
    def update(self):
        pass
        #if self.go:
            #self.Angle()
        


        
