import os
import pygame
from pygame import Color

pygame.init()

white = (248, 249, 250)
dark_blue = (9, 10, 31)
sky_blue = (127, 199, 255)

win = pygame.display.set_mode((300, 400))
pygame.display.set_caption('Главное меню')


class Button:
    def __init__(self, color, x, y, width, height, text='', action=None, text_color=dark_blue):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.action = action
        self.text_color = text_color

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 20)
            text = font.render(self.text, 1, self.text_color)
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos_):
        if pos_[0] > self.x and pos_[0] < self.x + self.width:
            if pos_[1] > self.y and pos_[1] < self.y + self.height:
                self.color = (218, 219, 220)
                return True
        self.color = white
        return False

    def is_not_over(self):
        self.color = white


def open_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print('Файл не найден')


def sub_menu():
    running = True
    pygame.display.set_caption('Настройки')

    button1 = Button(white, 50, 100, 200, 50, 'Окрас змейки', action=lambda: open_color_menu())
    button2 = Button(white, 50, 200, 200, 50, 'Громкость звуков', action=lambda: print('не реализованно'))
    back_button = Button(white, 10, 10, 30, 30, '<--', action=lambda: main_menu(), text_color=dark_blue)

    buttons = [button1, button2, back_button]

    while running:
        win.fill(sky_blue)
        back_button.draw(win)
        for button in buttons:
            button.draw(win)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.is_over(pos):
                        button.is_over(pos)
                    else:
                        button.is_not_over()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.is_over(pos):
                        if button.action:
                            button.action()


def open_color_menu():
    pygame.display.set_caption('Не реализованно:(')
    color_menu_running = True
    color_buttons = []

    colors = [Color('red'), Color('orange'), Color('yellow'), Color('green'), Color('blue'), Color('indigo'),
              Color('violet'), Color('white')]

    color_names = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'White']

    button_height = 80
    top_margin = 15
    bottom_margin = 25
    row_gap = 20
    rows = 4
    cols = (len(colors) + 1) // rows

    back_button = Button(white, 10, 10, 30, 30, '<--', action=lambda: main_menu(), text_color=dark_blue)

    for i in range(len(colors)):
        row = i // cols
        col = i % cols
        x = 60 + col * 100
        y = top_margin + row * ((bottom_margin - top_margin - row_gap) // (rows - 1) + button_height + row_gap)
        color_buttons.append(Button(colors[i], x, y, 80, 80, color_names[i]))

    while color_menu_running:
        win.fill(sky_blue)

        back_button.draw(win)

        for button in color_buttons:
            button.draw(win)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                color_menu_running = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_over(pygame.mouse.get_pos()):
                    back_button.action()


def show_rules():
    rules_window = pygame.display.set_mode((300, 400))
    pygame.display.set_caption('Правила игры')

    running = True
    while running:
        rules_window.fill((176, 224, 230))

        back_button = Button(white, 10, 10, 30, 30, '<--', action=lambda: main_menu(), text_color=dark_blue)
        back_button.draw(rules_window)

        font = pygame.font.Font(None, 15)
        text_lines = [
            "1. Игра представляет собой видоизмененную змейку,",
            "содержащую несколько уровней.",
            "2. В меню игры можно изменить громкость звука и",
            "внешний облик змейки.",
            "3. Цель игрока - собирать различную еду, достигать",
            "поставленные на уровнях цели и уворачиваться от ",
            "различных препятствий.",
            "4. В игре присутствует экран паузы.",
            "Чтобы открыть его, во время игры нажмите 'Space'",
            "",
            "",
            "                                  Автор:",
            "глупый Максим, который решил сделать змейку",
            "вместо Tower Defence...",
            "",
            "",
            "                          Удачной игры!!!"
        ]
        y_offset = 50
        for line in text_lines:
            text = font.render(line, True, dark_blue)
            rules_window.blit(text, (15, y_offset))
            y_offset += 20

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if back_button.is_over(pos):
                    back_button.action()
                    pygame.display.set_caption('Главное меню')


def main_menu():
    pygame.display.set_caption('Главное меню')
    running = True

    play_button = Button(white, 50, 150, 200, 50, 'Играть', action=lambda: os.system('python Run.py'))
    rules_button = Button(white, 50, 50, 200, 50, 'Правила игры', action=lambda: show_rules())
    encyclopedia_button = Button(white, 50, 250, 200, 50, 'Настройки', action=lambda: sub_menu())

    buttons = [play_button, rules_button, encyclopedia_button]

    while running:
        win.fill(sky_blue)
        for button in buttons:
            button.draw(win)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.is_over(pos):
                        button.is_over(pos)
                    else:
                        button.is_not_over()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.is_over(pos):
                        if button.action:
                            button.action()


main_menu()
show_rules()
