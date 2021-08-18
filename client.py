import pygame
from network import Network


width = 500
height = 500
window = pygame.display.set_mode((width, height))


def redrawWindow(window, player, opponent):
    window.fill((255, 255, 255))
    player.draw(window)
    opponent.draw(window)
    pygame.display.update()


def main():
    run = True
    n = Network()
    our_self = n.getPlayer()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        # Send our_self to server to get back opponent object
        opponent = n.send(our_self)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        our_self.move()
        redrawWindow(window, our_self, opponent)


main()
