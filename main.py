import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys
def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  clock = pygame.time.Clock()
  dt = 0
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  Shot.containers = shots, updatable, drawable
  Asteroid.containers = asteroids, updatable, drawable
  Player.containers = updatable,drawable
  AsteroidField.containers = updatable
  player = Player(x= SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
  asteroidfield = AsteroidField()
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    screen.fill(color = 'black')
    for sprite in drawable:
      sprite.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60)/1000  # will pause the game loop until 1/60 th of a second has passed
    updatable.update(dt)
    for asteroid in asteroids:
      if asteroid.collision(player):
        sys.exit('Game Over!')
      for bullet in shots:
          if asteroid.collision(bullet):
            asteroid.split()
            bullet.kill()

    continue
    
if __name__ == "__main__":
  main()