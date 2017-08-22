import pygame
import random
from sets import *

class Sheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename)
        self.rando = random.randrange(1, 10)
        self.rando2 = random.randrange(1, 3)
        
    #each appendage will scale image accordingly,
    #get_image10, allows for you to import the scale yourself
    def get_image(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (w * 2, h * 2))
        return image

    def get_image2(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (w // 4, h // 4))
        return image

    def get_image3(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        return image

    def get_image4(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (w // self.rando, h // self.rando))
        return image

    def get_image5(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (w * self.rando2, h * self.rando2))
        return image

    def get_image6(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        return image

    def get_image7(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (w * 2, w * 2))
        return image

    def get_image8(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (w // 2, h // 2))
        return image
    def get_image9(self, x, y, w, h):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (w * 2, h))
        return image
    def get_image10(self,x,y,w,h,scale_width,scale_hieght):
        image = pygame.Surface((w, h))
        image.blit(self.sheet, (0, 0), (x, y, w, h))
        image = pygame.transform.scale(image, (scale_width,scale_height))
        return image

