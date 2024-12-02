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
pygame.mixer.init()

run_game = True


while run_game: # Bucle de ejecución del juego
    
    # CODIGO DEL MENU PRINCIPAL
    pygame.display.set_caption("Menu")
    
    BTN_JUGAR, BTN_JUGAR_RECT = auxiliares.crear_boton("Arial", 30, 80, 40, "Jugar", clrs.NEGRO, (scrn.ANCHO_PANTALLA // 2), (scrn.ALTO_PANTALLA // 2))
        
    fondo = pygame.image.load("./media/imagenes/portada.jpg")
    titulo, titulo_rect = auxiliares.cargar_imagen("titulo.jpg", "./media/imagenes/titulo.png", ((scrn.ANCHO_PANTALLA // 2), 160))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if BTN_JUGAR_RECT.collidepoint(event.pos):
                    
                nombre_jugador = vistas.obtener_nombre()
                print(nombre_jugador)
                # Funcion de la vista para elegir rival
                rival = vistas.elegir_rival()
                
                # Funcion de la vista para elegir a cuántos puntos puntos
                puntos_objetivo = 8

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
                if puntos_jugador >= puntos_objetivo:
                    auxiliares.actualizar_registros(nombre_jugador, True, False)
                elif puntos_rival >= puntos_objetivo:
                    auxiliares.actualizar_registros(nombre_jugador, False, True)
        
    scrn.VENTANA_PRINCIPAL.fill(clrs.NEGRO)
        
    scrn.VENTANA_PRINCIPAL.blit(fondo)

    scrn.VENTANA_PRINCIPAL.blit(titulo, titulo_rect)

    auxiliares.mostrar_boton(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_JUGAR, BTN_JUGAR_RECT)
    # scrn.VENTANA_PRINCIPAL.blit(scrn.BOTON_JUGAR, scrn.BTN_JUGAR_RECT)
   
                
    pygame.display.update()