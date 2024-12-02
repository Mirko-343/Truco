import random

def asignar_cartas(listado_cartas) -> list:
    ''' Genera dos listados con 3 cartas (diccionarios) cada uno.
        Como parámetro recibe el listado de diccionarios con la información de todas las cartas
        Devuelve una tupla con las dos listas '''


    cantidad_cartas = 0
    lista_cartas_1 = []
    lista_cartas_2 = []
    

    while cantidad_cartas < 3:
        
        repetida = False
        carta_nueva_1 = random.choice(listado_cartas)
        
        if cantidad_cartas == 0:
            lista_cartas_1.append(carta_nueva_1)
            cantidad_cartas += 1
        else:
            for carta in lista_cartas_1:
                if carta == carta_nueva_1:
                    repetida = True
            if repetida != True:
                lista_cartas_1.append(carta_nueva_1)
                cantidad_cartas += 1

    cantidad_cartas = 0

    while cantidad_cartas < 3:
        
        repetida = False
        carta_nueva_2 = random.choice(listado_cartas)
        
        if cantidad_cartas == 0:
            for carta in lista_cartas_1:
                if carta == carta_nueva_2:
                    repetida = True
            if repetida != True:
                lista_cartas_2.append(carta_nueva_2)
                cantidad_cartas += 1
        else:
            for carta in lista_cartas_2:
                if carta == carta_nueva_2:
                    repetida = True
            for carta in lista_cartas_1:
                if carta == carta_nueva_2:
                    repetida = True
            if repetida != True:
                lista_cartas_2.append(carta_nueva_2)
                cantidad_cartas += 1
        
    return lista_cartas_1, lista_cartas_2

def definir_envido(cartas_asingadas) -> int:
    
    ''' Cacula cuantos puntos tiene de envido a partir de las cartas de una mano.
        Recibe como parámetro una lista con los diccionarios correspondientes a las 3 cartas
        Devuelve un entero con el total de puntos '''

    n = len(cartas_asingadas)
    total_puntos = 0


    for i in range(n):
        intercambio = False
        for j in range(n - i - 1):                     
            if cartas_asingadas[j]["Orden envido"] > cartas_asingadas[j + 1]["Orden envido"]:
                mayor = cartas_asingadas[j + 1]
                cartas_asingadas[j + 1] = cartas_asingadas[j]
                cartas_asingadas[j] = mayor
                intercambio = True                
        if intercambio == False:
            break

    if cartas_asingadas[0]["Palo"] == cartas_asingadas[1]["Palo"]:
        if cartas_asingadas[0]["Orden envido"] == 8:
            total_puntos = 0
        elif cartas_asingadas[1]["Orden envido"] == 8:
            total_puntos += cartas_asingadas[0]["Numero"]
        else:
            total_puntos += cartas_asingadas[0]["Numero"] + cartas_asingadas[1]["Numero"]            
    elif cartas_asingadas[1]["Palo"] == cartas_asingadas[2]["Palo"]:
        if cartas_asingadas[1]["Orden envido"] == 8:
            total_puntos = 0
        elif cartas_asingadas[2]["Orden envido"] == 8:
            total_puntos += cartas_asingadas[1]["Numero"]
        else:
            total_puntos += cartas_asingadas[1]["Numero"] + cartas_asingadas[2]["Numero"]
    elif cartas_asingadas[0]["Palo"] == cartas_asingadas[2]["Palo"]:
        if cartas_asingadas[0]["Orden envido"] == 8:
            total_puntos = 0
        elif cartas_asingadas[2]["Orden envido"] == 8:
            total_puntos += cartas_asingadas[0]["Numero"]
        else:
            total_puntos += cartas_asingadas[0]["Numero"] + cartas_asingadas[2]["Numero"]
    else:
        if cartas_asingadas[0]["Orden envido"] == 8:
            total_puntos = 0           
        else:
            total_puntos += cartas_asingadas[0]["Numero"]
            return total_puntos
          
    total_puntos += 20
    return total_puntos

