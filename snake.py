try:
    import pygame
except ImportError as e:
    raise ImportError("pygame is required to run Snake. Install it with 'pip install pygame'.") from e

import random
import sys

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELL_SIZE = 20
FPS = 8

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 24)
        self.big_font = pygame.font.SysFont('Arial', 48)
        self.running = True
        self.restart()

    def restart(self):
        self.snake_pos = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
        self.snake_body = [
            [self.snake_pos[0], self.snake_pos[1]],
            [self.snake_pos[0] - CELL_SIZE, self.snake_pos[1]],
            [self.snake_pos[0] - CELL_SIZE * 2, self.snake_pos[1]]
        ]
        self.direction = 'RIGHT'
        self.change_to = 'RIGHT'
        self.food_pos = self.random_food_position()
        self.food_spawn = True
        self.score = 0
        self.game_over = False

    def random_food_position(self):
        x = random.randrange(0, WINDOW_WIDTH // CELL_SIZE) * CELL_SIZE
        y = random.randrange(0, WINDOW_HEIGHT // CELL_SIZE) * CELL_SIZE
        return [x, y]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != 'DOWN':
                    self.change_to = 'UP'
                elif event.key == pygame.K_DOWN and self.direction != 'UP':
                    self.change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and self.direction != 'RIGHT':
                    self.change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and self.direction != 'LEFT':
                    self.change_to = 'RIGHT'
                elif event.key == pygame.K_r and self.game_over:
                    self.restart()
                elif event.key == pygame.K_q and self.game_over:
                    self.running = False

    def update(self):
        if self.game_over:
            return

        self.direction = self.change_to

        if self.direction == 'UP':
            self.snake_pos[1] -= CELL_SIZE
        elif self.direction == 'DOWN':
            self.snake_pos[1] += CELL_SIZE
        elif self.direction == 'LEFT':
            self.snake_pos[0] -= CELL_SIZE
        elif self.direction == 'RIGHT':
            self.snake_pos[0] += CELL_SIZE

        self.snake_body.insert(0, list(self.snake_pos))

        if self.snake_pos == self.food_pos:
            self.score += 1
            self.food_spawn = False
        else:
            self.snake_body.pop()

        if not self.food_spawn:
            self.food_pos = self.random_food_position()
            self.food_spawn = True

        if self.is_collision():
            self.game_over = True

    def is_collision(self):
        if (
            self.snake_pos[0] < 0
            or self.snake_pos[0] >= WINDOW_WIDTH
            or self.snake_pos[1] < 0
            or self.snake_pos[1] >= WINDOW_HEIGHT
        ):
            return True
        return self.snake_pos in self.snake_body[1:]

    def draw(self):
        self.screen.fill(BLACK)
        for block in self.snake_body:
            pygame.draw.rect(self.screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, RED, pygame.Rect(self.food_pos[0], self.food_pos[1], CELL_SIZE, CELL_SIZE))
        score_text = self.font.render(f'Score: {self.score}', True, WHITE)
        self.screen.blit(score_text, (10, 10))

        if self.game_over:
            self.draw_game_over()

        pygame.display.flip()

    def draw_game_over(self):
        game_over_text = self.big_font.render('Game Over', True, RED)
        restart_text = self.font.render('Press R to restart or Q to quit', True, WHITE)
        score_text = self.font.render(f'Final Score: {self.score}', True, WHITE)

        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 40))
        score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 10))
        restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))

        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(score_text, score_rect)
        self.screen.blit(restart_text, restart_rect)

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    SnakeGame().run()