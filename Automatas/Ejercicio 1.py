"""Cadenas que solo contienen los dígitos 0 y 1 y terminan en 0."""

# Definición del autómata finito determinista (AFD)
afd = {

    # Definición de los estados
    "estados": {"Q0", "Q1", "Q2", "Q3"},


    # Definición del alfabeto
    "alfabeto": {"0", "1"},
    "SD": "Símbolo de Desconocido",
    "F": "Estado de Falla",

    # Definición de las transiciones
    "transiciones": {
        "Q0": {'0': "Q1", '1': "Q0"},
        "Q1": {'0': "Q1", '1': "Q2"},
        "Q2": {'0': "Q3", '1': "Q2"},
        "Q3": {'0': "Q3", '1': "Q2"},
    },

    # Estado inicial y de aceptación
    "estado_inicial": "Q0",
    "estados_aceptacion": {"Q3"},
}

# Comprobación de una cadena
def Comprobacion(afd, cadena):
    estado_actual = afd["estado_inicial"]
    for simbolo in cadena:
        # Comprobamos si el símbolo está en el alfabeto
        if simbolo not in afd["alfabeto"]:
            print(f"Símbolo '{simbolo}' no pertenece al alfabeto.")
            return False 

        # Hacemos la transición
        print(f"En estado {estado_actual}, leyendo símbolo '{simbolo}'")
        estado_actual = afd["transiciones"][estado_actual][simbolo]

    # Comprobamos si el estado final es de aceptación
    if estado_actual in afd["estados_aceptacion"]:
        print(f"La cadena '{cadena}' es aceptada, finalizó en estado de aceptación: {estado_actual}.")
        return True
    else:
        print(f"La cadena '{cadena}' no es aceptada, finalizó en estado: {estado_actual}.")
        return False

# Ejemplo de uso
cadena = input("Introduce una cadena: ")
if Comprobacion(afd, cadena):
    print("Cadena aceptada ✅")
else:
    print("Cadena no aceptada ❌")