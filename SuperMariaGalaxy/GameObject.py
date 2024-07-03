import pygame

class GameObject(object):
    def __init__(self,hitbox):
        self.hitbox=pygame.Rect(hitbox)
        self.screen=pygame.display.get_surface()
        self.color=(255,255,255)
        self.direction=[0,0]

        
        
    def draw(self):
         pygame.draw.rect(self.screen, self.color, self.hitbox, 0)
    
    def move(self):
        self.hitbox.move_ip(self.direction[0],self.direction[1])
    
    def update(self):
        self.move()
        self.draw()
        
    