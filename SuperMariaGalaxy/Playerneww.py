import sys, pygame

from Block import *
from Player import *
from Enemies import *

from engine import *

#Import der Objektklassen

size=(800,800)
FPS=60
clock = pygame.time.Clock()


def main():
    # Initialisiere Pygame
    pygame.init()
    
    
    #Erstellung der Objekte:
    
    
    gameloop(FPS)



def gameloop(FPS):
    screen = pygame.display.set_mode(size)
    running=True



    enemy=Enemies((100,300,40,40))
    
    block1 = [
        Block((50, 500, 50, 20)),
        Block((125, 450, 50, 20)),
        Block((200, 400, 50, 20)),
        Block((275, 500, 50, 20)),
        Block((350, 450, 50, 20)),
        Block((425, 500, 50, 20)),
        Block((500, 450, 50, 20)),
        Block((575, 400, 50, 20)),
        Block((650, 500, 50, 20)),
        Block((725, 450, 50, 20)),
        ]
    block2 =[
        Block((50, 500, 50, 20)),
        Block((125, 450, 50, 20)),
        Block((200, 400, 50, 20)),
        Block((275, 350, 50, 20)),
        Block((350, 300, 50, 20)),
        Block((425, 250, 50, 20)),
        Block((500, 200, 50, 20)),
        Block((575, 150, 50, 20)),
        Block((650, 100, 50, 20)),
        Block((725, 50, 50, 20)),
    ]


    player = Player([80,100,10,50])
    
    
    
    while running:


        screen.fill((0,0,0))

        #print(player.direction[1])
        player.move()

        for i in block1:
            i.move() 

        for i in block1:
            
            checkCollision(player, i)

            if player.onGround:
                break



        #block1.update()
        enemy.update()


        player.draw()


        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        for obj in block1:
            obj.update()
            

            
        clock.tick(FPS)
        pygame.display.flip()
    

# Starte das Spiel
if __name__ == "__main__":
    main()