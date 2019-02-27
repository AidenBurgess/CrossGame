# Pygame Development
# Cross GAME
# Play as Link and try to cross the road to get treasure
# By: Aiden Burgess

import pygame
import random
import game_object


# Screen properties
SCREEN_TITLE = 'Cross x Crime'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
# Clock of game
clock = pygame.time.Clock()
pygame.font.init()
# Initiate fonts
large_font = pygame.font.SysFont('comicsans', 75)
level_font = pygame.font.SysFont('calibri', 30)
level_font.set_bold(True)


def text_objects(text, color, text_font):
    textSurface = text_font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen_center(surface, msg, color, text_font,y):
    textSurf, textRect = text_objects(msg, color, text_font)
    textRect.center = SCREEN_WIDTH / 2, y
    surface.blit(textSurf, textRect)


def message_to_screen_left(surface, msg, color, font, x, y):
    textSurf, textRect = text_objects(msg, color, font)
    surface.blit(textSurf, (x, y))


class Game:
    # Tick rate AKA FPS
    TICK_RATE = 120
    MEDIUM_LEVEL = 2
    HARD_LEVEL = 3
    WIN_LEVEL = 4 + 1.5

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        # Screen set-up
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    def start_game(self):
        slime_0 = game_object.NPC(
            'NPC/Slime.png', random.randrange(20, 700), 500, 50, 50)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        return
                    elif event.key == pygame.K_x:
                        self.run_game_loop(1)
            # Render background
            self.game_screen.fill(WHITE)
            self.game_screen.blit(self.image, (0, 0))
            # Display main menu text
            message_to_screen_left(
                self.game_screen, 'CROSS GAME', BLACK, large_font, 150, 150)
            message_to_screen_left(
                self.game_screen, 'Try and cross the road', BLACK, level_font, 150, 230)
            message_to_screen_left(
                self.game_screen, 'Controls: ', BLACK, level_font, 150, 300)
            message_to_screen_left(
                self.game_screen, 'Arrow Keys - Move Link ', BLACK, level_font, 150, 330)
            message_to_screen_left(
                self.game_screen, 'Esc or Q - Pause', BLACK, level_font, 150, 360)
            message_to_screen_left(
                self.game_screen, 'X - Boost', BLACK, level_font, 150, 390)
            message_to_screen_left(
                self.game_screen, 'Press X to start', BLACK, large_font, 150, 450)
            message_to_screen_left(
                self.game_screen, 'Press Q or esc to quit', BLACK, large_font, 150, 550)
            slime_0.move(self.width)
            slime_0.draw(self.game_screen)
            pygame.display.update()

    def pause(self):
        # Render background
        image = pygame.Surface([self.width, self.height])
        image.fill(BLACK)
        # image = pygame.Surface([640,480], pygame.SRCALPHA, 32)
        image.set_alpha(100)
        # image = image.convert_alpha()
        self.game_screen.blit(image, (0, 0))
        # Render text
        message_to_screen_center(
            self.game_screen, 'You have paused', RED, large_font, 50)
        message_to_screen_center(
            self.game_screen, 'Press X to continue', WHITE, large_font, 200)
        message_to_screen_center(
            self.game_screen, 'Press Q or esc to return', WHITE, large_font, 330)
        message_to_screen_center(
            self.game_screen, 'to Main Menu', WHITE, large_font, 380)
        # Update screen
        pygame.display.update()
        # Pause options checking
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        return True
                    elif event.key == pygame.K_x:
                        return False

    def win_game(self):
        slime_0 = game_object.NPC(
            'NPC/Slime.png', random.randrange(20, 700), 500, 50, 50)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        return False
                    elif event.key == pygame.K_r:
                        return True
            # Render winning text
            self.game_screen.fill(WHITE)
            message_to_screen_left(
                self.game_screen, 'You Won!', BLUE, large_font, 100, 50)
            message_to_screen_left(
                self.game_screen, 'Press R to Play Again', RED, large_font, 150, 200)
            message_to_screen_left(
                self.game_screen, 'Press Q or Esc', RED, large_font, 150, 350)
            message_to_screen_left(
                self.game_screen, 'to go to main menu', RED, large_font, 150, 400)
            # Display the winner slime
            slime_0.move(self.width)
            slime_0.draw(self.game_screen)
            pygame.display.update()

    def lose_game(self):
        message_to_screen_left(
            self.game_screen, 'You lost sorry...', RED, large_font, 200, 350)
        pygame.display.update()
        clock.tick(1)

    def game_restart(self):
        slime_0 = game_object.NPC(
            'NPC/Slime.png', random.randrange(20, 700), 500, 50, 50)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN \
                and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
                    return False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    return True
            # Display text for losing
            self.game_screen.fill(WHITE)
            message_to_screen_center(
                self.game_screen, 'You lost...', RED, large_font, 50)
            message_to_screen_center(
                self.game_screen, 'Press R to Restart', RED, large_font, 200)
            message_to_screen_center(
                self.game_screen, 'Press Q or esc to quit', RED, large_font, 300)
            # Have the loser slime dance around lol
            slime_0.move(self.width)
            slime_0.draw(self.game_screen)
            pygame.display.update()

    def run_game_loop(self, level):
        game_over = False
        did_win = True
        boost = 1

        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('LEVEL: ', level)

        # Draw player + first slime+ treasure
        particle = game_object.GameObject(
            'particle/Particle1.png', 500, 500, 50, 50)
        count = 1
        player = game_object.PC(
            'PC/Zelda.png', self.width / 2 - 25, self.height * 0.85, 50, 70)
        slime_0 = game_object.NPC('NPC/Slime.png', random.randrange(20, 300), 500, 50, 50)
        slime_0.BASE_SPEED *= level
        treasure = game_object.GameObject('NPC/Treasure.png', self.width / 2 - 45, 30, 100, 70)
        # Draw harder slimes
        if level > self.MEDIUM_LEVEL:
            slime_1 = game_object.NPC(
                'NPC/Slime.png', random.randrange(20, 700), 300, 50, 50)
            slime_1.BASE_SPEED *= level
        if level > self.HARD_LEVEL:
            slime_2 = game_object.NPC(
                'NPC/Slime.png', random.randrange(20, 700), 150, 50, 50)
            slime_2.BASE_SPEED *= level
            slime_2.move(self.width)
            slime_2.draw(self.game_screen)

        while not game_over:
            for event in pygame.event.get():
                # Quit if player tries to exit
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_q):
                    if self.pause():
                        return
            # Determine keypresses to determine dirx and diry
            dir_x = 0
            dir_y = 0
            boost = 1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                dir_y = 1
            if keys[pygame.K_DOWN]:
                dir_y = -1
            if keys[pygame.K_LEFT]:
                dir_x = -1
            if keys[pygame.K_RIGHT]:
                dir_x = 1
            if keys[pygame.K_x]:
                boost = 2
            # Redraw screen
            self.game_screen.fill(WHITE)
            self.game_screen.blit(self.image, (0, 0))
            # Draw GameObjects
            treasure.draw(self.game_screen)
            slime_0.move(self.width)
            slime_0.draw(self.game_screen)
            if level > self.MEDIUM_LEVEL:
                slime_1.move(self.width)
                slime_1.draw(self.game_screen)
            if level > self.HARD_LEVEL:
                slime_2.move(self.width)
                slime_2.draw(self.game_screen)
            # Draw player
            player.move(dir_x, dir_y, self.width, self.height, boost)
            player.draw(self.game_screen, dir_x, dir_y)
            # Render boost effects
            if boost > 1:
                object_image = pygame.image.load(
                    'particle/Particle' + str(count // 6 + 1) + '.png')
                particle.image = pygame.transform.scale(
                    object_image, (particle.width, particle.height))
                # Offset the particle to be roughly mid-body
                particle.x_pos = player.x_pos + 3
                particle.y_pos = player.y_pos + 30
                count += 1
                if count == 60:
                    count = 1
                particle.draw(self.game_screen)
            # Display level counter in corner
            message_to_screen_left(
                self.game_screen, 'Level ' + str(int((level - 1) * 2 + 1)), WHITE, level_font, 0, 0)
            # Detect collision
            try:
                collision = self.detect_all_collisions(
                    level, player, slime_0, slime_1, slime_2, treasure)
            except:
                try:
                    collision = self.detect_all_collisions(
                        level, player, slime_0, slime_1, 0, treasure)
                except:
                    collision = self.detect_all_collisions(
                        level, player, slime_0, 0, 0, treasure)

            if collision == 'dead':
                did_win = False
                break
            elif collision == 'treasure':
                break

            pygame.display.update()
            clock.tick(self.TICK_RATE)
        # Increment game or return to level one or go to main menu
        if did_win:
            if level >= self.WIN_LEVEL:
                self.win_game()
            else:
                message_to_screen_left(
                    self.game_screen, 'Level ' + str(int((level - 1) * 2 + 1)), WHITE, level_font, 0, 0)

                self.run_game_loop(level + 0.5)
        elif self.game_restart():
            self.run_game_loop(1)
        else:
            return

    def detect_all_collisions(self, level, player, slime_0, slime_1, slime_2, treasure):
        '''Detect collision between player and (slimes and treasure)'''
        dead = 0
        if level > self.HARD_LEVEL:
            dead += player.detect_collision(slime_2)
        if level > self.MEDIUM_LEVEL:
            dead += player.detect_collision(slime_1)
        dead += player.detect_collision(slime_0)
        if dead:
            self.lose_game()
            return 'dead'

        if player.detect_collision(treasure):
            message_to_screen_center(self.game_screen, 'Next Up, Level ' + str(
                int(level * 2)), WHITE, large_font, self.height / 2)
            pygame.display.update()
            clock.tick(1)
            return 'treasure'


# Start the game up
pygame.init()
new_game = Game('NPC/background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.start_game()

# After game is finished quit the program
pygame.quit()
quit()
