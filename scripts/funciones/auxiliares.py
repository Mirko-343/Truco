import os
import pygame
import csv

def inicializar_matriz(cantidad_filas : int, cantidad_columnas : int, valor_inicial : any) -> list:
    ''' Inicializa una matriz. Parámetros:
        1. Cantidad de filas
        2. Cantidad de columnas
        3. Valor inical
        Devuelve la matriz inicializada y con los valores iniciales cargados'''

    matriz = []
    
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]
    
    return matriz

def recorrer_matriz(matriz):
    ''' Permite recorrer una matriz. Recibe como parámetro la matriz a recorrer '''
    
    for i in range(len(matriz)): 
        for j in range(len(matriz[i])):
            print(f"\nFila {i} columna {j}: {matriz[i][j]}")     

def generar_listado_cartas(ruta_archivo : str, ruta_imagenes : str) -> None:
    
    ''' Genera una lista de diccionarios donde cada diccionario es una carta y continen la información de la misma.
        Las Key son:
        1. Numero
        2. Palo
        3. Orden (de valor en el juego)
        4. Orden envido
        5. Ruta foto (ruta de la imagen correspondiente a esa carta)
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
                               "Orden" : int(valores[2]),
                               "Orden envido" : int(valores[3]),
                               "Ruta foto": ruta_foto}
                
                lista_cartas.append(nueva_carta)
                
    return(lista_cartas)
             
def cargar_imagen(nombre_imagen : str, ruta_imagen : str, posicion : tuple) -> pygame.Surface | pygame.Rect:
    
    ''' Realiza los pasos necesarios para cargar una imagen y manipular su posición a través del rect asociado. Parámetros:
        1. Nombre de la imagen
        2. Ruta de la imagen
        3. Posición deseada en pantalla 
        Devuelve una Surface con la imagen y el Rect asociado a la misma. '''

    rect = "hit_box_" + nombre_imagen
    
    nombre_imagen = pygame.image.load(ruta_imagen) # Cargo la imagen
    rect = nombre_imagen.get_rect() # Obtengo el rectángulo asociado a la imágen
    rect.center = ((posicion)) # Defino la posición de la imagen en la pantalla a través de la posición del rect
    
    return nombre_imagen, rect

def crear_boton(fuente : str, font_size : float, ancho : int, alto : int, texto : str, color_texto : tuple,
                x : int, y : int) -> pygame.Rect:
    
    ''' Permite crear un botón. Parámetros
        1. Fuente que se desea usar en el texto del botón
        2. Tamaño de la fuente
        3. y 4. Ancho y alto del botón respectivamente
        5. El texto que tiene que contener el botón
        6. El color del texto dentro del botón
        7. y 8. Las coordenadas (x ; y) respectivamente del botón en pantalla
        Como primer valor devuelve el texto y segundo devuelve el rect asociado '''

    font = pygame.font.SysFont(fuente, font_size)
    # button_surface = pygame.Surface(ancho, alto)
    text = font.render(texto, True, color_texto)
    button_rect = pygame.Rect(x, y, ancho, alto)
    
    return text, button_rect

def mostrar_boton(superficie : pygame.Surface, color_boton : tuple, button_surface : pygame.Surface, button_rect : pygame.Rect) -> None:
    
    ''' Función que realiza las acciones necesarias para mostrar un botón ya creado en pantalla. Parámetros:
        1. Superficie donde se va a mostrar el botón
        2. Color deseado para el botón
        3. La superficie del botón
        4. El rectángulo asociado al botón '''
        
    pygame.draw.rect(superficie, color_boton, button_rect)
    superficie.blit(button_surface, button_rect)
    
def actualizar_registros(nombre_jugador: str, victoria: bool, derrota: bool):
    
    ''' Función que permite actualizar los registros donde se guardan los datos de cada jugador. Si encuentra un registro con
        el mismo nombre lo actualiza, si no existe crea uno. Parámetros:
        1. El nombre del jugador para el cual se quiere actualizar / crear un registro
        2. Un bool que indique si la partida terminó en victoria
        3. Un bool que indique si la partida terminó en derrota
        No devuelve nada. Únicamente actualiza el archvio '''

    registro_actualizado = False
    registros = []

    # Leer y actualizar los registros
    with open("./media/registros/registros.csv", "r") as archivo:
        registro = csv.reader(archivo)
        for line in registro:
            if line[0] == nombre_jugador: # Si se encuentra un registro con el mismo nombre
                print("Se encontró un registro con el mismo nombre")
                if victoria:
                    victorias = int(line[1])
                    victorias += 1
                    line[1] = str(victorias)
                    registro_actualizado = True
                    print("Registro actualizado por victoria")
                elif derrota:
                    derrotas = int(line[2])
                    derrotas += 1
                    line[2] = str(derrotas)
                    registro_actualizado = True
                    print("Registro actualizado por derrota")
            registros.append(line)

    # Si no se encontró un registro con el mismo nombre, agregar un nuevo registro
    if not registro_actualizado:
        print("No se encontró un registro con el mismo nombre")
        if victoria:
            registros.append([nombre_jugador, "1", "0"])
        elif derrota:
            registros.append([nombre_jugador, "0", "1"])

    # Sobrescribir el archivo con los nuevos registros
    with open("./media/registros/registros.csv", "w", newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(registros)

def ordenar_cartas(lista_cartas : list) -> list:
    
    cartas_ordenadas = sorted(lista_cartas, key = lambda carta : carta["Orden"])
    
