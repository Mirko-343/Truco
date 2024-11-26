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

    # Banderas
    envido_cantado = False # Bandera que sirve para habilitar al rival a que cante envido si el jugador no lo hizo antes
    truco_jugado =  False
    turno = -1 # Bandera que sirve para saber de quién es el turno

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
    
    BTN_ACEPTAR_EVDO, BTN_ACEPTAR_EVDO_RECT = crear_boton("Arail", 30, 60, 40, "Si", clrs.NEGRO, 250, 130)
    BTN_RECHAZAR_EVDO, BTN_RECHAZAR_EVDO_RECT = crear_boton("Arail", 30, 60, 40, "No", clrs.NEGRO, 550, 130)


    # ====================================== Bucle de ejecución ======================================
    clock = pygame.time.Clock()

    run = True

    numero_turnos = 0 # Contador para los turnos en cada ronda. Puede llegar a un máximo de 6.
    
    while run:
         

        event_list = pygame.event.get()
        
        # ====================================== Verificación de eventos ======================================
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BTN_ENVIDO_RECT.collidepoint(event.pos) and rondas == 0 and turno == 1 and numero_turnos == 0:
                    print("Click botón envido")
                    puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, "envido", ganador_envido, mano, 
                                                                    puntos_objetivo)
                    envido_cantado = True
                    # print(f"Tanto del rival: {envido_rival}")
                    # print(f"Tanto del jugador: {envido_jugador}")
                    # print(f"Puntos del jugador luego del envido {puntos_jugador}")
                elif BTN_REAL_ENVIDO_RECT.collidepoint(event.pos) and rondas == 0 and turno == 1 and numero_turnos == 0:
                    print("Click botón Real Envido")
                    puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, "real envido", ganador_envido, mano, 
                                                                    puntos_objetivo)
                    envido_cantado = True
                elif BTN_FALTA_ENVIDO_RECT.collidepoint(event.pos) and rondas == 0 and turno == 1 and numero_turnos == 0:
                    puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, "falta envido", ganador_envido, mano, 
                                                                    puntos_objetivo)
                    envido_cantado = True
                    print("Click botón Falta Envido")
                elif BTN_ACEPTAR_EVDO_RECT.collidepoint(event.pos) and rondas == 0 and numero_turnos == 0:
                    if envido_rival >= 30:
                        puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, "falta envido", ganador_envido, mano, 
                                                                    puntos_objetivo)
                    else:
                        puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, "envido", ganador_envido, mano, 
                                                                    puntos_objetivo)
                    envido_cantado = True
                elif BTN_RECHAZAR_EVDO_RECT.collidepoint(event.pos) and rondas == 0 and numero_turnos == 0:
                    puntos_rival += 1
                    envido_cantado = True



        # ====================================== Desarrollo de la lógica ======================================
        
        scrn.VENTANA_PRINCIPAL.fill(clrs.NEGRO)

        # El rival canta envido / falta envido
        if rondas == 0 and turno == -1 and envido_cantado == False and numero_turnos == 0:
            if envido_rival > 30:
                scrn.VENTANA_PRINCIPAL.blit(txt.RIVAL_FALTA_ENVIDO, txt.RIVAL_FALTA_ENVIDO_RECT)
            else:
                scrn.VENTANA_PRINCIPAL.blit(txt.RIVAL_ENVIDO, txt.RIVAL_ENVIDO_RECT)

            pygame.draw.rect(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_ACEPTAR_EVDO_RECT)
            scrn.VENTANA_PRINCIPAL.blit(BTN_ACEPTAR_EVDO, BTN_ACEPTAR_EVDO_RECT)
            
            pygame.draw.rect(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_RECHAZAR_EVDO_RECT)
            scrn.VENTANA_PRINCIPAL.blit(BTN_RECHAZAR_EVDO, BTN_RECHAZAR_EVDO_RECT)
            

        # ====================================== Actualización de elementos en pantalla ======================================

        # Cargar cartas
        scrn.VENTANA_PRINCIPAL.blit(carta_1, hit_box_carta_1)
        scrn.VENTANA_PRINCIPAL.blit(carta_2, hit_box_carta_2)
        scrn.VENTANA_PRINCIPAL.blit(carta_3, hit_box_carta_3)
        
        # Cargar botones
        pygame.draw.rect(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_ENVIDO_RECT)
        scrn.VENTANA_PRINCIPAL.blit(BTN_ENVIDO, BTN_ENVIDO_RECT)
        pygame.draw.rect(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_REAL_ENVIDO_RECT)
        scrn.VENTANA_PRINCIPAL.blit(BTN_REAL_ENVIDO, BTN_REAL_ENVIDO_RECT)
        pygame.draw.rect(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_FALTA_ENVIDO_RECT)
        scrn.VENTANA_PRINCIPAL.blit(BTN_FALTA_ENVIDO, BTN_FALTA_ENVIDO_RECT)
        
        # Carga textos


        pygame.display.update()
        

        # CAMBIAR DE VALOR LA VARIABLE TURNO
        
        # PONER CONDICIONES PARA TERMINAR LA RONDA
    
        clock.tick(15)
       
        if truco_jugado and envido_cantado:
            turno *= -1
            numero_turnos += 1

        # print(f"Turno numero: {numero_turnos} completado")

    pygame.quit()
                
                