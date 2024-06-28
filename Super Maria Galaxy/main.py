import sys, pygame

#Import der Objektklassen
from Block import *
from Player import *
from EnemiesIronBall import *
from EnemiesSpikes import *
from FallingEnemies import *
from engine import *
from worm import *





# Bildschirm festlegen

size=(800,800)
FPS=60
zeit=[0,0]
levelTime=0
points = 40

timepoints=90



#pygame.mixer.init()

pygame.joystick.init()
def initController():
    try:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
    except pygame.error:
        joystick = None
    return(joystick)
joystick = initController()

clock = pygame.time.Clock()


# globale Variablen festlegen
levels = []
listenemys = []

#Funktionen

def main():
    # Initialisiere Pygame
    pygame.init()
    init()  
    draw_start_menu()
    gameloop(FPS)

def init():
    screen = pygame.display.set_mode(size)


#Endlevel: legt Endblock fest und prüft nach Kollision mit diesem
def endlevel(currentLevel,levels, player):
    
    endBlock=levels[currentLevel][len(levels[currentLevel])-1]  
    ende=False
    if(player.hitbox.colliderect(endBlock.hitbox)):
        ende=True


        sound = pygame.mixer.Sound('victory.WAV') 
        sound.play() # Victory sound bei Abschluss des levels

    return(ende)        


def updateLevelPoints(points,levelTime):
    timepoints=90-levelTime
    if(timepoints>0):
        points+=int(round((timepoints/15)**2,0))
    points += 15
    return(points)
    
#Levelwechsel: lädt neues Level + Enemys und Update Punkte
def updateLevel(currentLevel,levels,player,start,currentenemys,points,levelTime):
    newlevelstart = False
    if endlevel(currentLevel,levels,player):
        currentLevel +=1
        currentenemys += 1
        
        points=updateLevelPoints(points,levelTime)
        levelTime=0
        newlevelstart = True
    try:
        start=[levels[currentLevel][0].hitbox.x,levels[currentLevel][0].hitbox.y-50]
        #player=Player([start[0],start[1],16,40])
        if newlevelstart:
            player.hitbox.x = start[0]
            player.hitbox.y = start[1]
            newlevelstart = False
        
        return(currentLevel,start,currentenemys,points,levelTime)
    except:
        return(10,10,points)

def main():
    # Initialisiere Pygame
    pygame.init()
    init()
    
    #Erstellung der Objekte:
    
    draw_start_menu()
    gameloop(FPS)
    pygame.quit()
    sys.exit()
                
    

    
def update_highscore(highscore,points):
           
    if points>highscore:
        highscore = points
        with open("highscore.txt", "w") as datei:
            datei.write(str(highscore))          
    return(highscore)

#Startmenü
def draw_start_menu():
    running = True
    screen = pygame.display.set_mode(size)
    while running:

        #Hintergrund
        screen.fill((0,0,0))
        backgroundimg = pygame.image.load("images/background/backgroundbeginning.png")
        #playerimg = pygame.image.load("images/background/player.png")
        screen.blit(backgroundimg, (0,0))
        #screen.blit(playerimg, (400,400))
        
        #Text des Startbildschirms; Font, Farbe
        font = pygame.font.Font("Font/CHASER.ttf", 35)
        text_surface = font.render(("Press START to start the game!"), True,((246, 218, 254))) 
        screen.blit(text_surface,(100 ,675))
        font = pygame.font.Font("Font/SuperMario256.ttf", 90)
        text_surface = font.render(("Super Maria"), True,((248, 155, 156)))
        screen.blit(text_surface,(75 ,75))
        text_surface = font.render(("Galaxy"), True,((248, 155, 156))) 
        screen.blit(text_surface,(200 ,175))
        
        #Aktualisierung des screen
        clock.tick(60)

        pygame.display.flip()
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s] or joystick.get_button(9):
            running = False


