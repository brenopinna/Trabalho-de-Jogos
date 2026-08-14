# Inicialização
import pygame 
import random
pygame.init()
pygame.font.init()



font = font = pygame.font.Font(None, 50)
Nome = "Breno Pinna"
x, y =  random.randint(0, 500), random.randint(0, 400)
rect =  (x, y, 205, 35)
# modifiquei o react para levar em conta certinho as coordenadas aleatorias!!

# random.seed(Nome)
# tambem tirei essa seed fixa pra ver a caixinha mudando de posicao em novas renderizacoes!!

print(y)

# Cria a janela
WIDTH   =  800; HEIGHT =  600
screen = pygame.display.set_mode((WIDTH, HEIGHT))  

#loop
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        # Desenha
        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, (255,255,255), rect)
        screen.blit(font.render(Nome, True, (0,0,0)), (x,y))
        pygame.display.flip()