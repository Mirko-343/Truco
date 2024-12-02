# Imports
import pygame
import pygame_gui
import csv

from config import colores as clrs
from config import texto as txt
from config import pantalla as scrn
from .auxiliares import *
from .bucle_principal import *

def jugar_vs_aleatorio(puntos_objetivo : int, rondas : int, puntos_jugador : int, puntos_rival : int, mano : int, 
                       nombre_jugador : str):
    
    # Asiganación de cartas
    info_cartas = "./media/registros/info_cartas.csv"
    ruta_imagenes = "./media/imagenes/cartas"
    lista_cartas = generar_listado_cartas(info_cartas,ruta_imagenes)

    cartas_jugador, cartas_rival = asignar_cartas(lista_cartas) # Reparte las cartas
    while definir_envido(cartas_rival) < 20: # Se asegura que el rival siempre tenga tanto
        cartas_jugador, cartas_rival = asignar_cartas(lista_cartas) # Si no tiene reparte de nuevo
        
    # Definir los tantos
    envido_jugador = definir_envido(cartas_jugador)    
    envido_rival = definir_envido(cartas_rival)
    
    # Inicializar variables
    numero_tiradas = 0 # Contador para los turnos en cada ronda. Puede llegar a un máximo de 6.
    carta_jugador = None
    carta_rival = None
    x_adicional = 0
    limite_vueltas = 0
    cartas_elegidas_rival = []
    vueltas_ganadas_jugador = 0
    vueltas_ganadas_rival = 0
    empates = 0
    tipo_truco = None

    # Banderas
    envido_cantado = False # Bandera que sirve para habilitar al rival a que cante envido si el jugador no lo hizo antes
    truco_cantado =  False # Bander que sirve para finalizar cada rona
    turno = mano # Bandera que sirve para saber de quién es el turno
    rival_jugo = False # Bandera para saber si el rival jugó
    jugador_jugo = False # Bandera para saber si el jugador jugó
    carta_rival_elegida = False # Bandera que sirve para saber si el rival ya eligió su carta
    # Banderas para manejar las imagenes de las cartas
    carta_1_elegida = False
    carta_2_elegida = False
    carta_3_elegida = False
    mostrar_rival_1 = False
    mostrar_rival_2 = False
    mostrar_rival_3 = False
    

    # ====================================== Carga de imagenes ======================================
       
    carta_1, hit_box_carta_1 = cargar_imagen("carta_1", cartas_jugador[0]["Ruta foto"],
                                                ((scrn.ANCHO_PANTALLA // 2) - 160, 500))
    carta_2, hit_box_carta_2 = cargar_imagen("carta_2", cartas_jugador[1]["Ruta foto"],
                                                (scrn.ANCHO_PANTALLA // 2, 500))
    carta_3, hit_box_carta_3 = cargar_imagen("carta_3", cartas_jugador[2]["Ruta foto"], 
                                                ((scrn.ANCHO_PANTALLA // 2) + 160, 500))
    
    carta_rival_1, carta_rival_1_rect = cargar_imagen("carta_rival_1", cartas_rival[0]["Ruta foto"], (0, 0))
    carta_rival_2, carta_rival_2_rect = cargar_imagen("carta_rival_2", cartas_rival[1]["Ruta foto"], (0, 0))
    carta_rival_3, carta_rival_3_rect = cargar_imagen("carta_rival_3", cartas_rival[2]["Ruta foto"], (0, 0))

    # ====================================== Carga de botones ======================================
    
    BTN_ENVIDO, BTN_ENVIDO_RECT = crear_boton("Arial", 30, 100, 40, "Envido", clrs.NEGRO, 45, 300)
    BTN_REAL_ENVIDO, BTN_REAL_ENVIDO_RECT = crear_boton("Arial", 30, 165, 40, "Real Envido", clrs.NEGRO, 45, 350)
    BTN_FALTA_ENVIDO, BTN_FALTA_ENVIDO_RECT = crear_boton("Arial", 30, 170, 40, "Falta Envido", clrs.NEGRO, 45, 400)
    
    BTN_ACEPTAR_EVDO, BTN_ACEPTAR_EVDO_RECT = crear_boton("Arail", 30, 60, 40, "Si", clrs.NEGRO, 300, 130)
    BTN_RECHAZAR_EVDO, BTN_RECHAZAR_EVDO_RECT = crear_boton("Arail", 30, 60, 40, "No", clrs.NEGRO, 500, 130)

    BTN_TRUCO, BTN_TRUCO_RECT = crear_boton("Arial", 30, 100, 40, "Truco", clrs.NEGRO, 815 , 300)
    BTN_RE_TRUCO, BTN_RE_TRUCO_RECT = crear_boton("Arial", 30, 165, 40, "Retruco", clrs.NEGRO, 755 , 350)
    BTN_VALE_CUATRO, BTN_VALE_CUATRO_RECT = crear_boton("Arial", 30, 165, 40, "Vale cuatro", clrs.NEGRO, 755 , 400)


    # ====================================== Bucle de ejecución ======================================
    clock = pygame.time.Clock()

    run = True
   
    print(f"Turno: {numero_tiradas}")

    while run:
        

        if mano == -1:
            limite_vueltas = 5
        else:
            limite_vueltas = 6

        if numero_tiradas == 2 or numero_tiradas == 3:
            x_adicional = 200
        elif numero_tiradas == 4 or numero_tiradas == 6:
            x_adicional = 400
        
                
        # ====================================== Verificación de eventos ======================================
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BTN_ENVIDO_RECT.collidepoint(event.pos) and turno == 1 and numero_tiradas == 0: # Cantar envido
                    print("Click botón envido")
                    ganador_envido, puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, "envido", 
                                                                                    envido_jugador, envido_rival, mano, puntos_objetivo)
                    gano_alguien = verificar_vicotria(puntos_jugador, puntos_rival, puntos_objetivo, nombre_jugador)
                    if gano_alguien:
                        return puntos_jugador, puntos_rival, nombre_jugador
                    envido_cantado = True
                    print(f"Cantaste envido y el ganador fue {ganador_envido}")
                elif BTN_FALTA_ENVIDO_RECT.collidepoint(event.pos) and turno == 1 and numero_tiradas == 0: # Cantar falta envido
                    ganador_envido, puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, "falta envido", 
                                                                                    envido_jugador, envido_rival, mano, puntos_objetivo)
                    envido_cantado = True
                    gano_alguien = verificar_vicotria(puntos_jugador, puntos_rival, puntos_objetivo, nombre_jugador)
                    if gano_alguien:
                        return puntos_jugador, puntos_rival, nombre_jugador
                    print(f"Cantaste Falta envido y el ganador fue {ganador_envido}")
                elif BTN_REAL_ENVIDO_RECT.collidepoint(event.pos) and turno == 1 and numero_tiradas == 0: # Cantar real envido
                    ganador_envido, puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, "real envido", 
                                                                                    envido_jugador, envido_rival, mano, puntos_objetivo)
                    envido_cantado = True
                    gano_alguien = verificar_vicotria(puntos_jugador, puntos_rival, puntos_objetivo, nombre_jugador)
                    if gano_alguien:
                        return puntos_jugador, puntos_rival, nombre_jugador
                    print(f"Cantaste Real envido y el ganador fue {ganador_envido}") # Cantar real
                elif BTN_ACEPTAR_EVDO_RECT.collidepoint(event.pos): # Aceptar envido
                    if numero_tiradas == 0 or numero_tiradas == 1:
                        if envido_rival >= 30:
                            ganador_envido, puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, 
                                                     "falta envido", envido_jugador, envido_rival, mano, puntos_objetivo)
                            print(f"Aceptaste el Falta envido y el ganador fue: {ganador_envido}")
                        else:
                            ganador_envido, puntos_jugador, puntos_rival = verificar_envido(puntos_jugador, puntos_rival, 
                                                           "envido", envido_jugador, envido_rival, mano, puntos_objetivo)
                            print(f"Aceptaste el envido y el ganador fue: {ganador_envido}")
                        gano_alguien = verificar_vicotria(puntos_jugador, puntos_rival, puntos_objetivo, nombre_jugador)
                        if gano_alguien:
                            return puntos_jugador, puntos_rival, nombre_jugador
                    envido_cantado = True
                elif BTN_RECHAZAR_EVDO_RECT.collidepoint(event.pos): # Rechazar envido
                    if numero_tiradas == 0 or numero_tiradas == 1:
                        ganador_envido = "rival"
                        puntos_rival += 1
                        envido_cantado = True
                        gano_alguien = verificar_vicotria(puntos_jugador, puntos_rival, puntos_objetivo, nombre_jugador)
                        if gano_alguien:
                            return puntos_jugador, puntos_rival, nombre_jugador
                        print("Rechazaste el envido.")
                elif hit_box_carta_1.collidepoint(event.pos) and turno == 1 and carta_1_elegida == False: # Elegir carta 1
                    print("Click en carta 1")
                    carta_jugador = cartas_jugador[0]
                    jugador_jugo = True                   
                    hit_box_carta_1.center = (240 + x_adicional , 220)
                    carta_1_elegida = True
                elif hit_box_carta_2.collidepoint(event.pos) and turno == 1 and carta_2_elegida == False: # Elegir carta 2
                    print("Click en carta 2")
                    carta_jugador = cartas_jugador[1]
                    jugador_jugo = True
                    hit_box_carta_2.center = (240 + x_adicional , 220)
                    carta_2_elegida = True
                elif hit_box_carta_3.collidepoint(event.pos) and turno == 1 and carta_3_elegida == False: # Elegir carta 3
                    print("Click en carta 3")
                    carta_jugador = cartas_jugador[2]
                    jugador_jugo = True
                    hit_box_carta_3.center = (240 + x_adicional , 220)
                    carta_3_elegida = True
                elif BTN_TRUCO_RECT.collidepoint(event.pos) and turno == 1 and truco_cantado == False:
                    print("Cantaste truco")
                    tipo_truco = "truco"
                    truco_cantado = True  # Cantar truco
                elif BTN_RE_TRUCO_RECT.collidepoint(event.pos) and turno == 1 and truco_cantado == False: # Cantar retruco
                    print("Cantaste retruco")
                    tipo_truco = "retruco"
                    truco_cantado = True
                elif BTN_VALE_CUATRO_RECT.collidepoint(event.pos) and turno == 1 and truco_cantado == False: # Cantar vale cuatro
                    print("Cantaste Vale Cuatro")
                    tipo_truco = "vale cuatro"
                    truco_cantado = True



        # ====================================== Desarrollo de la lógica ======================================
        
        scrn.VENTANA_PRINCIPAL.fill(clrs.NEGRO)

        # El rival canta envido / falta envido
        if numero_tiradas == 0 or numero_tiradas == 1:           
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
        if numero_tiradas < limite_vueltas:        
            if turno == -1 and envido_cantado and carta_rival_elegida == False:
                carta_rival = random.choice(cartas_rival)      
                print("El rival eligió su carta")               
                while carta_rival in cartas_elegidas_rival:
                    carta_rival = random.choice(cartas_rival)                    
                cartas_elegidas_rival.append(carta_rival)
                rival_jugo = True
                carta_rival_elegida = True
                

        # Lógica para mostrar las cartas del rival
            
        if numero_tiradas < limite_vueltas:
            if carta_rival_elegida:
                if carta_rival == cartas_rival[0]:
                    carta_rival_1_rect.center = ((240 + x_adicional), 150)              
                    mostrar_rival_1 = True 
                elif carta_rival == cartas_rival[1]:
                    carta_rival_2_rect.center = ((240 + x_adicional), 150)                            
                    mostrar_rival_2 = True
                elif carta_rival == cartas_rival[2]:
                    carta_rival_3_rect.center = ((240 + x_adicional), 150)   
                    mostrar_rival_3 = True

        # ====================================== Actualización de elementos en pantalla ======================================

        # Mostrar cartas del jugador
        scrn.VENTANA_PRINCIPAL.blit(carta_1, hit_box_carta_1)
        scrn.VENTANA_PRINCIPAL.blit(carta_2, hit_box_carta_2)
        scrn.VENTANA_PRINCIPAL.blit(carta_3, hit_box_carta_3)                         
           
        # Mostrar cartas del rival
        if mostrar_rival_1:
            scrn.VENTANA_PRINCIPAL.blit(carta_rival_1, carta_rival_1_rect)
        if mostrar_rival_2:
            scrn.VENTANA_PRINCIPAL.blit(carta_rival_2, carta_rival_2_rect)
        if mostrar_rival_3:
            scrn.VENTANA_PRINCIPAL.blit(carta_rival_3, carta_rival_3_rect)
                
        # Mostrar botones envido
        
        mostrar_boton(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_ENVIDO, BTN_ENVIDO_RECT)
        mostrar_boton(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_REAL_ENVIDO, BTN_REAL_ENVIDO_RECT)
        mostrar_boton(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_FALTA_ENVIDO, BTN_FALTA_ENVIDO_RECT)
        
        # Mostrar botones truco
        mostrar_boton(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_TRUCO, BTN_TRUCO_RECT)
        mostrar_boton(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_RE_TRUCO, BTN_RE_TRUCO_RECT)
        mostrar_boton(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_VALE_CUATRO, BTN_VALE_CUATRO_RECT)      
        
        # Mostrar textos       
        PTS_JUGADOR, PTS_JUGADOR_RECT = txt.mostrar_puntos(puntos_jugador, "jugador", 800, 225)
        PTS_RIVAL, PTS_RIVAL_RECT = txt.mostrar_puntos(puntos_rival, "rival", 800, 250)
        scrn.VENTANA_PRINCIPAL.blit(PTS_JUGADOR, PTS_JUGADOR_RECT)
        scrn.VENTANA_PRINCIPAL.blit(PTS_RIVAL, PTS_RIVAL_RECT)

        if numero_tiradas == 0 or numero_tiradas == 1:
            if envido_cantado:
                if ganador_envido == "jugador":
                    scrn.VENTANA_PRINCIPAL.blit(txt.GANASTE_ENVIDO, txt.GANASTE_ENVIDO_RECT)
                elif ganador_envido == "rival":
                    scrn.VENTANA_PRINCIPAL.blit(txt.PERDISTE_ENVIDO, txt.PERDISTE_ENVIDO_RECT)
        
        pygame.display.update()      

        # Lógica para cambios de turno
        if jugador_jugo == True and turno == 1:
            turno *= -1
            numero_tiradas += 1 
            print("Turno del rival")
            pygame.time.delay(1000)
        elif rival_jugo == True and turno == -1:
            turno *= -1
            numero_tiradas += 1   
            print(f"Turno del jugador")
        
        if jugador_jugo and rival_jugo: # Se completa una tirada

            # Verifica quién ganó la tirada y, si corresponde, quién ganó la mano
            ganador_mano, vueltas_ganadas_jugador, vueltas_ganadas_rival = definir_mano(carta_jugador, carta_rival,
                                                     vueltas_ganadas_jugador, vueltas_ganadas_rival, empates, mano)
            
            # Asigna los puntos dependiendo de quién haya ganado la mano
            puntos_jugador, puntos_rival = verificar_mano(ganador_mano, tipo_truco, puntos_jugador, puntos_rival)
            

            if ganador_mano == 1: # Si el jugador ganó la mano
                if puntos_jugador >= puntos_objetivo:
                    finalizar_mano(puntos_jugador, puntos_rival, True, False, ganador_mano)
                    print("ganaste la partida")
                else:
                    pygame.time.delay(1000)
                    finalizar_mano(puntos_jugador, puntos_rival, False, False, ganador_mano)
                return puntos_jugador, puntos_rival, nombre_jugador
            elif ganador_mano == -1: # Si el rival ganó la mano
                if puntos_rival >= puntos_objetivo:
                    pygame.time.delay(1000)
                    finalizar_mano(puntos_jugador, puntos_rival, False, True, ganador_mano)
                    
                    print("perdiste la partida")
                else:
                    finalizar_mano(puntos_jugador, puntos_rival, False, False, ganador_mano)
                return puntos_jugador, puntos_rival, nombre_jugador
            
            jugador_jugo = False
            carta_jugador = None
            
            rival_jugo = False
            carta_rival = None
            carta_rival_elegida = False
        
            print(f"Turno {numero_tiradas} ---------------")

    pygame.quit()
 
def elegir_rival() -> str:
    
    pygame.init()

    run_game = True


    while run_game: # Bucle de ejecución del juego
      
        BTN_ALEATORIO, BTN_ALEATORIO_RECT = crear_boton("Arial", 30, 195, 40, "Rival aleatorio", clrs.NEGRO, 
                                                        (scrn.ANCHO_PANTALLA // 2 - 250), (scrn.ALTO_PANTALLA // 2) )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BTN_ALEATORIO_RECT.collidepoint(event.pos):
                    return "aleatorio"
                
        scrn.VENTANA_PRINCIPAL.fill(clrs.NEGRO)
        
        mostrar_boton(scrn.VENTANA_PRINCIPAL, clrs.BLANCO, BTN_ALEATORIO, BTN_ALEATORIO_RECT)
                
        pygame.display.update()
    

    pygame.quit()

def finalizar_mano(puntos_jugador : int, puntos_rival : int, vicotria_jugador : bool, victoria_rival : bool, ganador_mano = None) -> tuple:
    pygame.init()

    run_game = True

    while run_game: # Bucle de ejecución del juego
         

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
        
        
        scrn.VENTANA_PRINCIPAL.fill(clrs.NEGRO)
        
        if vicotria_jugador:
            scrn.VENTANA_PRINCIPAL.blit(txt.GANASTE_PARTIDA, txt.GANASTE_PARTIDA_RECT)
        elif victoria_rival:
            scrn.VENTANA_PRINCIPAL.blit(txt.PERDISTE_PARTIDA, txt.PERDISTE_PARTIDA_RECT)
        elif ganador_mano == 1:
            print("Ganaste la mano. Repartiendo de nuevo")
            scrn.VENTANA_PRINCIPAL.blit(txt.GANASTE, txt.GANASTE_RECT)
        elif ganador_mano == -1:
            print("Perdiste la mano. Repartiendo de nuevo")
            scrn.VENTANA_PRINCIPAL.blit(txt.PERDISTE, txt.PERDISTE_RECT)
              
        pygame.display.update()
        
        pygame.time.delay(3000)
        
        return(puntos_jugador, puntos_rival)

    pygame.quit()
    
def obtener_nombre():
    pygame.init()

    x = 200
    y = 275

    run_game = True

    CLOCK = pygame.time.Clock()
    MANAGER = pygame_gui.UIManager((scrn.ANCHO_PANTALLA, scrn.ALTO_PANTALLA))

    TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((x , y), (500, 50)), manager=MANAGER, 
                                                     object_id="#main_text_entry")

    while run_game: # Bucle de ejecución del juego
        UI_REFRESH_RATE = CLOCK.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
                nombre_jugador = event.text
                return nombre_jugador
            
            MANAGER.process_events(event)
           
        MANAGER.update(UI_REFRESH_RATE)
         
        scrn.VENTANA_PRINCIPAL.fill(clrs.BLANCO)
        
        MANAGER.draw_ui(scrn.VENTANA_PRINCIPAL)    

        scrn.VENTANA_PRINCIPAL.blit(txt.INGRESE_NOMBRE, txt.INGRESE_NOMBRE_RECT)
                
        pygame.display.update()
    

    pygame.quit()
    

    

