# Definición del autómata finito determinista (AFD)
afd = {

    # Definición de los estados
    "estados": {"Q0", "Q1", "Q2", "Q3", "Q4"},

    # Definición del alfabeto
    "alfabeto": {"a", "b"},

    # Definición de las transiciones
    "transiciones": {
        "Q0": {'a': "Q4", 'b': "Q1"},
        "Q1": {'a': "Q2", 'b': "Q3"},
        "Q2": {'a': "Q0", 'b': "Q0"},
        "Q3": {'a': "Q0", 'b': "Q0"},
        "Q4": {'a': "Q2", 'b': "Q3"},

    },

    # Estado inicial y de aceptación
    "estado_inicial": "Q0",
    "estados_aceptacion": {"Q0"},
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