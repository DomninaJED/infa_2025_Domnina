import pygame
from pygame.draw import *
import math

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
background = pygame.Surface((400, 400))
background.fill((255, 255, 255))

# Фон
rect(screen, (205, 133, 63), (0, 0, 600, 600))
rect(screen, (210, 180, 140), (0, 500, 600, 400))

# Окно
rect(screen, (135, 206, 250), (350, 100, 200, 300))
rect(screen, (139, 69, 19), (350, 100, 200, 300), 10)
rect(screen, (139, 69, 19), (350, 180, 200, 10))
rect(screen, (139, 69, 19), (445, 100, 10, 300))

# Кот хвост
s = pygame.Surface((200, 60), pygame.SRCALPHA, 32)
ellipse(s, (60, 60, 60), [0, 0, 200, 60])
ellipse(s, (0, 0, 0), [0, 0, 200, 60], 2)
s1 = pygame.transform.rotate(s, 135)
screen.blit(s1, (400, 525))


# Кот тело
ellipse(screen, (60, 60, 60), [100, 500, 350, 170])
ellipse(screen, (0, 0, 0), [100, 500, 350, 170], 2)

# Кот голова
circle(screen, (60, 60, 60), (130, 500), 70) 
circle(screen, (0, 0, 0), (130, 500), 70, 2) 

# Кот лапы
ellipse(screen, (60, 60, 60), [80, 590, 50, 100])
ellipse(screen, (0, 0, 0), [80, 590, 50, 100], 2)
ellipse(screen, (60, 60, 60), [120, 640, 100, 50])
ellipse(screen, (0, 0, 0), [120, 640, 100, 50], 2)

circle(screen, (60, 60, 60), (400, 640), 55) 
circle(screen, (0, 0, 0), (400, 640), 55, 2) 
ellipse(screen, (60, 60, 60), [410, 640, 50, 100])
ellipse(screen, (0, 0, 0), [410, 640, 50, 100], 2)


# Кот уши
polygon(screen, (60, 60, 60), [(70, 470), (90, 400), (120, 435)])
polygon(screen, (0, 0, 0), [(70, 470), (90, 400), (120, 435)], 2)

polygon(screen, (150, 150, 150), [(77, 463), (93, 407), (115, 435)])
polygon(screen, (0, 0, 0), [(75, 463), (91, 405), (115, 435)], 2)


polygon(screen, (60, 60, 60), [(190, 470), (170, 400), (140, 435)])
polygon(screen, (0, 0, 0), [(190, 470), (170, 400), (140, 435)], 2)

polygon(screen, (150, 150, 150), [(184, 461), (169, 409), (147, 435)])
polygon(screen, (0, 0, 0), [(184, 461), (168, 409), (145, 435)], 2)

# Кот глаза
circle(screen, (60, 179, 113), (100, 500), 20)
circle(screen, (0, 0, 0), (100, 500), 20, 2)

circle(screen, (60, 179, 113), (160, 500), 20)
circle(screen, (0, 0, 0), (160, 500), 20, 2)

ellipse(screen, (0, 0, 0), [100, 480, 10, 37])
ellipse(screen, (0, 0, 0), [160, 480, 10, 37])

# Кот хвост
s = pygame.Surface((200, 60), pygame.SRCALPHA, 32)
ellipse(s, (255, 255, 255), [0, 0, 5, 16])
s1 = pygame.transform.rotate(s, 65)
screen.blit(s1, (85, 310))

s = pygame.Surface((200, 60), pygame.SRCALPHA, 32)
ellipse(s, (255, 255, 255), [0, 0, 5, 16])
s1 = pygame.transform.rotate(s, 65)
screen.blit(s1, (145, 310))

# Кот морда
polygon(screen, (0, 0, 0), [(140, 525), (120, 525), (130, 535)])
rect(screen, (0, 0, 0), (130, 535, 1, 10))

arc(screen, (0, 0, 0), [130, 535, 20, 20], math.pi, 2*math.pi, 1)
arc(screen, (0, 0, 0), [110, 535, 20, 20], math.pi, 2*math.pi, 1)

arc(screen, (0, 0, 0), [160, 525, 80, 10], 0, math.pi, 1)
arc(screen, (0, 0, 0), [160, 530, 80, 10], 0, (math.pi), 1)
arc(screen, (0, 0, 0), [160, 535, 80, 10], 0, (math.pi), 1)

arc(screen, (0, 0, 0), [20, 525, 80, 10], 0, (math.pi), 1)
arc(screen, (0, 0, 0), [20, 530, 80, 10], 0, (math.pi), 1)
arc(screen, (0, 0, 0), [20, 535, 80, 10], 0, (math.pi), 1)

# Клубок
circle(screen, (139, 0, 0), (300, 740), 50)
circle(screen, (0, 0, 0), (300, 740), 50, 2)

arc(screen, (0, 0, 0), [310, 700, 30, 70], 3*math.pi/2, 2*math.pi, 1)
arc(screen, (0, 0, 0), [295, 710, 30, 70], 3*math.pi/2 + 0.2, 2*math.pi + 0.2, 1)
arc(screen, (0, 0, 0), [300, 740, 10, 40], 3*math.pi/2 + 0.5, 2*math.pi + 0.8, 1)
arc(screen, (0, 0, 0), [270, 705, 50, 40], 3*math.pi/2 + math.pi/2, 2*math.pi + math.pi/2, 1)
arc(screen, (0, 0, 0), [260, 710, 50, 40], 3*math.pi/2 + math.pi/2 + 0.5, 2*math.pi + math.pi/2 + 0.5, 1)

arc(screen, (0, 0, 0), [280, 740, 30, 70], math.pi/2, math.pi, 1)
arc(screen, (0, 0, 0), [270, 720, 50, 70], math.pi/2 + 0.5, math.pi + 0.2, 1)

x = 10
y = 720
arc(screen, (139, 0, 0), [x, y, 100, 50], 0, math.pi, 1)
arc(screen, (139, 0, 0), [x + 100, y, 100, 50], math.pi, 2*math.pi, 1)
arc(screen, (139, 0, 0), [x + 200, y, 100, 50], 0, math.pi, 1)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()