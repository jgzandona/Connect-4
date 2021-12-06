import pygame

pygame.init()

board = pygame.image.load('data/board.png')
scale_factor = 0.8
board = pygame.transform.scale(board, (int(board.get_width()*scale_factor), int(board.get_height()*scale_factor)))

window = pygame.display.set_mode((board.get_width(),board.get_height()+50))

board = board.convert_alpha(window)

game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            game_over = True

    pygame.draw.circle(window, (0, 0, 0), (board.get_width(),board.get_height()), 1000)
    pygame.draw.circle(window, (255, 255, 255), pygame.mouse.get_pos(), 28)
    window.blit(board, (0, 50))
    pygame.time.delay(1)
    pygame.display.update()
    

pygame.quit()