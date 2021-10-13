
import argparse

import os
import sys

import pygame

####
pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

dis=pygame.display.set_mode((800,600))
# pygame.display.update()
pygame.display.set_caption('snake')

x1 = 300
y1 = 300
x1_change = 0
y1_change = 0

clock = pygame.time.Clock()


game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            game_over = True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x1_change=-10
                y1_change=0
            if event.key==pygame.K_RIGHT:
                x1_change=10
                y1_change=0
            if event.key==pygame.K_UP:
                x1_change=0
                y1_change=-10
            if event.key==pygame.K_DOWN:
                x1_change=0
                y1_change=10
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis,black,[x1,y1,10,10])
    # pygame.draw.rect(dis,red,[100,100,10,10])
    pygame.display.update()
    clock.tick(30)

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

