from funciones import bucle_principal
from funciones import auxiliares

info_cartas = "./media/info_cartas.csv"
ruta_imagenes = "./media/imagenes/cartas"

lista_cartas = auxiliares.generar_listado_cartas(info_cartas,ruta_imagenes)

cartas_jugador, cartas_bot = bucle_principal.asignar_cartas(lista_cartas)

print("Cartas del jugador:")
print(f"{cartas_jugador[0]["Numero"]} de {cartas_jugador[0]["Palo"]}")
print(f"{cartas_jugador[1]["Numero"]} de {cartas_jugador[1]["Palo"]}")
print(f"{cartas_jugador[2]["Numero"]} de {cartas_jugador[2]["Palo"]}")

print("\nCartas del bot:")
print(f"{cartas_bot[0]["Numero"]} de {cartas_bot[0]["Palo"]}")
print(f"{cartas_bot[1]["Numero"]} de {cartas_bot[1]["Palo"]}")
print(f"{cartas_bot[2]["Numero"]} de {cartas_bot[2]["Palo"]}")



envido_jugador = bucle_principal.definir_envido(cartas_jugador)
print(f"\n Total de envido del jugador: {envido_jugador}")

