
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUEs = (230, 245, 255)

def line(screen, x, y):
    pygame.draw.line(screen, BLACK, (x, y), (x, y + 20), 2)

def draw_text(screen, text, x, y,  bar = -1, font_size = 17):
    lineH = 20
    max_width = 800 - 20 
    max_chars_per_line = max_width // 10

    if bar != -1:
        yp = (bar * 10) // 780
        xp = (bar * 10) % 780
        line(screen, x + xp, y + yp * lineH)
        
    font = pygame.font.SysFont('Courier New', font_size)
    while len(text) * 10 > 800 - 20: # need a new line
        index = max_chars_per_line
        if text[index] != ' ':
            index = text.rfind(' ', 0, index)
            if index == -1: 
                index = max_chars_per_line
        img = font.render(text[:index], True, BLACK) 
        screen.blit(img, (x, y))
        y += lineH
        text = text[index:].lstrip()

    img = font.render(text, True, BLACK)
    screen.blit(img, (x, y))
    

def draw_top(screen):
    pygame.draw.rect(screen, BLUEs, pygame.Rect(0, 0, 800, 35))
    pygame.draw.line(screen, BLACK, (0, 34), (800, 34), 1)
    ix = 10
    draw_text(screen, "File", ix, 10)
    draw_text(screen, "Edit", ix + 80, 10)
    draw_text(screen, "View", ix + 160, 10)
    
