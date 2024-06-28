import pygame
from GameObject import *

standimg = pygame.image.load("images/playergraphics/stehen1.png")
startrunimg= pygame.image.load("images/playergraphics/laufenstart.png")
runimg = [pygame.image.load("images/playergraphics/laufen1.png"),pygame.image.load("images/playergraphics/laufen2.png"),pygame.image.load("images/playergraphics/laufen3.png"),pygame.image.load("images/playergraphics/laufen4.png"),pygame.image.load("images/playergraphics/laufen5.png"),pygame.image.load("images/playergraphics/laufen6.png"),pygame.image.load("images/playergraphics/laufen7.png"),pygame.image.load("images/playergraphics/laufen8.png"),pygame.image.load("images/playergraphics/laufen9.png"),pygame.image.load("images/playergraphics/laufen10.png")]
runleftimg = []
for i in runimg:
    leftimg= pygame.transform.flip(i, True, False)
    runleftimg.append(leftimg)
stoprunimg= [pygame.image.load("images/playergraphics/laufenstop1.png"),pygame.image.load("images/playergraphics/laufenstop2.png"),pygame.image.load("images/playergraphics/laufenstop3.png")]
jumpimg = [pygame.image.load("images/playergraphics/jump1.png"),pygame.image.load("images/playergraphics/jump2.png"),pygame.image.load("images/playergraphics/jump3.png"),pygame.image.load("images/playergraphics/jump4.png"),pygame.image.load("images/playergraphics/jump5.png"),pygame.image.load("images/playergraphics/jump6.png")]
runimgcounter = 0
runleftimgcounter = 0
tickcounter = 0
jumpimgcounter = 0

class Player(GameObject):
    
    def __init__(self,hitbox, joystick):
        super().__init__(hitbox)      
        self.direction = [3,0]
        self.layer = 3
        self.onGround = False

        self.jump = 0
        self.fall = 3
        self.joystick = joystick

    def draw(self):
        keys = pygame.key.get_pressed()
        global tickcounter
        tickcounter +=1
        js_axis_0 = self.joystick.get_axis(0)
        if keys[pygame.K_SPACE] or self.joystick.get_button(3) or not(self.onGround):
            global jumpimgcounter
            self.screen.blit(jumpimg[jumpimgcounter],(self.hitbox.x-12,self.hitbox.y))
            if tickcounter >= 5:
                tickcounter = 0
                if jumpimgcounter < len(jumpimg)-1:
                    jumpimgcounter += 1
                else:
                    jumpimgcounter = 0

        

        elif keys[pygame.K_d] or js_axis_0 > 0.1:
            global runimgcounter
            self.screen.blit(runimg[runimgcounter],(self.hitbox.x-12,self.hitbox.y))
            if tickcounter >= 5:
                tickcounter = 0
                if runimgcounter < len(runimg)-1:
                    runimgcounter += 1
                else:
                    runimgcounter = 0
                    
        elif keys[pygame.K_a] or js_axis_0 < -0.1:
            global runleftimgcounter
            self.screen.blit(runleftimg[runleftimgcounter],(self.hitbox.x-12,self.hitbox.y))
            if tickcounter >= 5:
                tickcounter = 0
                if runleftimgcounter < len(runleftimg)-1:
                    runleftimgcounter += 1
                else:
                    runleftimgcounter = 0   
        
        else:
            self.screen.blit(standimg, (self.hitbox.x-12,self.hitbox.y))
            
        #print(tickcounter)
        

    
    def move(self):
        keys = pygame.key.get_pressed() 
        js_axis_0 = self.joystick.get_axis(0)

        if keys[pygame.K_a] or js_axis_0 <-0.1:
            self.hitbox[0] -= self.direction[0]
            
        if keys[pygame.K_d] or js_axis_0 > 0.1:
            self.hitbox[0] += self.direction[0]
            

        if keys[pygame.K_UP]:
            self.hitbox[1] -= self.direction[1]     

        if self.onGround and (keys[pygame.K_SPACE] or keys[pygame.K_w] or self.joystick.get_button(3)):
            #self.hitbox[1] -= self.direction[1]
            #self.jump = 100
            self.fall = -10
            self.onGround = False
            #print("Fire")

        if not(self.onGround): #and self.jump == 0:
            #self.direction[1] = 15

            if self.fall < 13:
                self.fall += 0.5
            self.direction[1] = self.fall

        else:
            self.fall = 2
            self.direction[1] = self.fall

        
            


        #if self.onGround:
        #    self.jump = 0


        
        """if self.jump > 0:
            self.direction[1] = 15
            self.jump -= 1
            if self.onGround:
                self.jump = 0
        
        if self.jump > 25:
            self.direction[1] = 7.5
            self.jump -= 1
            if self.onGround:
                self.jump = 0

        if self.jump > 50:
            self.direction[1] = 0
            self.jump -= 1
            
        if self.jump > 55:
            self.direction[1] = -7.5
            self.jump -= 1

        if self.jump > 80:
            self.direction[1] = -15
            self.jump -= 1"""

        self.hitbox[1] += self.direction[1]

        



