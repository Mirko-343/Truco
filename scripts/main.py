﻿# Importaciones
import pygame
import random
from config import colores as clrs
from config import texto as txt
from config import pantalla as scrn
from funciones import bucle_principal
from funciones import auxiliares
from funciones import vistas

# Incializar
pygame.init()
pygame.mixer.init()

# ====================================== Carga de imágenes ======================================
fondo = pygame.image.load("./media/imagenes/fondo.jpg")
titulo, titulo_rect = auxiliares.cargar_imagen("titulo.jpg", "./media/imagenes/titulo.png", ((scrn.ANCHO_PANTALLA // 2), 160))
boton_jugar, boton_jugar_rect = auxiliares.cargar_imagen("boton_jugar" , "./media/imagenes/boton_con_texto_grande.png", 
                                                            ((scrn.ANCHO_PANTALLA // 2), 330))

pygame.mixer.music.load("./media/audio/menu.mp3")
pygame.mixer.music.play(loops=-1)


run_game = True


while run_game: # Bucle de ejecución del juego   
    pygame.display.set_caption("Menu")


    # ====================================== Verificación de eventos ======================================

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boton_jugar_rect.collidepoint(event.pos):
                
                # Obetener nombre del jugador
                nombre_jugador = vistas.obtener_nombre()
                
                # Elegir el rival
                rival = vistas.elegir_rival()
                
                # Funcion de la vista para elegir a cuántos puntos puntos
                puntos_objetivo = vistas.elegir_puntos()

                # Reinciar variables para cada partida
                puntos_rival = 0
                puntos_jugador = 0
                puntos_rival
                ronda = 0
                mano = random.choice([-1, 1])

                while puntos_jugador < puntos_objetivo and puntos_rival < puntos_objetivo:
                    if rival == "aleatorio":
                        puntos_jugador, puntos_rival, nombre_jugador = vistas.jugar_vs_aleatorio(puntos_objetivo, ronda, 
                                                                puntos_jugador, puntos_rival, mano, nombre_jugador)
                        ronda += 1
                        mano *= -1
                    elif rival == "estrategico":
                        puntos_jugador, puntos_rival, nombre_jugador = vistas.jugar_vs_estrategico(puntos_objetivo, ronda, 
                                                                puntos_jugador, puntos_rival, mano, nombre_jugador)
                        ronda += 1
                        mano *= -1
                if puntos_jugador >= puntos_objetivo:
                    auxiliares.actualizar_registros(nombre_jugador, True, False)
                elif puntos_rival >= puntos_objetivo:
                    auxiliares.actualizar_registros(nombre_jugador, False, True)
                    

   
    # ====================================== Actualización de elementos en pantalla ======================================

    scrn.VENTANA_PRINCIPAL.fill(clrs.NEGRO)
        
    scrn.VENTANA_PRINCIPAL.blit(fondo)

    scrn.VENTANA_PRINCIPAL.blit(titulo, titulo_rect)

    scrn.VENTANA_PRINCIPAL.blit(boton_jugar, boton_jugar_rect)

                
    pygame.display.update()