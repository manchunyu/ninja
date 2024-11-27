import sys, pygame

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Ninja Game")
        SCREEN_SIZE  = (SCREEN_WIDTH, SCREEN_HEIGHT) = (640, 480)
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load("data/images/clouds/cloud_1.png")
        self.img.set_colorkey((0, 0, 0))
        self.img_pos = [300, 240]
        self.movement = [False, False]
        self.collision_area = pygame.Rect(50, 50, 300, 50)

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))
            
            self.img_r = pygame.Rect(*self.img_pos, *self.img.get_size())
            if self.img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 255, 0), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)

            self.img_pos[1] += self.movement[1] - self.movement[0]
            self.screen.blit(self.img, self.img_pos)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()