import pygame

# Initialize Pygame
pygame.init()

# Set up game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Set up paddles
paddle_width = 10
paddle_height = 100
paddle_speed = 5
player_paddle = pygame.Rect(50, screen_height/2 - paddle_height/2, paddle_width, paddle_height)
computer_paddle = pygame.Rect(screen_width - 50 - paddle_width, screen_height/2 - paddle_height/2, paddle_width, paddle_height)

# Set up ball
ball_size = 10
ball_speed = 5
ball_rect = pygame.Rect(screen_width/2 - ball_size/2, screen_height/2 - ball_size/2, ball_size, ball_size)
ball_dx = ball_speed
ball_dy = ball_speed

# Set up scoring
font = pygame.font.SysFont("Arial", 30)
player_score = 0
computer_score = 0

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.move_ip(0, -paddle_speed)
    if keys[pygame.K_s] and player_paddle.bottom < screen_height:
        player_paddle.move_ip(0, paddle_speed)
    
    # Move ball
    ball_rect.move_ip(ball_dx, ball_dy)
    
    # Check for collisions with paddles
    if ball_rect.colliderect(player_paddle) or ball_rect.colliderect(computer_paddle):
        ball_dx *= -1
    
    # Check for collisions with walls
    if ball_rect.left < 0:
        computer_score += 1
        ball_rect = pygame.Rect(screen_width/2 - ball_size/2, screen_height/2 - ball_size/2, ball_size, ball_size)
        ball_dx = ball_speed
    if ball_rect.right > screen_width:
        player_score += 1
        ball_rect = pygame.Rect(screen_width/2 - ball_size/2, screen_height/2 - ball_size/2, ball_size, ball_size)
        ball_dx = -ball_speed
    if ball_rect.top < 0 or ball_rect.bottom > screen_height:
        ball_dy *= -1
    
    # Move computer paddle
    if computer_paddle.centery < ball_rect.centery and computer_paddle.bottom < screen_height:
        computer_paddle.move_ip(0, paddle_speed)
    elif computer_paddle.centery > ball_rect.centery and computer_paddle.top > 0:
        computer_paddle.move_ip(0, -paddle_speed)
    
    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player_paddle)
    pygame.draw.rect(screen, (255, 255, 255), computer_paddle)
    pygame.draw.ellipse(screen, (255, 255, 255), ball
