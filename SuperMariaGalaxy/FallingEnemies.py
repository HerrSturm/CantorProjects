
import pygame, random
from GameObject import *
[width1, height1] = [30, 40]
[width2, height2] = [40, 40]
bomb = [
        pygame.transform.scale(pygame.image.load("bomb1.png"),(width1, height1)),
        pygame.transform.scale(pygame.image.load("bomb2.png"),(width1, height1)),
        pygame.transform.scale(pygame.image.load("bomb3.png"),(width1, height1)),
        pygame.transform.scale(pygame.image.load("bomb4.png"),(width1, height1)),
        pygame.transform.scale(pygame.image.load("bomb5.png"),(width1, height1)),
        pygame.transform.scale(pygame.image.load("bomb6.png"),(width1, height1)),
        pygame.transform.scale(pygame.image.load("explosion1.png"),(width2, height2)),
        pygame.transform.scale(pygame.image.load("explosion2.png"),(width2, height2)),
        pygame.transform.scale(pygame.image.load("explosion3.png"),(width2, height2)),
        pygame.transform.scale(pygame.image.load("explosion4.png"),(width2, height2)),
        pygame.transform.scale(pygame.image.load("explosion5.png"),(width2, height2)),
        pygame.transform.scale(pygame.image.load("explosion6.png"),(width2, height2)),
        pygame.transform.scale(pygame.image.load("explosion7.png"),(width2, height2)),
        pygame.transform.scale(pygame.image.load("explosion8.png"),(width2, height2))
        ]

class FallingEnemies(GameObject):
    
    def __init__(self,hitbox,stop,respawnTime = 0):
        super().__init__(hitbox)
        self.stop=stop
        self.layer=2
        self.color=(0,0,255)
        self.direction=[0,3]
        self.hp=3
        self.drop=1
        self.image=0
        self.cnt = 0
        self.paused = True
        self.respawnTime = respawnTime
        
    def move(self):
        if not(self.paused):
            if (self.hitbox.y + self.hitbox.height <= self.stop):
                self.hitbox.move_ip(self.direction[0],self.direction[1])
                self.image+=1
                if (self.image >= 5):
                    self.image = 0
            if (self.hitbox.y + self.hitbox.height >= self.stop and self.image <= 12):
                self.image+=1
            if (self.image>=13):
                self.hitbox.y=0
                self.paused = True
        else:
            if self.cnt == self.respawnTime:
                self.cnt = 0
                self.paused = False
            else:
                self.cnt += 1
        
    def draw(self):
        self.screen.blit(bomb[self.image], self.hitbox)


        
    def draw(self):
        self.screen.blit(bomb[self.image], self.hitbox)
