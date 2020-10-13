import pygame, math
from sprite import Sprite
from sprite_controlled import SpriteControlled

def main():

    #Load
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    font = pygame.font.Font(None,24)   

    background = pygame.image.load('background.png').convert()
    ground = pygame.image.load('ground.png').convert()
    ground_height = 600 - ground.get_height()
    
    player = SpriteControlled(100, ground_height, 'sprite.png', True, 2)
    copain = Sprite(500, ground_height, 'copain.png', True)

    mouse_click = (0, 0)

    collision_text = font.render("Oops, sorry!", False, (0,0,0))
    
    cursor = Sprite(0,0, 'cursor.png', False)
    pygame.mouse.set_visible(False)

    quit_game = False

    while not quit_game:
        #Inputs/
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_click = pygame.mouse.get_pos()
                player.move_to(mouse_click[0])

        
        #Update
        cursor.set_position(pygame.mouse.get_pos())
        player.update()

        #Draw
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
        screen.blit(ground,(0, 500))   

        copain.draw(screen)
        player.draw(screen)
        if(player.intersects(copain)):
            screen.blit(collision_text, (player.x, player.y - 100))
        cursor.draw(screen)
        
        pygame.display.update()
    
if __name__=="__main__":
    main()

