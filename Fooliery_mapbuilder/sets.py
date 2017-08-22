import pygame
import random

wth = 500
hgt = 500
fps = 60

title = 'my game'
icon = 'gameicon'#this takes a image name

#my fav (rgb) colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
lightred = (255,25,25)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
lightblue = (0,155,155)
grey = (80,80,80)
lightgrey = (100,100,100)
darkgrey = (40,40,40)
blurple = (90,90,255)
pink = (255,90,255)
hotpink = (255,50,90)
lime = (0,255,90)
peach = (255,255,90)
pumpkin = (255,190,40)
junglegreen = (100,200,40)
purple = (255,0,255)

all_color_list = [black ,
        white,
        red ,
        lightred ,
        green ,
        blue ,
        yellow,
        lightblue,
        grey,
        lightgrey ,
        darkgrey ,
        blurple ,
        pink ,
        hotpink ,
        lime  ,
        peach  ,
        pumpkin ,
        junglegreen,
        purple ]

#Ive defined some extras in this framework---remember these or only sugestions ;)

backround_color = hotpink

color_fun = random.choice([all_color_list])



