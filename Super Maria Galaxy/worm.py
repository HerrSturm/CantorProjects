import pygame
from GameObject import *
width,height= 20, 20

wormrunleftimg =[pygame.image.load("images/worm/wormrunleft1.png"), pygame.image.load("images/worm/wormrunleft2.png")]
wormrunrightimg =[pygame.image.load("images/worm/wormrunright1.png"), pygame.image.load("images/worm/wormrunright2.png")]
wormturnleftimg = pygame.image.load("images/worm/wormturnleft.png")
wormturnrightimg = pygame.image.load("images/worm/wormturnright.png")

wormruncounter = 1
tickcounter = 0
class Worm(GameObject):
    
    def __init__(self,x,y):
        super().__init__((x,y,width,height))
        self.direction=[0,0]
        self.stop=[300,700]
        self.image=0
        self.cnt=0
        
    def draw(self):
        
        global tickcounter
        tickcounter +=1
    
        global wormruncounter
        if wormruncounter < 25:                
            #wormruncounter += 1
            self.hitbox[0] -= 3
            self.screen.blit(wormrunleftimg[wormruncounter % 2],self.hitbox)
            if tickcounter >= 10:
                tickcounter = 0
                wormruncounter +=1
                 
        if wormruncounter == 25:
            self.screen.blit(wormturnleftimg,self.hitbox)
            if tickcounter >= 10:
                tickcounter = 0
                wormruncounter +=1
                        
        if wormruncounter > 25:             
            # wormruncounter += 1
            self.hitbox[0] += 3
            self.screen.blit(wormrunrightimg[wormruncounter % 2],self.hitbox)
            if tickcounter >= 10:
                tickcounter = 0
                wormruncounter +=1

        if wormruncounter == 49:
            self.screen.blit(wormturnrightimg,self.hitbox)
            wormruncounter = 1
            if tickcounter >= 10:
                tickcounter = 0
                wormruncounter +=1

                   
               
        print(wormruncounter)