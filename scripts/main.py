from turtle import delay
import pygame
import random
from config import colores as clrs
from config import texto as txt
from config import pantalla as scrn
from funciones import bucle_principal
from funciones import auxiliares
from funciones import vistas


pygame.init()

run_game = True


while run_game: # Bucle de ejecución del juego
    
    # CODIGO DEL MENU PRINCIPAL
    pygame.display.set_caption("Menu")
    
    scrn.VENTANA_PRINCIPAL.blit(scrn.BOTON_JUGAR, scrn.BTN_JUGAR_RECT)
    
    scrn.VENTANA_PRINCIPAL.blit(txt.MENU_HEAD, txt.MENU_HEAD_RECT)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if scrn.BTN_JUGAR_RECT.collidepoint(event.pos):
                # Funcion de la vista para elegir rival
                rival = "Aleatorio"
                
                # Funcion de la vista para elegir a cuántos puntos puntos
                puntos_objetivo = 15

                puntos_rival = 0
                puntos_jugador = 0
                ronda = 0
                mano = 1
                while puntos_jugador < puntos_objetivo:
                    vistas.jugar_vs_aleatorio(puntos_objetivo, ronda, puntos_jugador, puntos_rival, mano)
                    ronda += 1
            
                
    pygame.display.update()
    

pygame.quit()