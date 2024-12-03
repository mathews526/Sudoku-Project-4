import pygame

class Cell:
    def __init__(self, value, row, col, screen, cell_size=60):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.cell_size = cell_size
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        font = pygame.font.Font(None, 40)

        if self.value != 0:
            num_surf = font.render(str(self.value), 0, (66, 66, 66))

            x_center = self.col * self.cell_size + self.cell_size // 2
            y_center = self.row * self.cell_size + self.cell_size // 2

            num_rect = num_surf.get_rect(center=(x_center, y_center))
            self.screen.blit(num_surf, num_rect)
        elif self.sketched_value != 0:
            sketch_surf = font.render(str(self.sketched_value), 0, (150, 150, 150))
            x_sketch_center = self.col * self.cell_size // 4
            y_sketch_center = self.row * self.cell_size // 4
            sketch_rect = sketch_surf.get_rect(center=(x_sketch_center, y_sketch_center))
            self.screen.blit(sketch_surf, sketch_rect)

        border_color = (255, 0, 0) if self.selected else (0, 0, 0)
        pygame.draw.rect(self.screen, border_color,(self.col * self.cell_size, self.row * self.cell_size, self.cell_size, self.cell_size), 3 if self.selected else 1)