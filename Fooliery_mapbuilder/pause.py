import pygame
import random
from sets import *

class Pause:
    def __init__(self):
        self.running = True
    def see_thru_pause(self):
        self.running = True
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.KEYUP:
                    self.running = False
            #pygame.display.flip()
    def black_out_pause(self,game):
        while self.running:
            game.screen.fill(black)
            for e in pygame.event.get():
                if e.type == pygame.KEYUP:
                    self.running = False
            pygame.display.flip()
            
            
