import pygame
OFFSET = 72
RADIUS = 28
color = {1: (255, 0, 0), -1: (0, 255, 0)}


class Piece(pygame.sprite.Sprite):

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2*RADIUS, 2*RADIUS))
        pygame.draw.circle(self.image, color[player], (RADIUS, RADIUS), RADIUS)
        self.dropped = False
        self.rect = self.image.get_rect()
        self.updateCenter()

    def updateCenter(self):
        if not self.dropped:
            self.rect.center = (pygame.mouse.get_pos()[0], OFFSET/2)
