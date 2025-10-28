import pygame, sys

pygame.init()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("D&D Combat GUI")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Layout zones
button_rects = {
    "Attack": pygame.Rect(80, 470, 150, 50),
    "Spell":  pygame.Rect(250, 470, 150, 50),
    "Item":   pygame.Rect(420, 470, 150, 50),
    "Flee":   pygame.Rect(590, 470, 150, 50)
}

msg = "Choose your action."

def draw_ui():
    screen.fill((200,230,255))
    # text box
    pygame.draw.rect(screen, (255,255,255), (40,420,720,60))
    pygame.draw.rect(screen, (0,0,0), (40,420,720,60), 2)
    t = font.render(msg, True, (0,0,0))
    screen.blit(t, (60,440))

    # buttons
    for name, rect in button_rects.items():
        pygame.draw.rect(screen, (240,240,240), rect)
        pygame.draw.rect(screen, (0,0,0), rect, 2)
        label = font.render(name, True, (0,0,0))
        label_rect = label.get_rect(center=rect.center)
        screen.blit(label, label_rect)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            for name, rect in button_rects.items():
                if rect.collidepoint(e.pos):
                    msg = f"{name} pressed."

    draw_ui()
    pygame.display.flip()
    clock.tick(30)
