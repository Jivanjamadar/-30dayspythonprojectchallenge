import pygame
import random


pygame.init()

#display
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blockfall Game")

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

#player blcok
player_width, player_height = 50, 80
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - player_height - 20
player_speed = 5

#obstacles
obstacle_width, obstacle_height = 50, 50
obstacles = []
obstacle_speed = 3
obstacle_frequency = 25
obstacle_counter = 0
block_size_increase = 0.1
block_size_color = (0, 255, 0) 

#game variables
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
game_over = False

#text on screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    SCREEN.blit(text_surface, text_rect)

#loop
running = True
while running:
    SCREEN.fill(BLACK)

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        #movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        #bounding player
        if player_x < 0:
            player_x = 0
        if player_x > WIDTH - player_width:
            player_x = WIDTH - player_width

    
        if obstacle_counter % obstacle_frequency == 0:
            obstacle_x = random.randint(0, WIDTH - obstacle_width)
            obstacle_y = -obstacle_height
            obstacles.append(pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height))
        obstacle_counter += 1

        #move & color
        for obstacle in obstacles:
            obstacle.y += obstacle_speed
            pygame.draw.rect(SCREEN, RED, obstacle)

            #collison detection
            if obstacle.colliderect((player_x, player_y, player_width, player_height)):
                game_over = True

            #remove passed obsticles
            if obstacle.top > HEIGHT:
                obstacles.remove(obstacle)
                score += 1
                if score % 50 == 0:
                    #increase obstacle size
                    obstacle_width = int(obstacle_width * (1 + block_size_increase))
                    obstacle_height = int(obstacle_height * (1 + block_size_increase))
                if score % 100 == 0:
                    obstacle_speed += 1  #increase obstacle speed

        #player block
        pygame.draw.rect(SCREEN, WHITE, (player_x, player_y, player_width, player_height))

        #draw score
        draw_text(f"Score: {score}", font, WHITE, 10, 10)

        #draw obstacle speed
        draw_text(f"Speed: {obstacle_speed}", font, WHITE, WIDTH - 150, 10)
    else:
        #draw game over message
        draw_text("Game Over !", font, WHITE, WIDTH // 2 - 100, HEIGHT // 2 - 50)
        draw_text(f"Final Score: {score}", font, WHITE, WIDTH // 2 - 100, HEIGHT // 2)
        draw_text("Press 'R' to Restart", font, WHITE, WIDTH // 2 - 150, HEIGHT // 2 + 50)

        #'R' for restart
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            game_over = False
            score = 0
            player_x = (WIDTH - player_width) // 2
            obstacles.clear()
            obstacle_speed = 3

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
