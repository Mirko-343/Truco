import pygame
from .pantalla import *
from .colores import *

pygame.init()

fuente = pygame.font.SysFont("Arial", 40)

# Menu ----------
MENU_HEAD = fuente.render("TRUCO", True, BLANCO)
MENU_HEAD_RECT = MENU_HEAD.get_rect(center = ((ANCHO_PANTALLA // 2), 90))

# Juego ----------
RIVAL_ENVIDO = fuente.render("El rival te canta Envido! ¿Aceptas?", True, BLANCO)
RIVAL_ENVIDO_RECT = RIVAL_ENVIDO.get_rect(center = ((ANCHO_PANTALLA // 2), 70))

RIVAL_FALTA_ENVIDO = fuente.render("El rival te canta Falta Envido! ¿Aceptas?", True, BLANCO)
RIVAL_FALTA_ENVIDO_RECT = RIVAL_ENVIDO.get_rect(center = ((ANCHO_PANTALLA // 2), 70))

GANASTE_ENVIDO = fuente.render("Ganaste el envido!", True, BLANCO)
GANASTE_ENVIDO_RECT = GANASTE_ENVIDO.get_rect(center = ((ANCHO_PANTALLA // 2), 180))

PERDISTE_ENVIDO = fuente.render("Perdiste el envido!", True, BLANCO)
PERDISTE_ENVIDO_RECT = PERDISTE_ENVIDO.get_rect(center = ((ANCHO_PANTALLA // 2), 180))

MOSTRAR_TANTO_RIVAL = fuente.render("Tanto del rival", True, BLANCO)
MOSTRAR_TANTO_RIVAL_RECT = MOSTRAR_TANTO_RIVAL.get_rect(center = ((ANCHO_PANTALLA // 2), 200))

PERDISTE = fuente.render("Perdiste la mano. Repartiendo cartas...", True, BLANCO)
PERDISTE_RECT = PERDISTE.get_rect(center = ((ANCHO_PANTALLA // 2), (ALTO_PANTALLA // 2)))

GANASTE = fuente.render("Ganaste la mano. Repartiendo cartas...", True, BLANCO)
GANASTE_RECT = GANASTE.get_rect(center = ((ANCHO_PANTALLA // 2), (ALTO_PANTALLA // 2)))

GANASTE_PARTIDA = fuente.render("GANASTE LA PARTIDA! Volviendo al menú principal", True, BLANCO)
GANASTE_PARTIDA_RECT = GANASTE_PARTIDA.get_rect(center = ((ANCHO_PANTALLA // 2), (ALTO_PANTALLA // 2)))

PERDISTE_PARTIDA = fuente.render("PERDISTE LA PARTIDA :( Volviendo al menú principal", True, BLANCO)
PERDISTE_PARTIDA_RECT = PERDISTE_PARTIDA.get_rect(center = ((ANCHO_PANTALLA // 2), (ALTO_PANTALLA // 2)))

INGRESE_NOMBRE = fuente.render("Ingrese su nombre: ", True, NEGRO)
INGRESE_NOMBRE_RECT =  INGRESE_NOMBRE.get_rect(center = ((ANCHO_PANTALLA // 2), 160))


def mostrar_puntos(puntos : int, pj : str, x, y):
    fuente_puntos = pygame.font.SysFont("Arial", 20)
    texto = "Puntos del " + pj + " " + str(puntos)
    PUNTOS = fuente_puntos.render(texto, True, BLANCO)
    PUNTOS_RECT = PUNTOS.get_rect(center = (x, y))
    
    return PUNTOS, PUNTOS_RECT

