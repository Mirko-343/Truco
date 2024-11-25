# Imports
import pygame

from config import colores as clrs
from config import texto as txt
from config import pantalla as scrn
from .auxiliares import *
from .bucle_principal import *


def jugar_vs_aleatorio(puntos_objetivo : int, rondas : int, puntos_jugador : int, puntos_rival : int, mano : int):
    
    # Asignación de cartas
    info_cartas = "./media/info_cartas.csv"
    ruta_imagenes = "./media/imagenes/cartas"
    lista_cartas = generar_listado_cartas(info_cartas,ruta_imagenes)

    cartas_jugador, cartas_rival = asignar_cartas(lista_cartas) # Reparte las cartas
    while definir_envido(cartas_rival) < 20: # Se asegura que el rival siempre tenga tanto
        cartas_jugador, cartas_rival = asignar_cartas(lista_cartas) # Si no tiene reparte de nuevo
        
    # Verificar quién gano el posible envido
    envido_jugador = definir_envido(cartas_jugador)    
    envido_rival = definir_envido(cartas_rival)
    
    if envido_jugador > envido_rival:
        ganador_envido = "jugador"
    elif envido_jugador < envido_rival:
        ganador_envido = "rival"
    else:
        ganador_envido = "empate"

    # ====================================== Carga de imagenes ======================================
        
    x_1 = (scrn.ANCHO_PANTALLA // 2) - 160
    y_1 = 500
    x_2 = scrn.ANCHO_PANTALLA // 2
    y_2 = 500
    x_3 = (scrn.ANCHO_PANTALLA // 2) + 160
    y_3 = 500

    carta_1, hit_box_carta_1 = cargar_imagen("carta_1", cartas_jugador[0]["Ruta foto"],
                                                (x_1, y_1))
    carta_2, hit_box_carta_2 = cargar_imagen("carta_2", cartas_jugador[1]["Ruta foto"],
                                                (x_2, y_2))
    carta_3, hit_box_carta_3 = cargar_imagen("carta_3", cartas_jugador[2]["Ruta foto"], 
                                                (x_3, y_3))

    # ====================================== Carga de botones ======================================
    
    BTN_ENVIDO, BTN_ENVIDO_RECT = crear_boton("Arial", 30, 100, 40, "Envido", clrs.NEGRO, 45, 300)
    BTN_REAL_ENVIDO, BTN_REAL_ENVIDO_RECT = crear_boton("Arial", 30, 165, 40, "Real Envido", clrs.NEGRO, 45, 350)
    BTN_FALTA_ENVIDO, BTN_FALTA_ENVIDO_RECT = crear_boton("Arial", 30, 170, 40, "Real Envido", clrs.NEGRO, 45, 400)


    # ====================================== Bucle de ejecución ======================================
    run = True

    while run:
        
        turno = 1

        event_list = pygame.event.get()
        
        # ====================================== Verificación de eventos ======================================
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BTN_ENVIDO_RECT.collidepoint(event.pos) and rondas == 0 and turno == 1:
                    print("Click botón envido")
                    puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, "envido", ganador_envido, mano, 
                                                                    puntos_objetivo)
                    # print(f"Tanto del rival: {envido_rival}")
                    # print(f"Tanto del jugador: {envido_jugador}")
                    # print(f"Puntos del jugador luego del envido {puntos_jugador}")
                elif BTN_REAL_ENVIDO_RECT.collidepoint(event.pos) and rondas == 0 and turno == 1:
                    print("Click botón Real Envido")
                    puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, "real envido", ganador_envido, mano, 
                                                                    puntos_objetivo)
                elif BTN_FALTA_ENVIDO_RECT.collidepoint(event.pos) and rondas == 0 and turno == 1:
                    puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, "falta envido", ganador_envido, mano, 
                                                                    puntos_objetivo)
                    print("Click botón Falta Envido")

        # ====================================== Desarrollo de la lógica ======================================
        

        
        # ====================================== Actualización de elementos en pantalla ======================================
        scrn.VENTANA_PRINCIPAL.fill(clrs.NEGRO)
        
        scrn.VENTANA_PRINCIPAL.blit(carta_1, hit_box_carta_1)
        scrn.VENTANA_PRINCIPAL.blit(carta_2, hit_box_carta_2)
        scrn.VENTANA_PRINCIPAL.blit(carta_3, hit_box_carta_3)
        
        pygame.draw.rect(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_ENVIDO_RECT)
        scrn.VENTANA_PRINCIPAL.blit(BTN_ENVIDO, BTN_ENVIDO_RECT)
        pygame.draw.rect(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_REAL_ENVIDO_RECT)
        scrn.VENTANA_PRINCIPAL.blit(BTN_REAL_ENVIDO, BTN_REAL_ENVIDO_RECT)
        pygame.draw.rect(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_FALTA_ENVIDO_RECT)
        scrn.VENTANA_PRINCIPAL.blit(BTN_FALTA_ENVIDO, BTN_FALTA_ENVIDO_RECT)
        
        pygame.display.update()
        
                
    pygame.quit()
                
                