def verificar_envido(puntos_jugador : int, puntos_rival : int, tipo : str, envido_jugador : int, envido_rival : int, mano : str, 
                     puntos_objetivo : int) -> tuple:
    
    ''' Función que permite asignar los puntos correspondientes al envido dependiendo el tipo y quién ganó.
        Parámetros:
        1. Puntos actuales del jugador
        2. Puntos acutales del rival
        3. El tipo de envido que se está disputando 
        4. El ganador del envido definido anteriormente 
        5. Quien es mano
        6. Los puntos objetivo
        Devuelve una tupla con los puntos del jugador y del rival luego de la asignación de puntos '''
    
    if envido_jugador > envido_rival:
        ganador_envido = "jugador"
    elif envido_jugador < envido_rival:
        ganador_envido = "rival"
    else:
        ganador_envido = "empate"

    if puntos_jugador > puntos_rival:
        mas_puntos = puntos_jugador
    elif puntos_jugador < puntos_rival:
        mas_puntos = puntos_rival
    else:
        mas_puntos = puntos_jugador

    if tipo == "envido":
        puntos = 2
    elif tipo == "real envido":
        puntos = 3
    else:
        puntos = puntos_objetivo - mas_puntos


    if ganador_envido == "jugador":
        puntos_jugador += puntos
    elif ganador_envido == "rival":
        puntos_rival += puntos
    else:
        if mano == 1:
            puntos_jugador += puntos
            ganador_envido = "jugador"
        elif mano == -1:
            puntos_rival += puntos
            ganador_envido = "rival"
    
    return ganador_envido, puntos_jugador, puntos_rival

def definir_mano(carta_jugador : dict, carta_rival : dict, rondas_ganadas_jugador : int, rondas_ganadas_rival : int, empates : int, mano : int):  
    
    ''' Define el ganador de una mano (cuando ambos jugadores ya eligieron sus cartas). Parámetros:
        1. La carta elegida por el jugador
        2. La carta elegida por el rival
        3. La variable que representa las rondas ganadas por el jugador
        4. La variable que representa las rondas ganadas por el rival
        5. La cantidad de rondas que resultaron en empate
        6. Quién es mano
        Devuelve una tupla con tres datos: el ganador de la ronda o de la mano en caso de que corresponda, las rondas ganadas por el jugador y
        las rondas ganadas por el rival '''

    if carta_jugador["Orden"] < carta_rival["Orden"]:
        ganador = "jugador"
        rondas_ganadas_jugador += 1
    elif carta_jugador["Orden"] > carta_rival["Orden"]:
        ganador = "rival"
        rondas_ganadas_rival += 1
    else:
        ganador = "empate"
        empates += 1
        
    if rondas_ganadas_jugador == 2:
        ganador = 1
    elif rondas_ganadas_rival == 2:
        ganador = -1
    elif empates == 2 and rondas_ganadas_jugador == 1:
        ganador = 1
    elif empates == 2 and rondas_ganadas_rival == 1:
        ganador = -1
    elif empates == 1 and rondas_ganadas_jugador == 1 and rondas_ganadas_rival == 1:
        ganador = mano
    elif empates == 3:
        ganador = mano

    return ganador, rondas_ganadas_jugador, rondas_ganadas_rival
        
def verificar_mano(ganador_mano : int, tipo_truco : str, puntos_jugador : int, puntos_rival : int) -> tuple:
    
    ''' Permite asignar los puntos correspondientes al ganador de una mano. Parámetros:
        1. El ganador de la mano
        2. El tipo de truco que se cantó (puede ser igual a None)
        3. Los puntos del jugador
        4. Los puntos del rival
        Devuelve una tupla con los puntos del jugador y del rival actualizados '''

    if tipo_truco == "truco":
        puntos = 2
    elif tipo_truco == "retruco":
        puntos = 3
    elif tipo_truco == "vale cuatro":
        puntos = 4
    else:
        puntos = 1

    if ganador_mano == 1:
        puntos_jugador += puntos
    elif ganador_mano == -1:
        puntos_rival += puntos
        
    return puntos_jugador, puntos_rival

def verificar_vicotria(puntos_jugador : int, puntos_rival : int, puntos_objetivo : int, nombre_jugador):
    
    from .vistas import finalizar_mano

    if puntos_jugador >= puntos_objetivo:
        finalizar_mano(puntos_jugador, puntos_rival, True, False)
        return True
        print("ganaste la partida")
    elif puntos_rival >= puntos_objetivo:
        finalizar_mano(puntos_jugador, puntos_rival, False, True)
        return True
    else:
        return False
    
    



        
        
    