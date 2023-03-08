import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()


class Button:
    def __init__(self, text, width, height, pos):
        # core attributes
        self.pressed = False

        # top-rect
        self.top_rect = pygame.Rect((pos), (width, height))
        self.top_color = '#484848'

        # text
        self.text_surface = button_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surface.get_rect(
            center=self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen, self.top_color,
                         self.top_rect, border_radius=20)
        screen.blit(self.text_surface, self.text_rect)
        self.check_clicks()

    def check_clicks(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#2C2C2C'
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    print('clicked')
                    self.pressed = False


# just the screen width and height stored in variables
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720

# setting the title of application window
pygame.display.set_caption('Binary Tree')

# main display surface which contains animatiion frame, buttons, input bar, etc.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((33, 33, 33))

# the animation surface
main_surface = pygame.Surface((900, 600))
main_surface.fill((66, 66, 66))

# heading font
heading_font = pygame.font.Font('fonts\helvetica\Helvetica_CE_Medium.ttf', 35)
title_text_surface = heading_font.render("Binary Search Tree and Operations", True, (255, 255, 255))

# button font
button_font = pygame.font.Font('fonts\helvetica\Helvetica_CE_Medium.ttf', 15)

# creating required buttons

# insert search and delete
insert_button = Button('Insert', 150, 40, (1000, 140))
search_button = Button('Search', 150, 40, (1000, 210))
delete_button = Button('Delete', 150, 40, (1000, 280))

# traversal heading
traversal_font = pygame.font.Font('fonts\helvetica\Helvetica_CE_Medium.ttf', 30)
traversal_heading_surface = traversal_font.render('Traversal', True, '#FFFFFF')
# tfont_rect = traversal_heading_surface.get_rect(centerx = insert_button.top_rect.centerx) .... failed attempt

# traversal buttons
inorder_button = Button('InOrder', 150, 40, (1000, 430))
preorder_button = Button('PreOrder', 150, 40, (1000, 500))
postorder_button = Button('PostOrder', 150, 40, (1000, 570))

# flip
# main_surface.blit((50,50))
screen.blit(main_surface, (50, 55))
screen.blit(title_text_surface, (200, 10))

# drawing buttons
insert_button.draw()
search_button.draw()
delete_button.draw()

# traversal-heading
screen.blit(traversal_heading_surface, (1015, 360))

# traversal buttons
inorder_button.draw()
preorder_button.draw()
postorder_button.draw()

#update using flip

pygame.display.flip()

# main event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN and insert_button.top_rect.collidepoint(pygame.mouse.get_pos()):
            print('clicked insert')
            # insert_button.top_color = '#000000'

    pygame.display.update()
    clock.tick(60)
