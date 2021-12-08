import pygame
OFFSET = 72
RADIUS = 28
color = {1: (255, 0, 0), -1: (0, 255, 0)}
FIRST_CENTER = 52
GAP_CENTERS = 68


class Piece(pygame.sprite.Sprite):

    def __init__(self, player, surf):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2*RADIUS, 2*RADIUS))
        pygame.draw.circle(self.image, color[player], (RADIUS, RADIUS), RADIUS)
        self.image.convert_alpha(surf)
        self.dropped = False
        self.rect = self.image.get_rect()
        self.updateCenter()

    def updateCenter(self):
        if not self.dropped:
            self.rect.center = (self.findClosestCenter(), OFFSET/2)

    def findClosestCenter(self):
        mouseX = pygame.mouse.get_pos()[0]
        closestX = -500
        for i in range(7):
            centeri = (FIRST_CENTER+GAP_CENTERS*i)
            if abs(mouseX - centeri) < abs(mouseX - closestX):
                closestX = centeri
        return closestX

    def dropPiece(self, logicBoard):
        column = int((self.rect.centerx-FIRST_CENTER)/GAP_CENTERS)
        self.dropped = logicBoard.dropPiece(column)
        return self.dropped
