import pygame
from network import Network


width = 500
height = 500
window = pygame.display.set_mode((width, height))


def redrawWindow(window, player, player2):
    window.fill((255, 255, 255))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()


def main():
    run = True
    n = Network()
    player1 = n.getPlayer()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        # Send player1 to server to get back player2 object
        player2 = n.send(player1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        player1.move()
        redrawWindow(window, player1, player2)


main()
