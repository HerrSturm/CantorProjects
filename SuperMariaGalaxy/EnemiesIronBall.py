import pygame
from GameObject import *
width,height=40,40
images=[
    pygame.transform.scale(pygame.image.load("Enemy_IronBall1.png"),(width,height)),
    pygame.transform.scale(pygame.image.load("Enemy_IronBall2.png"),(width,height)),
    pygame.transform.scale(pygame.image.load("Enemy_IronBall3.png"),(width,height)),
    pygame.transform.scale(pygame.image.load("Enemy_IronBall4.png"),(width,height)),
    pygame.transform.scale(pygame.image.load("Enemy_IronBall5.png"),(width,height)),
    pygame.transform.scale(pygame.image.load("Enemy_IronBall6.png"),(width,height)),
    pygame.transform.scale(pygame.image.load("Enemy_IronBall7.png"),(width,height)),
    pygame.transform.scale(pygame.image.load("Enemy_IronBall8.png"),(width,height))
        ]
    
class IronBall(GameObject):
    
    def __init__(self,x,y):
        super().__init__((x,y,width,height))
        self.layer=2
        self.color=(0,0,255)
        self.direction=[4,0]
        self.hp=3
        self.drop=1
        self.stop=[100,700]
        self.image=0
        self.cnt=0
        
        
    
    def move(self):
        super().move()
        self.cnt+=1
        if(self.direction[0]>0 and self.cnt>=2):
            self.image+=1
            self.cnt=0
            if(self.image>=7):
                self.image=0
        
        if(self.direction[0]<0 and self.cnt>=2):
            self.image-=1
            self.cnt=0
            if(self.image<=0):
                self.image=7
                
        if(self.hitbox.x+self.hitbox.width>=self.stop[1]):
            self.direction[0]*=-1
        
        if(self.hitbox.x<=self.stop[0]):
            self.direction[0]*=-1
    
    def draw(self):
        self.screen.blit(images[self.image], self.hitbox)