def gameloop(FPS):
    screen = pygame.display.set_mode(size)
    running = True
    start = [80,100]
    currentLevel = 0
    currentenemys = 0

    


    
    backtrack = pygame.mixer.Sound('doommusic.MP3')
    backtrack.play(-1)
    
    

    global points
    global levelTime
    with open("highscore.txt", "r") as datei:
        highscore = int(datei.read())

    
    
    
    block1 = [
        Block((50, 200, 40, 20)),
        #Block((200, 0, 40, 20)),
        Block((50, 500, 40, 20)),
        Block((125, 450, 40, 20)),
        Block((200, 400, 40, 20)),
        Block((275, 500, 40, 20)),
        Block((350, 450, 40, 20)),
        Block((425, 500, 40, 20)),
        Block((500, 450, 40, 20)),
        Block((575, 400, 40, 20)),
        Block((650, 500, 40, 20)),
        Block((725, 450, 40, 20)),
        ]
    

    block2 =[
        Block((50, 500, 40, 20)),
        Block((125, 450, 40, 20)),
        Block((200, 400, 40, 20)),
        Block((275, 350, 40, 20)),
        Block((350, 300, 40, 20)),
        Block((425, 250, 40, 20)),
        Block((500, 200, 40, 20)),
        Block((575, 150, 40, 20)),
        Block((650, 100, 40, 20)),
        Block((725, 50, 40, 20)),
        ]
    
    block3 = [
        Block((50, 500, 40, 20)),
        Block((125, 450, 40, 20)),
        Block((200, 400, 40, 20)),
        Block((275, 350, 40, 20)),
        Block((350, 400, 40, 20)),
        Block((425, 450, 40, 20)),
        Block((500, 400, 40, 20)),
        Block((575, 450, 40, 20)),
        Block((650, 500, 40, 20)),
        Block((725, 450, 40, 20)),
        ]
    block4 = [
        Block((50, 500, 40, 20)),
        Block((125, 450, 40, 20)),
        Block((200, 400, 40, 20)),
        Block((275, 400, 40, 20)),
        Block((350, 400, 40, 20)),
        Block((425, 350, 40, 20)),
        Block((500, 400, 40, 20)),
        Block((575, 450, 40, 20)),
        Block((650, 400, 40, 20)),
        Block((725, 450, 40, 20)),
        ]

    block5 = [
        Block((50, 500, 40, 20)),
        Block((125, 450, 40, 20)),
        Block((200, 400, 40, 20)),
        Block((275, 400, 40, 20)),
        Block((350, 450, 40, 20)),
        Block((425, 500, 40, 20)),
        Block((500, 450, 40, 20)),
        Block((575, 400, 40, 20)),
        Block((650, 600, 40, 20)),
        Block((725, 550, 40, 20)),
    ]

    block6 = [
        Block((50, 500, 40, 20)),
        Block((125, 450, 40, 20)),
        Block((200, 400, 40, 20)),
        Block((275, 400, 40, 20)),
        Block((350, 350, 40, 20)),
        Block((425, 300, 40, 20)),
        Block((500, 350, 40, 20)),
        Block((575, 400, 40, 20)),
        Block((650, 350, 40, 20)),
        Block((725, 300, 40, 20)),
    ]

    block7 = [
        Block((50, 500, 40, 20)),
        Block((125, 450, 40, 20)),
        Block((200, 400, 40, 20)),
        Block((275, 350, 40, 20)),
        Block((350, 300, 40, 20)),
        Block((425, 250, 40, 20)),
        Block((500, 200, 40, 20)),
        Block((575, 250, 40, 20)),
        Block((650, 300, 40, 20)),
        Block((725, 350, 40, 20)),
    ]

    block8 = [
        Block((50, 500, 40, 20)),
        Block((125, 450, 40, 20)),
        Block((200, 400, 40, 20)),
        Block((275, 350, 40, 20)),
        Block((350, 400, 40, 20)),
        Block((425, 450, 40, 20)),
        Block((500, 400, 40, 20)),
        Block((575, 350, 40, 20)),
        Block((650, 400, 40, 20)),
        Block((725, 450, 40, 20)),
    ]

    block9 = [
        Block((50, 500, 40, 20)),
        Block((125, 450, 40, 20)),
        Block((200, 400, 40, 20)),
        Block((275, 350, 40, 20)),
        Block((350, 400, 40, 20)),
        Block((425, 450, 40, 20)),
        Block((500, 400, 40, 20)),
        Block((575, 350, 40, 20)),
        Block((650, 300, 40, 20)),
        Block((725, 250, 40, 20)),
    ]

    block10 = [
        Block((50, 500, 40, 20)),
        Block((125, 450, 40, 20)),
        Block((200, 400, 40, 20)),
        Block((275, 350, 40, 20)),
        Block((350, 500, 40, 20)),
        Block((425, 450, 40, 20)),
        Block((500, 400, 40, 20)),
        Block((575, 450, 40, 20)),
        Block((650, 400, 40, 20)),
        Block((725, 450, 40, 20)),
    ]

    levels = [block1, block2, block3, block4, block5, block6, block7, block8, block9, block10]


    
    enemy1 = [IronBall(100, 300),spikes(445,460),FallingEnemies((575,0,40,40,),390)]
    
    enemy2 = [IronBall(100, 300),spikes(445,210),FallingEnemies((125,0,40,40),440)]
    
    enemy3 = [IronBall(100, 300),spikes(445,410),FallingEnemies((650,0,40,40),490)]
    
    enemy4 = [spikes(445,310),FallingEnemies((575,0,40,40),440),Worm(1000,380)]
    
    enemy5 = [IronBall(100, 300),spikes(445,460),FallingEnemies((425,0,40,40),490)]

    enemy6 = [IronBall(100, 300),spikes(445,260),FallingEnemies((575,0,40,40),390)]
    
    enemy7 = [IronBall(100, 300),spikes(445,210),FallingEnemies((200,0,40,40),390)]
    
    enemy8 = [IronBall(100, 300),spikes(445,410),FallingEnemies((425,0,40,40),440)]
    
    enemy9 = [IronBall(100, 300),spikes(445,410),FallingEnemies((200,0,40,40),390)]
    
    enemy10 = [IronBall(100, 300),spikes(445,410),FallingEnemies((575,0,40,40),440)]
    
    listenemys = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10]

    player = Player([start[0],start[1],10,40],joystick)
    

    
    backgroundimg = pygame.image.load("images/background/background1.png")

    
    zeitcounter=0
    respawn=0

    respawncounter=0

    




    startKeyReleased = False

    while running:
        if not(joystick.get_button(9)):
            startKeyReleased = True
        #Spiel beenden
        keys = pygame.key.get_pressed() #gets the pressed keys
        if keys[pygame.K_ESCAPE] or (startKeyReleased and joystick.get_button(9)):
            running = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()


        

        #Respwan-Knopf
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_RSHIFT] or player.hitbox.y > 1000:
            sound = pygame.mixer.Sound('fall.MP3') 
            sound.play() #deathsound bei Abschluss des levels
            if respawncounter==0:
                player.hitbox.x = start[0]
                player.hitbox.y = start[1]
                respawn+=1
                points -= 1
                respawncounter=1
        if respawncounter!=0:
            respawncounter+=1
        if respawncounter>=15:
            respawncounter=0  
               
            
            
        


        #DEBUG
        #print(player.direction[1])
        #print(player.direction[1])
        #print(player.onGround)
            
     
        
  





        LLUpdate=updateLevel(currentLevel, levels,player,start,currentenemys,points,levelTime)

        if LLUpdate[0]<10:
            currentLevel=LLUpdate[0]
            currentenemys = LLUpdate[2]
            points=LLUpdate[3]
            levelTime=LLUpdate[4]
        else:
           
            running=False
            screen.fill((0,0,0))

    
            points=LLUpdate[2]
            
       
            
         

                 
            backgroundimg = pygame.image.load("images/background/backgroundend3.png")
            screen.blit(backgroundimg, (0,0))
            font = pygame.font.Font("Font/Comic Hunter.ttf", 40)
            text_surface = font.render(("Congratulations, you succeeded!"), True,(254, 228, 232)) 
            screen.blit(text_surface,(95 ,250))
            font = pygame.font.Font("Font/Comic Hunter.ttf", 30)
            text_surface = font.render(("Your time was "+ minute + " : "+ sekunde+"."), True,(170, 153, 213)) 
            screen.blit(text_surface,(250 ,550))
            text_surface = font.render(("You had to respawn "+ str(respawn)+" times."), True,(170, 153, 213)) 
            screen.blit(text_surface,(200 ,600))

            text_surface = font.render(("Your score: "+ str(points)+" points."), True,(170, 153, 213)) 
            screen.blit(text_surface,(250 ,650))


            
            while running==False:
                keys = pygame.key.get_pressed() #gets the pressed keys
                if keys[pygame.K_ESCAPE] or joystick.get_button(9):
                    pygame.quit()
            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        sys.exit()
                
    
                
                    
                    
             
                    clock.tick(FPS)
                    pygame.display.flip()

                    
                    
               
                    
      

     
        highscore=update_highscore(highscore,points)
        


       
        #Koordinaten vom Startblock übergeben
        start=LLUpdate[1]

        
        #Zeit
        zeitcounter+=1
        if(zeitcounter>=60):
            zeit[0]+=1
            levelTime+=1
            if(zeit[0]>=60):
                zeit[1]+=1
                zeit[0]=0
            zeitcounter=0

        minute=str(zeit[1])
        sekunde=str(zeit[0])
        if len(minute)==1:
            minute="0"+minute
        
        if len(sekunde)==1:
            sekunde="0"+sekunde
        
        font = pygame.font.Font(None, 30)
        text_surface = font.render(minute+" : "+sekunde, True,(255 ,255 ,255)) 
        screen.blit(text_surface,(25 ,25))


        #Game-Stats zeichnen
        text_surface = font.render(("Respawns: "+str(respawn)), True,(255 ,255 ,255)) 
        screen.blit(text_surface,(25 ,50))

        text_surface = font.render(("Level: "+str(currentLevel+1)+"/10"), True,(255 ,255 ,255)) 
        screen.blit(text_surface,(25 ,75))

        text_surface = font.render(("Points: "+str(points)), True,(255 ,255 ,255)) 
        screen.blit(text_surface,(25 ,100))

        text_surface = font.render(("Highscore: "+str(highscore)), True,(255 ,255 ,255)) 


        screen.blit(text_surface,(25 ,125))
    


        #Player-Enemy-Kollision
        for i in listenemys[currentenemys]:
            if checkEnemyCollision(player, i, start):
                respawn+=1
                sound = pygame.mixer.Sound('hit.MP3') 
                sound.play()
                points -= 1
                
            i.update()


        #for i in levels[currentLevel]:
        #    i.move() 


        #Player-Block-Kollision
        for i in levels[currentLevel]:

            checkCollisionY(player, i)

        for i in levels[currentLevel]:
            
            checkCollisionX(player, i)

            if player.onGround:
                break

        
        #Update Level, Enemys
        for obj in levels[currentLevel]:
            obj.update()

        for i in listenemys[currentenemys]:
            i.update()


        
        player.move()

        player.draw()


            
        clock.tick(FPS)
        pygame.display.flip()

        screen.blit(backgroundimg, (0, 0))
    

            
    

# Starte das Spiel
if __name__ == "__main__":
        main()


