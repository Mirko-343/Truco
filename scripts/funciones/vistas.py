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
    
    # Inicializar variables
    numero_turnos = 0 # Contador para los turnos en cada ronda. Puede llegar a un máximo de 6.
    carta_elegida = None
    carta_rival = None
    x_adicional = 0
    limite_vueltas = 0

    

    # Banderas
    envido_cantado = False # Bandera que sirve para habilitar al rival a que cante envido si el jugador no lo hizo antes
    truco_jugado =  False
    turno = 1 # Bandera que sirve para saber de quién es el turno
    rival_jugo = False
    jugador_jugo = False
    carta_rival_elegida = False
    mostrar_carta_rival = False
    carta_1_elegida = False
    carta_2_elegida = False
    carta_3_elegida = False
    mostrar_rival_1 = False
    mostrar_rival_2 = False
    mostrar_rival_3 = False
    

    # ====================================== Carga de imagenes ======================================
        
    x_1 = (scrn.ANCHO_PANTALLA // 2) - 160
    y_1 = 500
    x_2 = scrn.ANCHO_PANTALLA // 2
    y_2 = 500
    x_3 = (scrn.ANCHO_PANTALLA // 2) + 160
    y_3 = 500

    x_r_1 = (scrn.ANCHO_PANTALLA // 2) - 350
    y_r_1 = 100
    

    carta_1, hit_box_carta_1 = cargar_imagen("carta_1", cartas_jugador[0]["Ruta foto"],
                                                (x_1, y_1))
    carta_2, hit_box_carta_2 = cargar_imagen("carta_2", cartas_jugador[1]["Ruta foto"],
                                                (x_2, y_2))
    carta_3, hit_box_carta_3 = cargar_imagen("carta_3", cartas_jugador[2]["Ruta foto"], 
                                                (x_3, y_3))
    
    carta_rival_1, carta_rival_1_rect = cargar_imagen("carta_rival_1", cartas_rival[0]["Ruta foto"], (x_r_1, y_r_1))
    carta_rival_2, carta_rival_2_rect = cargar_imagen("carta_rival_2", cartas_rival[1]["Ruta foto"], (x_r_1, y_r_1))
    carta_rival_3, carta_rival_3_rect = cargar_imagen("carta_rival_3", cartas_rival[2]["Ruta foto"], (x_r_1, y_r_1))

    # ====================================== Carga de botones ======================================
    
    BTN_ENVIDO, BTN_ENVIDO_RECT = crear_boton("Arial", 30, 100, 40, "Envido", clrs.NEGRO, 45, 300)
    BTN_REAL_ENVIDO, BTN_REAL_ENVIDO_RECT = crear_boton("Arial", 30, 165, 40, "Real Envido", clrs.NEGRO, 45, 350)
    BTN_FALTA_ENVIDO, BTN_FALTA_ENVIDO_RECT = crear_boton("Arial", 30, 170, 40, "Real Envido", clrs.NEGRO, 45, 400)
    
    BTN_ACEPTAR_EVDO, BTN_ACEPTAR_EVDO_RECT = crear_boton("Arail", 30, 60, 40, "Si", clrs.NEGRO, 250, 130)
    BTN_RECHAZAR_EVDO, BTN_RECHAZAR_EVDO_RECT = crear_boton("Arail", 30, 60, 40, "No", clrs.NEGRO, 550, 130)


    # ====================================== Bucle de ejecución ======================================
    clock = pygame.time.Clock()

    run = True

    
    
    while run:

        if mano == -1:
            limite_vueltas = 5
        else:
            limite_vueltas = 6

        if numero_turnos == 2 or numero_turnos == 3:
            x_adicional = 200
        elif numero_turnos == 4 or numero_turnos == 6:
            x_adicional = 400
        
        # ====================================== Verificación de eventos ======================================
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BTN_ENVIDO_RECT.collidepoint(event.pos) and rondas == 0 and turno == 1 and numero_turnos == 0:
                    print("Click botón envido")
                    ganador_envido, puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, "envido", 
                                                                                    envido_jugador, envido_rival, mano, puntos_objetivo)
                    envido_cantado = True
                    print(f"Cantaste envido y el ganador fue {ganador_envido}") # Cantar envido
                elif BTN_FALTA_ENVIDO_RECT.collidepoint(event.pos) and rondas == 0 and turno == 1 and numero_turnos == 0:
                    ganador_envido, puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, "falta envido", 
                                                                                    envido_jugador, envido_rival, mano, puntos_objetivo)
                    envido_cantado = True
                    print(f"Cantaste Falta envido y el ganador fue {ganador_envido}") # Cantar falta
                elif BTN_REAL_ENVIDO_RECT.collidepoint(event.pos) and rondas == 0 and turno == 1 and numero_turnos == 0:
                    ganador_envido, puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, "real envido", 
                                                                                    envido_jugador, envido_rival, mano, puntos_objetivo)
                    envido_cantado = True
                    print(f"Cantaste Real envido y el ganador fue {ganador_envido}") # Cantar real
                elif BTN_ACEPTAR_EVDO_RECT.collidepoint(event.pos) and rondas == 0: # Aceptar envido
                    if numero_turnos == 0 or numero_turnos == 1:
                        if envido_rival >= 30:
                            ganador_envido, puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, 
                                                     "falta envido", envido_jugador, envido_rival, mano, puntos_objetivo)
                            print(f"Aceptaste el Falta envido y el ganador fue: {ganador_envido}")
                        else:
                            ganador_envido, puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, 
                                                           "envido", envido_jugador, envido_rival, mano, puntos_objetivo)
                            print(f"Aceptaste el envido y el ganador fue: {ganador_envido}")
                    envido_cantado = True
                elif BTN_RECHAZAR_EVDO_RECT.collidepoint(event.pos) and rondas == 0: # Rechazar envido
                    if numero_turnos == 0 or numero_turnos == 1:
                        ganador_envido = "rival"
                        puntos_rival += 1
                        envido_cantado = True
                        print("Rechazaste el envido.")
                elif hit_box_carta_1.collidepoint(event.pos) and turno == 1 and carta_1_elegida == False:
                    print("Click en carta 1")
                    carta_elegida = cartas_jugador[0]
                    jugador_jugo = True
                    x_1 = 200 + x_adicional
                    y_1 = 220
                    hit_box_carta_1.center = (x_1 , y_1)
                    carta_1_elegida = True
                elif hit_box_carta_2.collidepoint(event.pos) and turno == 1 and carta_2_elegida == False:
                    print("Click en carta 2")
                    carta_elegida = cartas_jugador[1]
                    jugador_jugo = True
                    x_2 = 200 + x_adicional
                    y_2 = 220
                    hit_box_carta_2.center = (x_2 , y_2)
                    carta_2_elegida = True
                elif hit_box_carta_3.collidepoint(event.pos) and turno == 1 and carta_3_elegida == False:
                    print("Click en carta 3")
                    carta_elegida = cartas_jugador[2]
                    jugador_jugo = True
                    x_3 = 200 + x_adicional
                    y_3 = 220
                    hit_box_carta_3.center = (x_3 , y_3)
                    carta_3_elegida = True



        # ====================================== Desarrollo de la lógica ======================================
        
        scrn.VENTANA_PRINCIPAL.fill(clrs.NEGRO)

        # El rival canta envido / falta envido
        if numero_turnos == 0 or numero_turnos == 1:           
            if turno == -1 and envido_cantado == False:
                if envido_rival > 30:
                    scrn.VENTANA_PRINCIPAL.blit(txt.RIVAL_FALTA_ENVIDO, txt.RIVAL_FALTA_ENVIDO_RECT)
                else:
                    scrn.VENTANA_PRINCIPAL.blit(txt.RIVAL_ENVIDO, txt.RIVAL_ENVIDO_RECT)

                pygame.draw.rect(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_ACEPTAR_EVDO_RECT)
                scrn.VENTANA_PRINCIPAL.blit(BTN_ACEPTAR_EVDO, BTN_ACEPTAR_EVDO_RECT)
            
                pygame.draw.rect(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_RECHAZAR_EVDO_RECT)
                scrn.VENTANA_PRINCIPAL.blit(BTN_RECHAZAR_EVDO, BTN_RECHAZAR_EVDO_RECT)
         
        # El rival elige su carta
        
        
        # if numero_turnos < limite_vueltas:
        #     if turno == -1 and envido_cantado and carta_rival_elegida == False:
        #         posicion = random.randint(0, len(cartas_rival))
        #         carta_rival = cartas_rival[posicion]
        #         cartas_rival.pop(posicion)
        #         rival_jugo = True
        #         carta_rival_elegida = True

        if numero_turnos < limite_vueltas:        
            if turno == -1 and envido_cantado and carta_rival_elegida == False : # Si va el primero 
                carta_rival = random.choice(cartas_rival)      
                print("El rival eligió su carta")
                if mostrar_rival_1:
                    while carta_rival == cartas_rival[0]:
                        carta_rival = random.choice(cartas_rival)
                    if mostrar_rival_2:
                        while carta_rival == cartas_rival[1] or carta_rival == cartas_rival[0]:
                            carta_rival = random.choice(cartas_rival)
                    elif mostrar_rival_3:
                        while carta_rival == cartas_rival[2] or carta_rival == cartas_rival[0]:
                            carta_rival = random.choice(cartas_rival)
                if mostrar_rival_2:
                    while carta_rival == cartas_rival[1]:
                        carta_rival = random.choice(cartas_rival)
                    if mostrar_rival_1:
                        while carta_rival == cartas_rival[1] or carta_rival == cartas_rival[0]:
                            carta_rival = random.choice(cartas_rival)
                    elif mostrar_rival_3:
                        while carta_rival == cartas_rival[2] or carta_rival == cartas_rival[1]:
                            carta_rival = random.choice(cartas_rival)
                elif mostrar_rival_3:
                    while carta_rival == cartas_rival[2]:
                        carta_rival = random.choice(cartas_rival)
                    if mostrar_rival_1:
                        while carta_rival == cartas_rival[2] or carta_rival == cartas_rival[0]:
                            carta_rival = random.choice(cartas_rival)
                    elif mostrar_rival_2:
                        while carta_rival == cartas_rival[2] or carta_rival == cartas_rival[1]:
                            carta_rival = random.choice(cartas_rival)
                rival_jugo = True
                carta_rival_elegida = True
            


        # elif turno == -1 and envido_cantado and carta_elegida != None and carta_rival_elegida == False: # Si primero va el jugador
        #     carta_rival = random.choice(cartas_rival)
        #     print("El rival eligió su carta")
        #     rival_jugo = True
        #     carta_rival_elegida = True
            
        # Se define el ganador de la vuelta
        if carta_rival != None and carta_elegida != None:
            ganador_vuelta = definir_vuelta(carta_elegida, carta_rival)
            print(f"El ganador de la vuelta fue {ganador_vuelta}.")

        # ====================================== Actualización de elementos en pantalla ======================================

        # Cargar cartas
        scrn.VENTANA_PRINCIPAL.blit(carta_1, hit_box_carta_1)
        scrn.VENTANA_PRINCIPAL.blit(carta_2, hit_box_carta_2)
        scrn.VENTANA_PRINCIPAL.blit(carta_3, hit_box_carta_3)
        

        if numero_turnos < limite_vueltas:
            if carta_rival_elegida:
                if carta_rival == cartas_rival[0]:
                    print(f"El rival elgió el {cartas_rival[0]["Numero"]} de {cartas_rival[0]["Palo"]}")
                    carta_rival_1_rect.center = ((200 + x_adicional), 150)              
                    mostrar_rival_1 = True 
                    #print("Se descartó la primer carta del rival")
                elif carta_rival == cartas_rival[1]:
                    print(f"El rival elgió el {cartas_rival[1]["Numero"]} de {cartas_rival[1]["Palo"]}")
                    carta_rival_2_rect.center = ((200 + x_adicional), 150)                            
                    mostrar_rival_2 = True
                    #print("Se descartó la segunda carta del rival")
                elif carta_rival == cartas_rival[2]:
                    print(f"El rival elgió el {cartas_rival[2]["Numero"]} de {cartas_rival[2]["Palo"]}")
                    carta_rival_3_rect.center = ((200 + x_adicional), 150)   
                    mostrar_rival_3 = True
                    #print("Se descartó la tercer carta del rival")
                mostrar_carta_rival = True
                

           
        if mostrar_rival_1:
            scrn.VENTANA_PRINCIPAL.blit(carta_rival_1, carta_rival_1_rect)
        if mostrar_rival_2:
            scrn.VENTANA_PRINCIPAL.blit(carta_rival_2, carta_rival_2_rect)
        if mostrar_rival_3:
            scrn.VENTANA_PRINCIPAL.blit(carta_rival_3, carta_rival_3_rect)
                


        # Cargar botones
        pygame.draw.rect(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_ENVIDO_RECT)
        scrn.VENTANA_PRINCIPAL.blit(BTN_ENVIDO, BTN_ENVIDO_RECT)
        pygame.draw.rect(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_REAL_ENVIDO_RECT)
        scrn.VENTANA_PRINCIPAL.blit(BTN_REAL_ENVIDO, BTN_REAL_ENVIDO_RECT)
        pygame.draw.rect(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_FALTA_ENVIDO_RECT)
        scrn.VENTANA_PRINCIPAL.blit(BTN_FALTA_ENVIDO, BTN_FALTA_ENVIDO_RECT)
        
        # Carga textos
        
        PTS_JUGADOR, PTS_JUGADOR_RECT = txt.mostrar_puntos(puntos_jugador, "jugador", 100, 225)
        PTS_RIVAL, PTS_RIVAL_RECT = txt.mostrar_puntos(puntos_rival, "rival", 100, 250)
        scrn.VENTANA_PRINCIPAL.blit(PTS_JUGADOR, PTS_JUGADOR_RECT)
        scrn.VENTANA_PRINCIPAL.blit(PTS_RIVAL, PTS_RIVAL_RECT)

        # if envido_cantado:
        #     if ganador_envido == "jugador":
        #         scrn.VENTANA_PRINCIPAL.blit(txt.GANASTE_ENVIDO, txt.GANASTE_ENVIDO_RECT)
        #         if pygame.time.get_ticks() > tiempo_acutal:
        #             envido_cantado = False
        #     else:
        #          scrn.VENTANA_PRINCIPAL.blit(txt.PERDISTE_ENVIDO, txt.PERDISTE_ENVIDO_RECT)
        #          if pygame.time.get_ticks() > tiempo_acutal:
        #                 envido_cantado = False
                

        pygame.display.update()
        


        if jugador_jugo == True and turno == 1:
            turno *= -1
            numero_turnos += 1 
            print("Turno del rival")
            print(f"Numero de turnos: {numero_turnos}")
        elif rival_jugo == True and turno == -1:
            turno *= -1
            numero_turnos += 1   
            print(f"Turno del jugador")
            print(f"Numero de turnos: {numero_turnos}")
        
        if jugador_jugo and rival_jugo:
            jugador_jugo = False
            carta_elegida = None
            rival_jugo = False
            carta_rival = None
            carta_rival_elegida = False
        

        # if ronda_completada == True:
        #     carta_elegida = None
        #     carta_rival = None
            
                

    pygame.quit()
                
                