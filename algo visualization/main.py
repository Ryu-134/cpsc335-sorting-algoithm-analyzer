import pygame
import sys
import random
from sorters import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 60

# Colors
BACKGROUND_COLOR = (24, 29, 39)
BAR_COLOR = (200, 200, 200)
HIGHLIGHT_COLOR = (255, 82, 82)
PIVOT_COLOR = (82, 113, 255)
TEXT_COLOR = (255, 255, 255)
UI_BACKGROUND_COLOR = (44, 51, 64)

# Bar properties
MIN_BAR_HEIGHT = 5
MAX_BAR_HEIGHT = WINDOW_HEIGHT - 200 # Leave space for UI
BAR_WIDTH = 5

class SorterVisualizer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.array = []
        self.pivot_index = -1
        self.paused = False

        self.array_size = 100
        self.sorting_speed = 10 # Yields per frame

        self.available_algorithms = {
            "Bubble Sort": bubble_sort,
            "Insertion Sort": insertion_sort,
            "Selection Sort": selection_sort,
            "Merge Sort": merge_sort,
            "Quick Sort": quick_sort
        }
        self.algorithm_names = list(self.available_algorithms.keys())
        self.current_algorithm_index = 0
        self.font = pygame.font.SysFont('Arial', 18)
        self.title_font = pygame.font.SysFont('Arial', 28, bold=True)
        
        self.reset_array()

    def reset_array(self):
        self.array = [random.randint(MIN_BAR_HEIGHT, MAX_BAR_HEIGHT) for _ in range(self.array_size)]
        self.is_sorting = False
        self.sorting_algorithm_generator = None
        self.clear_highlight()
        self.clear_pivot()
        self.paused = False

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset_array()
                if event.key == pygame.K_SPACE and not self.is_sorting:
                    self.start_sorting()
                if event.key == pygame.K_p and self.is_sorting:
                    self.paused = not self.paused
                if event.key == pygame.K_RIGHT and not self.is_sorting:
                    self.current_algorithm_index = (self.current_algorithm_index + 1) % len(self.algorithm_names)
                if event.key == pygame.K_LEFT and not self.is_sorting:
                    self.current_algorithm_index = (self.current_algorithm_index - 1) % len(self.algorithm_names)
                if event.key == pygame.K_UP and not self.is_sorting:
                    self.array_size = min(500, self.array_size + 10)
                    self.reset_array()
                if event.key == pygame.K_DOWN and not self.is_sorting:
                    self.array_size = max(10, self.array_size - 10)
                    self.reset_array()
                if event.key == pygame.K_EQUALS: # '+' key
                    self.sorting_speed = min(1000, self.sorting_speed + 10)
                if event.key == pygame.K_MINUS: # '-' key
                    self.sorting_speed = max(1, self.sorting_speed - 10)


    def start_sorting(self):
        self.is_sorting = True
        self.paused = False
        algorithm_name = self.algorithm_names[self.current_algorithm_index]
        sort_function = self.available_algorithms[algorithm_name]
        self.sorting_algorithm_generator = sort_function(self.array, self)

    def update(self):
        if self.is_sorting and not self.paused:
            for _ in range(self.sorting_speed):
                try:
                    next(self.sorting_algorithm_generator)
                except StopIteration:
                    self.is_sorting = False
                    self.sorting_algorithm_generator = None
                    self.clear_highlight()
                    self.clear_pivot()
                    break

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_bars()
        self.draw_ui()
        pygame.display.flip()
        
    def draw_ui(self):
        # Draw UI background panel
        pygame.draw.rect(self.screen, UI_BACKGROUND_COLOR, (0, 0, WINDOW_WIDTH, 120))
        pygame.draw.line(self.screen, BAR_COLOR, (0, 120), (WINDOW_WIDTH, 120), 2)

        # Title
        title_text = self.title_font.render("Sorting Algorithm", True, TEXT_COLOR)
        self.screen.blit(title_text, (20, 20))

        # Algorithm Name
        algorithm_name = self.algorithm_names[self.current_algorithm_index]
        algo_text = self.font.render(f"Algorithm: {algorithm_name}", True, TEXT_COLOR)
        self.screen.blit(algo_text, (20, 70))

        # Controls
        controls_text = self.font.render("R: Reset | P: Pause | Space: Start | <- ->: Change Algorithm", True, TEXT_COLOR)
        self.screen.blit(controls_text, (350, 30))

        # Size and Speed
        size_speed_text = self.font.render(f"Size: {self.array_size} (Up/Down) | Speed: {self.sorting_speed} (+/-)", True, TEXT_COLOR)
        self.screen.blit(size_speed_text, (350, 70))

        if self.paused:
            pause_text = self.font.render("PAUSED", True, HIGHLIGHT_COLOR)
            text_rect = pause_text.get_rect(center=(WINDOW_WIDTH - 100, 50))
            self.screen.blit(pause_text, text_rect)

    def draw_bars(self):
        if not self.array:
            return

        bar_width = WINDOW_WIDTH / len(self.array)
        bar_spacing = 0.8 # Percentage of bar_width to use for the bar itself
        
        for i, val in enumerate(self.array):
            x = i * bar_width
            # Bars grow from the bottom, leaving space for the UI panel
            y = WINDOW_HEIGHT - val
            
            bar_color = BAR_COLOR
            if i in self.highlighted:
                bar_color = HIGHLIGHT_COLOR
            if i == self.pivot_index:
                bar_color = PIVOT_COLOR
            
            pygame.draw.rect(self.screen, bar_color, (x, y, bar_width * bar_spacing, val))

    def set_highlight(self, indices):
        self.highlighted = indices

    def clear_highlight(self):
        self.highlighted = []

    def set_pivot(self, index):
        self.pivot_index = index

    def clear_pivot(self):
        self.pivot_index = -1

    def quit(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    visualizer = SorterVisualizer()
    visualizer.run()
    visualizer.quit()
