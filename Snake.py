import pygame


class Snake:
    def __init__(self, elements):
        super().__init__()
        self.lenght = len(elements)
        self.elements = elements
        self.head = self.elements[0]
        self.dir = 'E'
        self.key_lock = False
        self.reserve = [[], []]
        self.dead = False

    def display(self, app, colors, element_size, map_size, borders):
        color_index = 0
        for element in self.elements[1:]:
            pygame.draw.circle(app, colors[color_index],
                               (element[0] * element_size + element_size // 2,
                                element[1] * element_size + element_size // 2),
                               element_size // 2 - 2)
            color_index = (color_index + 1) % len(colors)

        pygame.draw.circle(app, colors[3],
                           (self.head[0] * element_size + element_size // 2,
                            self.head[1] * element_size + element_size // 2),
                           element_size // 2 - 2)

        eye_radius = int(element_size * 0.15)
        eye_offset = int(element_size * 0.3)
        eye_y = self.head[1] * element_size + int(element_size * 0.35)
        mouth_y = self.head[1] * element_size + int(element_size * 0.7)

        pygame.draw.circle(app, colors[1],
                           (self.head[0] * element_size + eye_offset, eye_y),
                           eye_radius)
        pygame.draw.circle(app, colors[1],
                           (self.head[0] * element_size + element_size - eye_offset, eye_y),
                           eye_radius)

        pupil_radius = int(element_size * 0.05)
        pygame.draw.circle(app, colors[0],
                           (self.head[0] * element_size + eye_offset, eye_y),
                           pupil_radius)
        pygame.draw.circle(app, colors[0],
                           (self.head[0] * element_size + element_size - eye_offset, eye_y),
                           pupil_radius)

        pygame.draw.line(app, colors[0], (self.head[0] * element_size + int(element_size * 0.3), mouth_y),
                         (self.head[0] * element_size + int(element_size * 0.7), mouth_y), 3)

    def move(self):
        self.reserve[1] = self.reserve[0]
        self.reserve[0] = self.elements[-1]
        for i in range(self.lenght - 1, 0, -1):
            self.elements[i] = self.elements[i - 1]
        if self.dir == 'E':
            self.elements[0] = [self.elements[0][0] + 1, self.elements[0][1]]
        elif self.dir == 'S':
            self.elements[0] = [self.elements[0][0], self.elements[0][1] + 1]
        elif self.dir == 'W':
            self.elements[0] = [self.elements[0][0] - 1, self.elements[0][1]]
        elif self.dir == 'N':
            self.elements[0] = [self.elements[0][0], self.elements[0][1] - 1]
        self.head = self.elements[0]
        self.key_lock = False

    def check_collision(self, map_size, borders, food):
        for i in range(self.lenght - 1, 0, -1):
            if self.elements[i] == self.head:
                self.dead = True
        if not borders:
            if self.head[0] >= map_size:
                self.head[0] = 0
            elif self.head[0] < 0:
                self.head[0] = map_size
            elif self.head[1] >= map_size:
                self.head[1] = 0
            elif self.head[1] < 0:
                self.head[1] = map_size
            self.elements[0] = self.head
        else:
            if self.head[0] >= map_size or self.head[0] < 0 or self.head[1] >= map_size or self.head[1] < 0:
                self.dead = True
        if self.head == food.pos:
            if food.type == 0:
                self.grow(2)
            else:
                self.grow(1)
            food.spawn(map_size, self.elements)

    def grow(self, amount):
        self.lenght += amount
        for i in range(0, amount):
            self.elements.append(self.reserve[i])

    def restart(self, elements):
        self.lenght = len(elements)
        self.elements = elements
        self.head = self.elements[0]
        self.dir = 'E'
        self.key_lock = False
        self.reserve = [[], []]
        self.dead = False
