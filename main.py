import pygame

peso = input("Ingresa tu peso: ")

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Imagen Rotando")


imagen = pygame.image.load("logos.jpg")
imagen = pygame.transform.scale(imagen, (400, 400)) 
rect = imagen.get_rect(center=(300, 200))

angulo = 0
reloj = pygame.time.Clock()

pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play(-1) 

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    angulo += 1
    imagen_rotada = pygame.transform.rotate(imagen, angulo)
    rect_rotado = imagen_rotada.get_rect(center=rect.center)

    screen.fill((255, 255, 255))
    screen.blit(imagen_rotada, rect_rotado.topleft)
    
    pygame.display.flip()
    reloj.tick(60) 