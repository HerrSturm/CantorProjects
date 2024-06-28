import pygame
import subprocess
import sys
import os

pygame.init()

# Fenstergröße
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Arcade Game Menu")

# Farben
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Schriftarten
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# Menüpunkte
menu_items = ["Super Maria Galaxy", "Game 2", "Game 3", "Exit"]
menu_actions = [("Super Maria Galaxy","main.py"), ("","game2.py"), ("","game3.py"), "exit"]
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
    for index, item in enumerate(menu_items):
        if index == selected_item:
            label = font.render(item, True, blue)
        else:
            label = font.render(item, True, white)
        screen.blit(label, (width//2 - label.get_width()//2, height//4 + index * 100))
    pygame.display.flip()

def start_game(script_name,directory):
    original_directory = os.getcwd()
    try:
        # Setze das Arbeitsverzeichnis auf den Ordner, in dem das Menü-Skript liegt
        new_directory = f"{directory}/"   
        os.chdir(new_directory)
        # Führe das Skript aus
        subprocess.run(["python", script_name])
    finally:
        # Kehre zum ursprünglichen Arbeitsverzeichnis zurück
        os.chdir(original_directory)


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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_item = (selected_item + 1) % len(menu_items)
                elif event.key == pygame.K_UP:
                    selected_item = (selected_item - 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    if menu_actions[selected_item] == "exit":
                        running = False
                    else:
                        start_game(menu_actions[selected_item][1],menu_actions[selected_item][0])   
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 1 and event.value > 0.1:
                    selected_item = (selected_item + 1) % len(menu_items)
                elif event.axis == 1 and event.value < -0.1:
                    selected_item = (selected_item - 1) % len(menu_items)
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 9:
                    if menu_actions[selected_item] == "exit":
                        running = False
                    else:
                        start_game(menu_actions[selected_item][1],menu_actions[selected_item][0])                

        
        draw_menu()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
