import pygame
from sets import *



class Loop:
    def __init__(self,times_run):
        self.run = times_run
        
        self.count = 0
    def play(self):
        if self.run >= self.count:
            return True
        else:
            return False
        self.count +=1
        
        
