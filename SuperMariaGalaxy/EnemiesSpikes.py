import pygame
from GameObject import *
width,height=30,40
images=[
       pygame.transform.scale(pygame.image.load("16_bit_spike_Sheet1.png"),(width,height))
        ]
    
class spikes(GameObject):
    
    def __init__(self,x,y):
        super().__init__((x,y,width,height))
        self.layer=2
        self.color=(0,0,255)
        self.drop=1
        self.image=0

        
        
    def draw(self):
        self.screen.blit(images[self.image], self.hitbox)

