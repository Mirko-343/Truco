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

def mostrar_puntos(puntos : int, pj : str, x, y):
    fuente_puntos = pygame.font.SysFont("Arial", 20)
    texto = "Puntos del " + pj + " " + str(puntos)
    PUNTOS = fuente_puntos.render(texto, True, BLANCO)
    PUNTOS_RECT = PUNTOS.get_rect(center = (x, y))
    
    return PUNTOS, PUNTOS_RECT

