import pygame
import subprocess
import sys

pygame.init()

# Fenstergröße
size = width, height = 800, 600
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
menu_items = ["Game 1", "Game 2", "Game 3", "Exit"]
menu_actions = ["Super Maria Galaxy/main.py", "game2.py", "game3.py", "exit"]
selected_item = 0

# Gamecontroller initialisieren
pygame.joystick.init()
try:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
except pygame.error:
    joystick = None

def draw_menu():
    screen.fill(black)
    for index, item in enumerate(menu_items):
        if index == selected_item:
            label = font.render(item, True, blue)
        else:
            label = font.render(item, True, white)
        screen.blit(label, (width//2 - label.get_width()//2, height//4 + index * 100))
    pygame.display.flip()

def start_game(script_name):
    subprocess.run(["python", script_name])

def main():
    global selected_item
    clock = pygame.time.Clock()

    running = True
    while running:
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
                        start_game(menu_actions[selected_item])
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == 1 and event.value > 0.1:
                    selected_item = (selected_item + 1) % len(menu_items)
                elif event.axis == 1 and event.value < -0.1:
                    selected_item = (selected_item - 1) % len(menu_items)
            elif event.type == pygame.JOYBUTTONDOWN and event.button == 8:
                    if menu_actions[selected_item] == "exit":
                        running = False
                    else:
                        start_game(menu_actions[selected_item])                

        if joystick:
            if joystick.get_button(1):  # Down
                selected_item = (selected_item + 1) % len(menu_items)
            elif joystick.get_button(0):  # Up
                selected_item = (selected_item - 1) % len(menu_items)
            elif joystick.get_button(9):  # Start button
                if menu_actions[selected_item] == "exit":
                    running = False
                else:
                    start_game(menu_actions[selected_item])

        draw_menu()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
