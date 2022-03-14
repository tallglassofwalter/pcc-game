import pygame

class Ship():
  def __init__(self, screen):
    """initialize the ship and its starting position"""
    self.screen = screen

    # load ship image and get its rect attribute
    self.image = pygame.image.load('./images/ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    # start with new ship at bottom center of screen
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

  def blitme(self):
    """draw ship at its current location"""
    self.screen.blit(self.image, self.rect)