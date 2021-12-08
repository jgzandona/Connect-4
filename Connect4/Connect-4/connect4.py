import pygame
import piece
import logicBoard
OFFSET = 72

pygame.init()

board = pygame.image.load('data/board.png')
scale_factor = 0.8
board = pygame.transform.scale(
    board, (int(board.get_width()*scale_factor), int(board.get_height()*scale_factor)))

window = pygame.display.set_mode(
    (board.get_width(), board.get_height()+OFFSET))

board = board.convert_alpha(window)
background = pygame.Surface((1000, 1000))
background.fill((0, 0, 0))
background.blit(board, (0, OFFSET))

game_over = False

piece1 = piece.Piece(1, background)
pieceGroup = pygame.sprite.Group()
pieceGroup.add(piece1)
window.blit(board, (0, OFFSET))
logicBoard = logicBoard.LogicBoard()
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(piece1.dropPiece(logicBoard))
    piece1.updateCenter()
    pieceGroup.clear(window, background)
    pieceGroup.draw(window)
    pygame.time.delay(1)
    pygame.display.update()


pygame.quit()
