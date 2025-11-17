# Definición del autómata finito determinista (AFD)
afd = {

    # Definición de los estados
    "estados": {"P", "Q", "R"},

    # Definición del alfabeto
    "alfabeto": {"a", "b"},

    # Definición de las transiciones
    "transiciones": {
        "P": {'0': "Q", '1': "P"},
        "Q": {'0': "Q", '1': "R"},
        "R": {'0': "Q", '1': "P"}
    },

    # Estado inicial y de aceptación
    "estado_inicial": "P",
    "estados_aceptacion": {"R"},
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