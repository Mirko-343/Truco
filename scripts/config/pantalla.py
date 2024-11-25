import pygame
from .texto import *
from .colores import *

pygame.init()

# Configuraciones iniciales de la pantalla
ALTO_PANTALLA = 540
ANCHO_PANTALLA = 960

VENTANA_PRINCIPAL = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))


# Botones

fuente_botones = pygame.font.SysFont("microsoftyibaiti", 40)

BOTON_JUGAR = fuente_botones.render("Jugar", True, BLANCO)
BTN_JUGAR_RECT = pygame.Rect(420, 414, 80, 40)

