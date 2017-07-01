import sys, pygame

from pygame.locals import *
from personaje import Personaje
from obstaculo import Obstaculo
from random import randint

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy")

fondo = pygame.image.load("img/fondo.png")

speedFondo = [-1,0]
morraco = Personaje(size)
    
obstaculo = [Obstaculo(size,640, randint(1, 5)),
            Obstaculo(size,940, randint(1, 5)), 
            Obstaculo(size,1240, randint(1, 5)), 
            Obstaculo(size,1540, randint(1, 5))]




def main():
    pygame.init()        
    fondoRect = fondo.get_rect()
    
    
    fuente = pygame.font.Font(None,40)    
    

    hilito1 = 0 
    muerto = False
    
    
    puntaje = 0    
    sonido = pygame.mixer.Sound("sonido/cartoon130.wav")

    while muerto == False:
    	
    	for event in pygame.event.get():    		
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    morraco.saltando = True
                    sonido.play()
            if event.type == pygame.QUIT:
                sys.exit()

        hilito1 += 1
        if hilito1 == 20:            
            fondoRect = fondoRect.move(speedFondo)
            hilito1 = 0
            if fondoRect.left < -490:
                fondoRect.left = 0       

        for i in range(0,4):
            if obstaculo[i].rect.left < -110:
                obstaculo[i].cambiar(1560, randint(1, 5))
            for j in range(0,4):
                if i != j:
                    if abs(obstaculo[i].rect.left - obstaculo[j].rect.left) < 80 and obstaculo[i].tipo%2 == 1 and obstaculo[j].tipo%2 == 1:
                        obstaculo[j].rect.left += 250;        
            obstaculo[i].rect.left -= 1;
        

        for i in range(0,4):
            if obstaculo[i].tipo%2 == 0:
                if (morraco.rect.left == obstaculo[i].rect.left + 90):
                    puntaje += 5
            elif morraco.rect.left == obstaculo[i].rect.left + 79:
                puntaje += 10

        
               
        
        carreta = fuente.render("Puntaje: " + str(puntaje),0,(255,230,230))
        morraco.update()        
        screen.blit(fondo, fondoRect) 
        screen.blit(morraco.image, morraco.rect)    	
        screen.blit(carreta,(200,50))
        for i in range(0,4):
            screen.blit(obstaculo[i].image, obstaculo[i].rect)        

        if morraco.rect.top > 480:
            muerto = True
            iniciar(str(puntaje))
        
        for i in range(0,4):
            if obstaculo[i].tipo == 1:
                if morraco.rect.left+38 >= obstaculo[i].rect.left and morraco.rect.left <= obstaculo[i].rect.left+72 and (morraco.rect.top <= 148 or morraco.rect.top+42 >= 310):
                    muerto = True
                    iniciar(str(puntaje))                
            if obstaculo[i].tipo == 3:
                if morraco.rect.left+38 >= obstaculo[i].rect.left and morraco.rect.left <= obstaculo[i].rect.left+72 and (morraco.rect.top <= 206 or morraco.rect.top+42 >= 363):
                    muerto = True
                    iniciar(str(puntaje))
            if obstaculo[i].tipo == 5:
                if morraco.rect.left+38 >= obstaculo[i].rect.left and morraco.rect.left <= obstaculo[i].rect.left+72 and (morraco.rect.top <= 112 or morraco.rect.top+42 >= 270):
                    muerto = True
                    iniciar(str(puntaje))
            if obstaculo[i].tipo%2 == 0:
                if morraco.rect.left+20 >= obstaculo[i].rect.left and morraco.rect.left <= obstaculo[i].rect.left+89 and morraco.rect.top+30 >= obstaculo[i].rect.top and morraco.rect.top <= obstaculo[i].rect.top+40:
                    muerto = True
                    iniciar(str(puntaje))
        



        pygame.display.update()
    

def iniciar(puntaje):    
    pygame.init()
    muerto = True
    mensaje = pygame.image.load("img/master.jpg")
    mensajeRect = mensaje.get_rect()
    
    fuente1 = pygame.font.Font(None,40)
    aux = "Ha muerto, Su puntaje es de " + str(puntaje)
    texto = fuente1.render(aux,0,(255,230,230))
    texto1 = fuente1.render("Presione SPACE para empezar",0,(255,230,230))
    texto2 = fuente1.render("Cristian David Santoyo Parra " + "Cod: 20141020077",0,(255,230,230))
    screen.blit(mensaje, mensajeRect)
    screen.blit(texto,(0,0))
    screen.blit(texto1,(150,150))
    screen.blit(texto2,(0,350))
    
    obstaculo[0].cambiar(640, randint(1, 5))
    obstaculo[1].cambiar(940, randint(1, 5))
    obstaculo[2].cambiar(1240, randint(1, 5))
    obstaculo[3].cambiar(1540, randint(1, 5))

    while muerto == True:        
        
        for event in pygame.event.get():            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.draw.rect(screen, (0, 64, 64, 64), pygame.Rect(640,100,0,380))
        pygame.display.update()


if __name__ == '__main__':
     iniciar("")

