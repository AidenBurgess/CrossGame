#Pygame Development
#Cross GAME
# Play as Link and try to cross the road to get treasure
#By: Aiden Burgess

import pygame
import random

#Screen properties
SCREEN_TITLE = 'Cross x Crime'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
#Clock of game
clock = pygame.time.Clock()
pygame.font.init()
#Initiate fonts
large_font = pygame.font.SysFont('comicsans', 75)
level_font = pygame.font.SysFont('calibri', 30)
level_font.set_bold(True)

def text_objects(text, color, text_font):
    textSurface = text_font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen_center(surface, msg, color, text_font, x, y):
    textSurf, textRect = text_objects(msg, color, text_font)
    textRect.center = x, y
    surface.blit(textSurf, textRect)

def message_to_screen_left(surface, msg, color, font,x , y):
    textSurf, textRect = text_objects(msg, color, font)
    #textRect.center = x, y
    surface.blit(textSurf, (x, y))

class Game:
    #Tick rate AKA FPS
    TICK_RATE = 120
    MEDIUM_LEVEL = 2
    HARD_LEVEL = 3
    WIN_LEVEL = 4 + 1.5

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        #Screen set-up
        self.game_screen = pygame.display.set_mode((width,height))
        self.game_screen.fill(WHITE)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))

    def start_game(self):
        slime_0 = NonPlayerCharacter('Slime.png', random.randrange(20, 700), 500, 50, 50)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        return
                    elif event.key == pygame.K_x:
                        self.run_game_loop(1)
            #Render background
            self.game_screen.fill(WHITE)
            self.game_screen.blit(self.image, (0,0))
            #Display main menu text
            message_to_screen_left(self.game_screen, 'CROSS GAME', BLACK, large_font,150 , 150)
            message_to_screen_left(self.game_screen, 'Try and cross the road', BLACK, level_font,150 , 230)
            message_to_screen_left(self.game_screen, 'Controls: ', BLACK, level_font,150 , 300)
            message_to_screen_left(self.game_screen, 'Arrow Keys - Move Link ', BLACK, level_font,150 , 330)
            message_to_screen_left(self.game_screen, 'Esc or Q - Pause', BLACK, level_font,150 , 360)
            message_to_screen_left(self.game_screen, 'X - Boost', BLACK, level_font,150 , 390)
            message_to_screen_left(self.game_screen, 'Press X to start', BLACK, large_font,150 , 450)
            message_to_screen_left(self.game_screen, 'Press Q or esc to quit', BLACK, large_font,150 , 550)
            slime_0.move(self.width)
            slime_0.draw(self.game_screen)
            pygame.display.update()

    def pause(self):
        #Render background
        image = pygame.Surface([self.width,self.height])
        image.fill(BLACK)
        #image = pygame.Surface([640,480], pygame.SRCALPHA, 32)
        image.set_alpha(100)
        #image = image.convert_alpha()
        self.game_screen.blit(image, (0,0))
        #Render text
        message_to_screen_left(self.game_screen, 'You have paused', RED, large_font, 100, 50)
        message_to_screen_left(self.game_screen, 'Press X to continue', WHITE, large_font, 150, 200)
        message_to_screen_left(self.game_screen, 'Press Q or esc to return', WHITE, large_font, 80, 330)
        message_to_screen_left(self.game_screen, 'to Main Menu', WHITE, large_font, 200, 380)
        #Update screen
        pygame.display.update()
        #Pause options checking
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
        slime_0 = NonPlayerCharacter('Slime.png', random.randrange(20, 700), 500, 50, 50)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        return False
                    elif event.key == pygame.K_r:
                        return True
            #Render winning text
            self.game_screen.fill(WHITE)
            message_to_screen_left(self.game_screen, 'You Won!', BLUE, large_font,100 , 50)
            message_to_screen_left(self.game_screen, 'Press R to Play Again', RED, large_font,150 , 200)
            message_to_screen_left(self.game_screen, 'Press Q or Esc', RED, large_font,150 , 350)
            message_to_screen_left(self.game_screen, 'to go to main menu', RED, large_font,150 , 400)
            #Display the winner slime
            slime_0.move(self.width)
            slime_0.draw(self.game_screen)
            pygame.display.update()

    def lose_game(self):
        game_over = True
        message_to_screen_left(self.game_screen, 'Suck my ass lmao', RED, large_font,200 , 350)
        pygame.display.update()
        clock.tick(1)

    def game_restart(self):
        slime_0 = NonPlayerCharacter('Slime.png', random.randrange(20, 700), 500, 50, 50)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE)):
                    return False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    return True
            #Display text for losers
            self.game_screen.fill(WHITE)
            message_to_screen_left(self.game_screen, 'You lost my easy ass game', RED, large_font,100 , 50)
            message_to_screen_left(self.game_screen, 'Press R to Restart', RED, large_font,150 , 200)
            message_to_screen_left(self.game_screen, 'Press Q or esc to quit', RED, large_font,150 , 300)
            #Have the loser slime dance around lol
            slime_0.move(self.width)
            slime_0.draw(self.game_screen)
            pygame.display.update()

    def run_game_loop(self, level):
        game_over = False
        did_win = True
        dir_y=dir_x=down= up= left= right = 0
        boost = 1

        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('LEVEL: ', level)

        #Draw player + first slime+ treasure
        particle = GameObject('particle effects/Particle1.png', 500 ,500, 50, 50)
        count = 1
        player= PlayerCharacter('Zelda.png', self.width/2-25, self.height *0.85, 50, 70)
        slime_0 = NonPlayerCharacter('Slime.png', random.randrange(20, 300), 500, 50, 50)
        slime_0.BASE_SPEED*= level
        treasure = GameObject('Treasure.png', self.width/2 - 45, 30, 100, 70)
        #Draw harder slimes
        if level > self.MEDIUM_LEVEL:
            slime_1 = NonPlayerCharacter('Slime.png', random.randrange(20, 700), 300, 50, 50)
            slime_1.BASE_SPEED*= level
        if level > self.HARD_LEVEL:
            slime_2 = NonPlayerCharacter('Slime.png', random.randrange(20, 700), 150, 50, 50)
            slime_2.BASE_SPEED*= level
            slime_2.move(self.width)
            slime_2.draw(self.game_screen)

        while not game_over:
            for event in pygame.event.get():
               #Quit if player tries to exit
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_ESCAPE or event.key == pygame.K_q):
                    if self.pause():
                        return
            #Determine keypresses to determine dirx and diry
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
            #Redraw screen
            self.game_screen.fill(WHITE)
            self.game_screen.blit(self.image, (0,0))
            #Draw GameObjects
            treasure.draw(self.game_screen)
            slime_0.move(self.width)
            slime_0.draw(self.game_screen)
            if level > self.MEDIUM_LEVEL:
                slime_1.move(self.width)
                slime_1.draw(self.game_screen)
            if level > self.HARD_LEVEL:
                slime_2.move(self.width)
                slime_2.draw(self.game_screen)
            #Draw player
            player.move(dir_x, dir_y, self.width, self.height,boost)
            player.draw(self.game_screen, dir_x, dir_y)
            #Render boost effects
            if boost > 1:
                object_image = pygame.image.load('particle effects/Particle' + str(count// 6 + 1) + '.png')
                particle.image = pygame.transform.scale(object_image, (particle.width, particle.height))
                #Offset the particle to be roughly mid-body
                particle.x_pos = player.x_pos + 3
                particle.y_pos = player.y_pos+30
                count+=1
                if count == 60: count = 1
                particle.draw(self.game_screen)
            #Display level counter in corner
            #message_to_screen_left(self.game_screen, 'Level ' + str(int((level-1)*2 +1)), WHITE, level_font, 0, 0)
            #Detect collision
            try:
                collision = self.detect_all_collisions(level, player, slime_0, slime_1, slime_2, treasure)
            except:
                try:
                    collision = self.detect_all_collisions(level, player, slime_0, slime_1, 0, treasure)
                except:
                    collision = self.detect_all_collisions(level, player, slime_0, 0, 0, treasure)

            if collision == 'dead':
                did_win = False
                break
            elif collision == 'treasure':
                break

            pygame.display.update()
            clock.tick(self.TICK_RATE)
        #Increment game or return to level one or go to main menu
        if did_win:
            if level >= self.WIN_LEVEL:
                self.win_game()
            else:
                message_to_screen_left(self.game_screen, 'Level ' + str(int((level-1)*2 +1)), WHITE, level_font, 0, 0)

                self.run_game_loop(level + 0.5)
        elif self.game_restart():
            self.run_game_loop(1)
        else:
            return

    def detect_all_collisions (self, level, player, slime_0, slime_1, slime_2, treasure):
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
            message_to_screen_center(self.game_screen, 'Next Up, Level ' + str(int(level*2)), WHITE, large_font,self.width/2 , self.height/2)
            pygame.display.update()
            clock.tick(1)
            return 'treasure'

class GameObject:

    def __init__(self, image_path, x, y, width, height):
        #Load images and scaleup
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))

