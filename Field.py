import pygame


class Field:
    def __init__(self, map_size, scale, borders):
        self.map_size = map_size
        self.scale = scale
        self.borders = borders

    def display(self, app, colors):
        app.fill(colors[0])
        for x in range(0, self.map_size[0], 2):
            for y in range(0, self.map_size[1], 2):
                pygame.draw.rect(app, colors[1], [x * self.scale, y * self.scale, self.scale, self.scale])
        for x in range(1, self.map_size[0], 2):
            for y in range(1, self.map_size[1], 2):
                pygame.draw.rect(app, colors[1], [x * self.scale, y * self.scale, self.scale, self.scale])

        if self.borders:
            pygame.draw.rect(app, colors[2], [0, 0, self.map_size[0] * self.scale, self.map_size[1] * self.scale], 1)
