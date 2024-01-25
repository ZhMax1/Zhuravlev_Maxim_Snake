import pygame
import os
import sys
import Snake as SnakeClass
import Food as FoodClass
from Field import Field

os.system('title SNAKE')
os.system('cls')

colors = [(50, 50, 50), (255, 255, 255), (128, 128, 128), (230, 80, 60), (255, 210, 50)]

map_size = 25
scale = 20
fps = 10
element_size = 20

running = True
pause = False
game_over = False
borders = False
done = False

field = Field((25, 25), 20, True)
args = sys.argv[1:]
try:
    if len(args) > 0:
        if len(args) >= 1:
            map_size = int(args[0])
            if 10 <= map_size <= 30:
                print(f"\n{'argument initialized map size':<20} to {map_size}")
            else:
                map_size = 25
        if len(args) >= 2:
            scale = int(args[1])
            if 20 <= scale <= 40:
                print(f"{'argument initialized scale':<20} to {scale}")
            else:
                scale = 25
        if len(args) >= 3:
            fps = int(args[2])
            print(f"{'argument initialized fps':<20} to {fps}")
        if len(args) == 4 and (args[3].lower() == 'true' or args[3].lower() == 'false'):
            if args[3].lower() == 'true':
                borders = True
            elif args[3].lower() == 'false':
                borders = False
            print(f"{'argument initialized borders':<20} to {'true' if borders else 'false'}")
except (ValueError, IndexError):
    pass

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
app = pygame.display.set_mode((map_size * scale, map_size * scale))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

pause_bg = pygame.Surface((map_size * scale, map_size * scale))
pause_bg.set_alpha(128)

snake = SnakeClass.Snake([[2, 12], [1, 12], [0, 12]])
FoodClass = FoodClass.Food(map_size, snake.elements, 1)

font_sizes = [int(map_size * scale / 15), int(map_size * scale / 5)]


def display_len():
    global font_sizes
    font = pygame.font.SysFont("Arial", font_sizes[0])
    text = font.render(str(snake.lenght), True, colors[1])
    text_shadow = font.render(str(snake.lenght), True, (0, 0, 0))
    app.blit(text_shadow, (scale / 2 + 2, scale / 2 + 2))
    app.blit(text, (scale / 2, scale / 2))


def pause_screen():
    global done, font_sizes
    pause_bg.fill((0, 0, 0))
    font = pygame.font.SysFont("Arial", font_sizes[1])
    text = font.render("ПАУЗА", True, colors[1])
    text_shadow = font.render("ПАУЗА", True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (map_size * scale / 2, map_size * scale / 2)
    app.blit(pause_bg, (0, 0))
    app.blit(text_shadow, (text_rect.x + 2, text_rect.y + 2))
    app.blit(text, text_rect)


def game_over_screen():
    global done, font_sizes
    pause_bg.fill(colors[3])
    font = pygame.font.SysFont("Arial", font_sizes[1])
    text = font.render("game over", True, colors[1])
    text_rect = text.get_rect()
    text_rect.center = (map_size * scale / 2, map_size * scale / 2 - font_sizes[1])  # Изменяем координаты по вертикали
    app.blit(pause_bg, (0, 0))

    shadow_offset = 2
    shadow_color = (0, 0, 0)
    shadow_text = font.render("game over", True, shadow_color)
    shadow_rect = text.get_rect()
    shadow_rect.center = (text_rect.center[0] + shadow_offset, text_rect.center[1] + shadow_offset)
    app.blit(shadow_text, shadow_rect)

    app.blit(text, text_rect)

    font = pygame.font.SysFont("Arial", font_sizes[0])
    text = font.render("press r to restart", True, colors[1])
    text_rect = text.get_rect()
    text_rect.center = (map_size * scale / 2, map_size * scale / 2 + font_sizes[0] * 2 - 35)

    shadow_text = font.render("press r to restart", True, shadow_color)
    shadow_rect = text.get_rect()
    shadow_rect.center = (text_rect.center[0] + shadow_offset, text_rect.center[1] + shadow_offset)
    app.blit(shadow_text, shadow_rect)

    app.blit(text, text_rect)

    text = font.render("press Esc to menu", True, colors[1])
    text_rect = text.get_rect()
    text_rect.center = (map_size * scale / 2, map_size * scale / 2 + font_sizes[0] * 4 - 40)

    shadow_text = font.render("press Esc to menu", True, shadow_color)
    shadow_rect = text.get_rect()
    shadow_rect.center = (text_rect.center[0] + shadow_offset, text_rect.center[1] + shadow_offset)
    app.blit(shadow_text, shadow_rect)

    app.blit(text, text_rect)


def restart():
    global pause, game_over
    snake.restart([[2, 12], [1, 12], [0, 12]])
    pause = False
    game_over = False


while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
            running = False
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_r and game_over:
            restart()
        elif e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE and not game_over:
            pause = not pause
            pause_screen()
        elif e.type == pygame.KEYDOWN and not snake.key_lock and not pause and not game_over:
            if (e.key == pygame.K_w or e.key == pygame.K_UP) and snake.dir != 'S':
                snake.dir = 'N'
                snake.key_lock = True
            elif (e.key == pygame.K_s or e.key == pygame.K_DOWN) and snake.dir != 'N':
                snake.dir = 'S'
                snake.key_lock = True
            elif (e.key == pygame.K_d or e.key == pygame.K_RIGHT) and snake.dir != 'W':
                snake.dir = 'E'
                snake.key_lock = True
            elif (e.key == pygame.K_a or e.key == pygame.K_LEFT) and snake.dir != 'E':
                snake.dir = 'W'
                snake.key_lock = True

    if not pause and not game_over:
        field.display(app, [(189, 218, 87), (169, 198, 67), (0, 0, 0)])

        FoodClass.display(app, element_size, scale)
        snake.display(app, colors, scale, map_size, borders)
        display_len()
        snake.move()
        snake.check_collision(map_size, borders, FoodClass)
        if snake.dead:
            game_over = True
            game_over_screen()

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
