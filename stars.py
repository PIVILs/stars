import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import randint

screen_width = 1400
screen_height = 800

class Star(Sprite):
    def __init__(self, screen):
        self.screen = screen
        super(Star, self).__init__()
        self.image = pygame.image.load('images/lone-star-2028578_640_1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Starry Sky")
    stars = Group()
    create_sky(screen, stars)
    random_star(screen, stars)
    print(len(stars))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 85, 255))
        #random_star(screen, stars)  #ХАОТИЧНОЕ ПЕРЕМЕЩЕНИЕ
        stars.draw(screen)

        pygame.display.flip()
        
def create_sky(screen, stars):
    star = Star(screen)
    star_width = star.rect.width
    available_space_x = screen_width - 2 * star_width
    number_stars_x = int(available_space_x / (2 * star_width))
    number_rows = get_number_rows(screen, star.rect.height)
    
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            star = Star(screen)
            star.x = star_width + 2 * star_width * star_number
            star.rect.x = star.x
            star.rect.y = star.rect.height + 2 * star.rect.height * row_number
            stars.add(star)
            
        
def get_number_rows(screen, star_height):
    available_space_y = screen_height - star_height
    number_rows = int(available_space_y / (2 * star_height))
    return number_rows
    
def random_star(screen, stars):
    """ Случайное смещешие звезд."""
    for misaligned_star in stars.sprites():
        misaligned_star.x = misaligned_star.rect.x + randint(-30, 30)
        misaligned_star.rect.x = misaligned_star.x
        misaligned_star.y = misaligned_star.rect.y + randint(-30, 30)
        misaligned_star.rect.y = misaligned_star.y   

run_game()


