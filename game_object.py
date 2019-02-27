import pygame


class GameObject:

    def __init__(self, image_path, x, y, width, height):
        # Load images and scaleup
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))


class NPC(GameObject):
    BASE_SPEED = 3
    # True  = right, False = Left
    direction = True

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def draw(self, background):
        if self.direction:
            background.blit(self.image, (self.x_pos, self.y_pos))
        else:
            background.blit(pygame.transform.flip(
                self.image, 1, 0), (self.x_pos, self.y_pos))
    # Move character method - moves left to right across the screen

    def move(self, max_width,):
        if self.x_pos <= 10:
            self.BASE_SPEED = abs(self.BASE_SPEED)
        elif self.x_pos >= (max_width - 25):
            self.BASE_SPEED = -abs(self.BASE_SPEED)
        self.x_pos += self.BASE_SPEED
        self.direction = self.BASE_SPEED < 0


class PC(GameObject):

    BASE_SPEED = 5

    object_image = pygame.image.load('PC/ZeldaFront.png')
    prev_sprite = pygame.transform.scale(object_image, (50, 70))

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)
        # Load in all the sprites
        object_image = pygame.image.load(image_path)
        self.fr_image = pygame.transform.scale(object_image, (width, height))
        object_image = pygame.image.load('PC/ZeldaFront.png')
        self.ba_image = pygame.transform.scale(object_image, (width, height))
        object_image = pygame.image.load('PC/ZeldaLeft.png')
        self.le_image = pygame.transform.scale(object_image, (width, height))
        object_image = pygame.image.load('PC/ZeldaRight.png')
        self.ri_image = pygame.transform.scale(object_image, (width, height))

    # Special drawing based on sprite movement
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

    # Move character method
    def move(self, dir_x, dir_y, max_width, max_height, boost):
        MOVE_BY = self.BASE_SPEED
        # Moving diagonally should be 1/sqrt(2)
        if dir_x != 0 and dir_y != 0:
            MOVE_BY *= 0.707
        # Calculate how much to move by
        MOVE_BY *= boost
        # Define X and Y  movement
        self.y_pos += MOVE_BY * -dir_y
        self.x_pos += MOVE_BY * dir_x
        # Boundary detection
        if self.y_pos > max_height - self.height:
            self.y_pos = max_height - self.height
        elif self.y_pos < 0:
            self.y_pos = 0
        if self.x_pos > max_width - self.width:
            self.x_pos = max_width - self.width
        elif self.x_pos < 0:
            self.x_pos = 0

    def detect_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height - self.height / 2:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False
        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False
        return True
