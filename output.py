# My attempt at mimicking the unity flight sim in pygame
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Flight Simulator")

# Colors
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)  # Sky color
GREEN = (34, 139, 34)  # Ground color

# Load airplane image
plane_img = pygame.image.load('plane.png')  # Replace with your own plane image file
plane_rect = plane_img.get_rect()
plane_speed = 5

# Game clock
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Control the plane's movement
    if keys[pygame.K_LEFT]:
        plane_rect.x -= plane_speed
    if keys[pygame.K_RIGHT]:
        plane_rect.x += plane_speed
    if keys[pygame.K_UP]:
        plane_rect.y -= plane_speed
    if keys[pygame.K_DOWN]:
        plane_rect.y += plane_speed

    # Prevent the plane from going off-screen
    if plane_rect.x < 0:
        plane_rect.x = 0
    if plane_rect.x > width - plane_rect.width:
        plane_rect.x = width - plane_rect.width
    if plane_rect.y < 0:
        plane_rect.y = 0
    if plane_rect.y > height - plane_rect.height:
        plane_rect.y = height - plane_rect.height

    # Fill the background with sky color
    screen.fill(BLUE)

    # Draw the ground
    pygame.draw.rect(screen, GREEN, (0, height - 100, width, 100))

    # Draw the plane
    screen.blit(plane_img, plane_rect)

    # Update the display
    pygame.display.update()

    # Set the frames per second
    clock.tick(60)
