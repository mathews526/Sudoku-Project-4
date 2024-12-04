import pygame

class Cell:
    def __init__(self, value, row, col, screen, cell_size=60):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.cell_size = cell_size
        self.selected = False # Whether the cell is currently selected


    def set_cell_value(self, value): # Setter for this cell's value
        if 0 <= value <= 9:
            self.value = value


    def set_sketched_value(self, value): # Setter for this cell's sketched value
        if 0 <= value <= 9:
            self.sketched_value = value


    # Draws this cell, along with the value inside it. If this cell has a nonzero value, that value is displayed.
    # Otherwise, no value is displayed in the cell. The cell is outlined red if it is currently selected.
    def draw(self):
        font = pygame.font.Font(None, 40)

        if self.value != 0: # Draws permanent value if not 0
            num_surf = font.render(str(self.value), 0, (66, 66, 66))

            # Centers the value in the cell
            x_center = self.col * self.cell_size + self.cell_size // 2
            y_center = self.row * self.cell_size + self.cell_size // 2

            # Sets area/bounding for the box
            num_rect = num_surf.get_rect(center=(x_center, y_center))
            self.screen.blit(num_surf, num_rect)

        elif self.sketched_value != 0: # If the cell value is 0 then it draws the sketched value.
            sketch_surf = font.render(str(self.sketched_value), 0, (150, 150, 150))

            # Offsets sketched value
            x_sketch_center = self.col * self.cell_size + 15
            y_sketch_center = self.row * self.cell_size + 15

            sketch_rect = sketch_surf.get_rect(center=(x_sketch_center, y_sketch_center))
            self.screen.blit(sketch_surf, sketch_rect)

        # Draws cell border and highlights red if currently selected.
        border_color = (255, 0, 0) if self.selected else (0, 0, 0)
        pygame.draw.rect(self.screen, border_color,(self.col * self.cell_size, self.row * self.cell_size, self.cell_size, self.cell_size), 3 if self.selected else 1)