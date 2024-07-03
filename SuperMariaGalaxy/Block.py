import sys, pygame
from GameObject import *


class Block(GameObject):

    blockimg = pygame.image.load("images/block/blueblock.png")
    transformedimg = pygame.transform.scale(blockimg, (20, 20))
        
    def __init__(self,hitbox):
        super().__init__(hitbox)
        self.color = (50,255,50)
        self.layer = 1
        self.onGround = False
        

        
    def draw(self):
        #pygame.draw.rect(self.screen, self.color, self.hitbox, 0)
        skalar = self.hitbox[2] // 20
        for i in range (skalar):
            self.screen.blit(self.transformedimg, (self.hitbox[0] + i * 20, self.hitbox[1]))
    

    
