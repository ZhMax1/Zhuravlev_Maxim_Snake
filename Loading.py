import pygame
import time
import codecs

pygame.init()

screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Экран загрузки')


def loading_screen(progress):
    font = pygame.font.SysFont(None, 50)
    text = font.render('Loading...', True, (18, 53, 36))
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 - text.get_height() // 2 - 50))
    screen.blit(text, text_rect)

    outline_font = pygame.font.Font(None, 50)
    outline_text = outline_font.render('Loading...', True, (255, 255, 255))
    outline_rect = outline_text.get_rect(
        center=(screen_width // 2 + 2, screen_height // 2 - outline_text.get_height() // 2 - 50 + 2))
    screen.blit(outline_text, outline_rect)

    color_start = (255, 244, 79)
    color_end = (202, 58, 39)
    current_color = [color_start[i] + int((color_end[i] - color_start[i]) * progress / 100) for i in range(3)]
    pygame.draw.rect(screen, current_color, (50, screen_height // 2 - 10, progress * 3, 30))

    progress_text = font.render(f'{progress}%', True, (18, 53, 36))
    progress_text_rect = progress_text.get_rect(center=(screen_width // 2, screen_height // 2 + 60))
    screen.blit(progress_text, progress_text_rect)

    outline_progress_font = pygame.font.Font(None, 50)
    outline_progress_text = outline_progress_font.render(f'{progress}%', True, (255, 255, 255))
    outline_progress_rect = outline_progress_text.get_rect(
        center=(screen_width // 2 + 2, screen_height // 2 + outline_progress_text.get_height() // 2 + 45))
    screen.blit(outline_progress_text, outline_progress_rect)

    pygame.display.flip()
    screen.fill((107, 142, 35))


loading_screen(0)

for i in range(101):
    loading_screen(i)
    time.sleep(0.05)

pygame.quit()

with codecs.open('Menu.py', 'r', encoding='utf-8') as file:
    code = file.read()
    exec(code)
