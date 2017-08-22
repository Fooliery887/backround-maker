import pygame
import random
from sets import *


class Text:
    def __init__(self,game):
        self.game = game
        self.renders()
    def draw_text(self,font, text, size,color,x,y):
        #standered text to screen, flexable
        font = pygame.font.Font(font, size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.game.screen.blit(text_surface, text_rect)
        
    def draw_text2(self,font, text,color,x,y):
        #less flexable way to text to screen
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.game.screen.blit(text_surface, text_rect)
        
    def draw_text3(self,font,text,size,color,x,y):
        #the paced in pos is top left allowing for user to line up each line
        font = pygame.font.Font(font,size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x,y)
        self.game.screen.blit(text_surface,text_rect)
    def renders(self):
        self.default = pygame.font.Font(None,40)
    def ask(self,question):
        word=""
        Text(self.game).draw_text2(self.default,question,green,wth//2,50) #example asking name
        pygame.display.flip()
        done = True
        while done:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        word+=str(chr(event.key))
                    if event.key == pygame.K_b:
                        word+=chr(event.key)
                    if event.key == pygame.K_c:
                        word+=chr(event.key)
                    if event.key == pygame.K_d:
                        word+=chr(event.key)
                    if event.key == pygame.K_RETURN:
                        done=False
                    #events...
        return Text(self.game).draw_text2(self.default,word,green,wth//2,100)
