import pygame, sys
import random

# Initialisierung von Pygame
pygame.init()

# Bildschirmgröße
breite = 800
hoehe = 600

# Farben
black = (0, 0, 0)
white = (255, 255, 255)

# Schriftart und Größe festlegen
font = pygame.font.SysFont(None, 48)

# Spielbildschirm erstellen
screen = pygame.display.set_mode((breite, hoehe),pygame.NOFRAME)
pygame.display.set_caption("Asteroids")

#Variablen und Clock definieren
clock = pygame.time.Clock()

pygame.joystick.init()
def initController():
    try:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
    except pygame.error:
        joystick = None
    return(joystick)

asteroidIMGk = pygame.image.load("asteroid.png")
asteroidIMGg = pygame.image.load("asteroid.png")
asteroidIMGm = pygame.image.load("asteroid.png")
bg = pygame.image.load("background3.png")
schussIMG = pygame.image.load("Schuss.png")


#Größe der Bilder anpassen
k=20
m=30
g=50
asteroidIMGk = pygame.transform.scale(asteroidIMGk, (k, k))
asteroidIMGm = pygame.transform.scale(asteroidIMGm, (m, m))
asteroidIMGg = pygame.transform.scale(asteroidIMGg, (g, g))
bg = pygame.transform.scale(bg, (800,600))
schussIMG= pygame.transform.scale(schussIMG, (20,20))
#Erstellt eine leere Liste für die Asteroiden
asteroidList = []
schussList=[]
#Füge hier Asteroiden in die Liste ein:
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),k,k))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),k,k))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),k,k))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),k,k))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),k,k))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),k,k))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),k,k))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),m,m))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),m,m))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),m,m))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),m,m))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),m,m))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),m,m))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),m,m))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),m,m))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),m,m))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),m,m))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),m,m))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),g,g))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),g,g))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),g,g))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),g,g))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),g,g))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),g,g))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),g,g))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),g,g))
asteroidList.append(pygame.Rect(random.randint(300,1200),random.randint(0,600),g,g))



#Ersetze das pass mit Logik um die Asteroiden an Stelle der Hitbox zu zeichnen.
#Gehe dazu die Liste mit Hilfe der for-Schleife durch.
def renderAsteroids(asteroidList):
    for asteroid in range(len(asteroidList)):
        if asteroid <= 6:
            screen.blit(asteroidIMGk, asteroidList[asteroid])
        if asteroid > 6 and asteroid <=17:
            screen.blit(asteroidIMGm, asteroidList[asteroid])
        if asteroid >17:
            screen.blit(asteroidIMGg, asteroidList[asteroid])
    return()


#Bewegung der Asteroiden
def moveAsteroids(asteroidList):
    for asteroid in asteroidList:
        asteroid.move_ip(-s,0)
    return()

#Grafiken laden
spaceshipIMG = pygame.image.load("spaceship.png")
spaceshipIMG = pygame.transform.scale(spaceshipIMG, (40, 40))
#Hitbox für das Spaceship erzeugen (Ersetze das None):
spaceship = pygame.Rect(100,300,40,40)

#Spaceship zeichnen:

def drawSpaceship(spaceship):
    screen.blit(spaceshipIMG, spaceship)
    return()


def moveSpaceship(spaceship):
    # Ermittelt die gedrückten Tasten
    keys = pygame.key.get_pressed()
    #Programmiere die Steuerung nach dem Muster:
    if (keys[pygame.K_LEFT] or joystick.get_axis(0) < -0.1) and spaceship.x>10:
        spaceship.move_ip(-10,0)
    if (keys[pygame.K_RIGHT]  or joystick.get_axis(0) > 0.1) and spaceship.x<745:
        spaceship.move_ip(10,0)
    if (keys[pygame.K_DOWN]  or joystick.get_axis(1) > 0.1)and spaceship.y<545:
        spaceship.move_ip(0,10)
    if (keys[pygame.K_UP] or joystick.get_axis(1) < -0.1) and spaceship.y>10:
        spaceship.move_ip(0,-10)

hitpoints = 3

# Programmiere hier die Überprüfung, ob das Raumschiff einen Asteroiden trifft und programmiere die Logik, 
# was passieren soll, wenn das der Fall ist. 
def checkCollision(hitpoints,spaceship,asteroidList):
    for asteroid in asteroidList:
        if spaceship.colliderect(asteroid):
            hitpoints -= 1
            asteroid.x=random.randint(900,1300)
            asteroid.y=random.randint(0,600)
        if asteroid.x <1:
            asteroid.x=random.randint(900,1300)
            asteroid.y=random.randint(0,600)
    return(hitpoints)

#Definiert eine Schriftart und Schriftgröße für das Spiel
font = pygame.font.SysFont(None, 48)

# Programmiere hier die Score-Anzeige
def renderHitpoints(hitpoints,font):
    text = font.render(f"Leben:{hitpoints}", True, white)
    screen.blit(text, (100, 100))
    #pass
    return()    

def renderScore(score):
    textt = font.render(f"Score:{score}", True, white)
    screen.blit(textt, (400, 100))
    return()

score = 0

    
# Spielschleife

running = True
c=100
s=5
joystick = initController()
while running:
    if hitpoints>-1:
        score+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE] or joystick.get_button(9):
        running = False
    #schusscountdown
    c+=1
    #Schnelligkeit Asteroiden
    s = (5+(score//300))
    #Ruft die Spielelogik auf, die du oben programmiert hast
    moveAsteroids(asteroidList)
    moveSpaceship(spaceship)
    hitpoints=checkCollision(hitpoints,spaceship,asteroidList)
    
    # Zeichnungen der Objekte
    # Hier wird alles, was du oben programmiert hast, aufgerufen
    #screen.fill(white)
    gblist=[]
    gblist.append(pygame.Rect(0,0,800,600))
    screen.blit(bg, gblist[0])
    renderAsteroids(asteroidList)
    drawSpaceship(spaceship)
    renderHitpoints(hitpoints, font)
    renderScore(score)
    #Schüsse
    for schuss in schussList:
        schuss.move_ip(5,0)
    if (keys[pygame.K_SPACE] or joystick.get_button(1))and c > 50:
        c=0
        schussList.append(pygame.Rect(spaceship.x,spaceship.y,20,20))
    for schuss in range(len(schussList)):
        screen.blit(schussIMG, schussList[schuss])


    for schuss in schussList:
        for asteroid in asteroidList:
            if asteroid.colliderect(schuss):
                asteroid.x=800
                asteroid.y=random.randint(0,600)
                schuss.x=0
                schuss.y=700
    if hitpoints<0:
        sc=score
        screen.fill(black)
        gameover = font.render("Game Over", True, white)
        screen.blit(gameover, (300, 150))
        scr = font.render(f"Score={sc}", True, white)
        screen.blit(scr, (300, 250))
        
        
    pygame.display.flip()
    clock.tick(30)
 

pygame.quit()
sys.exit()   
