
import argparse

import os
import sys

import pygame
import time
####
pygame.init()

####
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
dis_width = 800
dis_height = 600

snake_block = 10
snake_speed = 30

######

dis=pygame.display.set_mode((dis_width,dis_height))
# pygame.display.update()
pygame.display.set_caption('snake')


game_over = False

x1 = dis_width/2
y1 = dis_height/2

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None,50)

def message(msg,color):
    mesg = font_style.render(msg,True,color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            game_over = True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x1_change=-snake_block
                y1_change=0
            if event.key==pygame.K_RIGHT:
                x1_change=snake_block
                y1_change=0
            if event.key==pygame.K_UP:
                x1_change=0
                y1_change=-snake_block
            if event.key==pygame.K_DOWN:
                x1_change=0
                y1_change=snake_block
    
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True
    
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis,black,[x1,y1,snake_block,snake_block])
    # pygame.draw.rect(dis,red,[100,100,10,10])
    pygame.display.update()
    clock.tick(snake_speed)

message("You Lost",red)
pygame.display.update()
time.sleep(2)

pygame.quit()

quit()


####

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument ('--id', type=str, default='anonymous', help='id')
    parser.add_argument ('--file', type=str, default='file.txt', help='file')
    args = parser.parse_args()

print(args.id+args.file)
# print(args.file)

