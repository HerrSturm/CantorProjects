import pygame
import subprocess
import sys
import os
import csv

pygame.init()

# Fenstergröße
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size,pygame.NOFRAME)
pygame.display.set_caption("Arcade Game Menu")

spiele = []

with open('games.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        spiele.append(row)

# Farben
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Schriftarten
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# Menüpunkte
#menu_items = ["Super Maria Galaxy", "Game 2", "Game 3", "Exit"]
#menu_actions = [("Super Maria Galaxy","main.py"), ("","game2.py"), ("","game3.py"), "exit"]
selected_item = 0

# Gamecontroller initialisieren
pygame.joystick.init()
def initController():
    try:
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
    except pygame.error:
        joystick = None
    return(joystick)

def draw_menu():
    screen.fill(black)
    for index, spiel in enumerate(spiele):
        if index == selected_item:
            label = font.render(f"{spiel['name']} (Spieler: {spiel['player']})", True, blue)
        else:
            label = font.render(f"{spiel['name']}  (Spieler: {spiel['player']})", True, white)
        screen.blit(label, (width//2 - label.get_width()//2, height//4 + index * 100))
    pygame.display.flip()

def start_game(spiel):
    original_directory = os.getcwd()
    try:
        # Setze das Arbeitsverzeichnis auf den Ordner, in dem das Menü-Skript liegt
        new_directory = f"{spiel['path']}/"   
        os.chdir(new_directory)
        # Führe das Skript aus
        subprocess.run(["python", spiel['file']])
    finally:
        # Kehre zum ursprünglichen Arbeitsverzeichnis zurück
        os.chdir(original_directory)
        pygame.event.get()


def main():
    global selected_item
    clock = pygame.time.Clock()
    joystick = initController()

    


    running = True
    while running:
        #Controller nachträglich initialisieren
        if not(joystick):
            joystick = initController()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #Tastaturstuerung
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_item = (selected_item + 1) % len(spiele)
                elif event.key == pygame.K_UP:
                    selected_item = (selected_item - 1) % len(spiele)
                elif event.key == pygame.K_RETURN:
                    start_game(spiele[selected_item])
            #Joysticksteuerung 
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 1 and event.value > 0.1:
                    selected_item = (selected_item + 1) % len(spiele)
                elif event.axis == 1 and event.value < -0.1:
                    selected_item = (selected_item - 1) % len(spiele)
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 9:
                start_game(spiele[selected_item])                
            elif joystick.get_button(4) and joystick.get_button(5):
                running = False
        
        draw_menu()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
