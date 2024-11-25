
import os
import pygame

def inicializar_matriz(cantidad_filas : int, cantidad_columnas : int, valor_inicial : any) -> list:
    ''' Inicializa una matriz.
        Primer parámetro: cantidad filas / Segundo parámetro: cantidad columnas
        Tercer parámetro (opcional): valor inicial'''

    matriz = []
    
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    
    return matriz

def recorrer_matriz(matriz):
    for i in range(len(matriz)): 
        for j in range(len(matriz[i])):
            print(f"\nFila {i} columna {j}: {matriz[i][j]}")     

def generar_listado_cartas(ruta_archivo : str, ruta_imagenes : str) -> None:
    ''' Genera una lista de diccionarios donde cada diccionario es una carta y continen la información de la misma.
        Las Key son:
        1- Número
        2- Palo
        3- Orden de valor en el juego
        4- Ruta de la imagen correspondiente.
        Como primer parámetro recibe la ruta del archivo donde se encuentra la información de las cartas. Debe ser un .csv
        Como segundo parámetro recibe la ruta de la carpeta donde están las imágenes de las cartas.'''
    

    lista_cartas = []
    
    with open(ruta_archivo) as archivo:
        for linea in archivo:
            
            linea.strip
            valores = linea.split(",") # Separa cada columna de cada fila en elementos distintos dentro de una lista
            
            if valores[0] != "Numero":
                
                ruta_foto = ruta_imagenes + "/"+ valores[0] + " " + "de" + " " + valores[1] + ".jpg" # Obtiene la ruta de la foto

                nueva_carta = {"Numero" : int(valores[0]),
                               "Palo" : valores[1],
                               "Orden" : valores[2],
                               "Orden envido" : int(valores[3]),
                               "Ruta foto": ruta_foto}
                
                lista_cartas.append(nueva_carta)
                
    return(lista_cartas)
             
def cargar_imagen(nombre_imagen : str, ruta_imagen : str, posicion : tuple) -> pygame.Surface | pygame.Rect:
    ''' Realiza los pasos necesarios para cargar una imagen y manipular su posición a través del rect asociado
        1. Nombre de la imagen
        2. Ruta de la imagen
        3. Posición deseada en pantalla 
        Devuelve una Surface con la imagen y el Rect asociado a la misma '''

    rect = "hit_box_" + nombre_imagen
    
    nombre_imagen = pygame.image.load(ruta_imagen) # Cargo la imagen
    rect = nombre_imagen.get_rect() # Obtengo el rectángulo asociado a la imágen
    rect.center = ((posicion)) # Defino la posición de la imagen en la pantalla a través de la posición del rect
    
    return nombre_imagen, rect

def crear_boton(fuente : str, font_size : float, ancho : int, alto : int, texto : str, color_texto : tuple,
                x : int, y : int) -> pygame.Rect:
    
    font = pygame.font.SysFont(fuente, font_size)
    # button_surface = pygame.Surface(ancho, alto)
    text = font.render(texto, True, color_texto)
    button_rect = pygame.Rect(x, y, ancho, alto)
    
    return text, button_rect