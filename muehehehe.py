import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720)) #Tell the program what resolution to be!
clock = pygame.time.Clock()
running = True
dt = 5 #This is needed for timing
player_location = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill('purple')
  pygame.draw.circle(screen, 'red', player_location, 40)
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    player_location.y -= 300 * dt
  if keys[pygame.K_s]:
    player_location.y += 300 * dt
  if keys[pygame.K_a]:
    player_location.x -= 300 * dt
  if keys[pygame.K_d]:
    player_location.x += 300 * dt
  pygame.display.flip()
  dt = clock.tick(60) / 1000
pygame.quit()