class PlayerCharacter(GameObject):

    BASE_SPEED = 5

    object_image = pygame.image.load('ZeldaFront.png')
    prev_sprite = pygame.transform.scale(object_image, (50,70))

    def __init__ (self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
        #Load in all the sprites
        object_image = pygame.image.load(image_path)
        self.fr_image = pygame.transform.scale(object_image, (width,height))
        object_image = pygame.image.load('ZeldaFront.png')
        self.ba_image = pygame.transform.scale(object_image, (width,height))
        object_image = pygame.image.load('ZeldaLeft.png')
        self.le_image = pygame.transform.scale(object_image, (width,height))
        object_image = pygame.image.load('ZeldaRight.png')
        self.ri_image = pygame.transform.scale(object_image, (width,height))

    #Special drawing based on sprite movement
    def draw(self, background, dir_x, dir_y):
        if dir_y > 0:
            background.blit(self.fr_image, (self.x_pos, self.y_pos))
            self.prev_sprite = self.fr_image
        elif dir_y < 0:
            background.blit(self.ba_image, (self.x_pos, self.y_pos))
            self.prev_sprite = self.ba_image
        elif dir_x > 0:
            background.blit(self.ri_image, (self.x_pos, self.y_pos))
            self.prev_sprite = self.ri_image
        elif dir_x < 0:
            background.blit(self.le_image, (self.x_pos, self.y_pos))
            self.prev_sprite = self.le_image
        else:
            background.blit(self.prev_sprite, (self.x_pos, self.y_pos))

    #Move character method
    def move(self, dir_x, dir_y, max_width, max_height, boost):
        MOVE_BY = self.BASE_SPEED
        #Moving diagonally should be 1/sqrt(2)
        if dir_x != 0 and dir_y != 0:
            MOVE_BY *= 0.707
        #Calculate how much to move by
        MOVE_BY *= boost
        #Define X and Y  movement
        self.y_pos += MOVE_BY * -dir_y
        self.x_pos += MOVE_BY * dir_x
        #Boundary detection
        if self.y_pos > max_height-self.height:
            self.y_pos = max_height-self.height
        elif self.y_pos < 0:
            self.y_pos = 0
        if self.x_pos > max_width - self.width:
            self.x_pos = max_width - self.width
        elif self.x_pos < 0:
            self.x_pos = 0

    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height - self.height/2:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False
        return True

class NonPlayerCharacter(GameObject):
    BASE_SPEED = 3
    #True  = right, False = Left
    direction = True
    def __init__ (self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def draw(self, background):
        if self.direction:
            background.blit(self.image, (self.x_pos, self.y_pos))
        else:
            background.blit(pygame.transform.flip(self.image, 1, 0), (self.x_pos, self.y_pos))
    #Move character method - moves left to right across the screen
    def move(self, max_width,):
        if self.x_pos <= 10:
            self.BASE_SPEED = abs(self.BASE_SPEED)
        elif self.x_pos >= (max_width - 25):
            self.BASE_SPEED = -abs(self.BASE_SPEED)
        self.x_pos += self.BASE_SPEED
        self.direction = self.BASE_SPEED < 0

#Start the game up
pygame.init()
new_game = Game('background.png',SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.start_game()

#After game is finished quit the program
pygame.quit()
quit()
