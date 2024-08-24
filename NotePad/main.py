import pygame
from func import draw_text
from func import draw_top
from func import line

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


pygame.font.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Note Pad")

x = 10
y = 50
screen.fill(WHITE)
draw_top(screen)
line(screen, x , y)
pygame.display.flip()

running = True
erasing = False
string = ''
c = 0
baseDelay = 100000
tempDelay = baseDelay
capsLock = False
pos = 0


def refresh():
    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 35, 800, 600-35))
    draw_text(screen, string, x, y, pos)
    pygame.display.flip()           

while running:
    c += 1
    for event in pygame.event.get():

        if event.type == pygame.QUIT: # Close screen/game
            running = False
            
        elif event.type == pygame.KEYDOWN: # Button pressed
            
            key_name = pygame.key.name(event.key)            
            
            if len(key_name) == 1: 
                if capsLock:
                    string = string[:pos] +  key_name.upper() + string[pos:]
                else:
                    string = string[:pos] +  key_name + string[pos:]
                pos += 1
            elif event.key == pygame.K_SPACE:  
                string = string[:pos] +  ' ' + string[pos:]
                pos += 1
            elif event.key == pygame.K_BACKSPACE:
                c = 0
                erasing = True
                tempDelay = baseDelay
            elif event.key == pygame.K_CAPSLOCK:
                capsLock = not capsLock
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                capsLock = not capsLock
            elif event.key == pygame.K_LEFT:
                pos = max(0, pos - 1)
            elif event.key == pygame.K_RIGHT:
                pos = min(pos + 1, len(string))

            refresh()    

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_BACKSPACE:
                erasing = False
            elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                capsLock = not capsLock
        #elif event.type == pygame.MOUSEBUTTONDOWN:
    if erasing:
        if c % tempDelay == 0:
            tempDelay = max(tempDelay - 5000, 10000)
            if pos != 0:
                string = string[:pos - 1] + string[pos:]
            pos = max(0, pos - 1)
            refresh()
            
    


pygame.quit()
