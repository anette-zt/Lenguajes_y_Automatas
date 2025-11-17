class Token:
    def __init__(self, tipo, valor, linea):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea

    # Muestra los tokens en texto legible (en lugar de objetos con direcciones)
    def __str__(self):
        return f"Tipo: {self.tipo:12} | Valor: {self.valor:10} | Línea: {self.linea}"
