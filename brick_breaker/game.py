import pygame



pygame.init()
width= 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
x = width//2
y = height//2
direction = 1
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("red")

    # RENDER YOUR GAME HERE
    
    if(x + 50 < width):
        x+=direction
    else:
        direction = -1
        x+=direction
    pygame.draw.circle(surface=screen,center=(x,y),radius=50,color="purple")
    '''
    (0,0), right +x,left -x
            up -y, down +y
            
    '''
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()