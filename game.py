import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Rock Paper Scissor Game")

background_image = pygame.image.load('graphics/blue.png').convert()
font = pygame.font.Font('font/SunnyspellsRegular.otf', 33)
play_message = font.render("Welcome to Rock Paper Scissor Game", True, (255, 235, 193))
play_message2 = font.render("Pick you Weapon to start playing", True, (255, 235, 193))

score_font = pygame.font.Font('font/SunnyspellsRegular.otf', 25)
user_score_message = score_font.render("Your Score 0", True, (255, 235, 193))
comp_score_message = score_font.render("Comp Score 0", True, (255, 235, 193))

button_rock = pygame.image.load('graphics/button_rock.png')
button_paper = pygame.image.load('graphics/button_paper.png')
button_scissor = pygame.image.load('graphics/button_scissor.png')

rock_rect = button_rock.get_rect(topleft=(25, 330))
paper_rect = button_rock.get_rect(topleft=(225, 330))
scissor_rect = button_rock.get_rect(topleft=(425, 330))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rock_rect.collidepoint(event.pos):
                print("rock")
            elif paper_rect.collidepoint(event.pos):
                print('paper')
            elif scissor_rect.collidepoint(event.pos):
                print("scissor")

    screen.blit(background_image, (0, 0))
    screen.blit(user_score_message, (50, 20))
    screen.blit(comp_score_message, (420, 20))

    screen.blit(play_message, (100, 170))
    screen.blit(play_message2, (120, 200))
    screen.blit(button_rock, rock_rect)
    screen.blit(button_paper, paper_rect)
    screen.blit(button_scissor, scissor_rect)

    pygame.display.update()
