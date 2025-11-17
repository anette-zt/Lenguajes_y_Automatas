import re

# =========================
# Clase Token
# =========================
class Token:
    def __init__(self, tipo, valor, linea):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea

    # Para mostrar los tokens de forma legible
    def __str__(self):
        return f"Tipo: {self.tipo:12} | Valor: {self.valor:10} | Línea: {self.linea}"


# =========================
# Clase Analizador Léxico
# =========================
class AnalizadorLexico:
    def __init__(self, codigo):
        self.codigo = codigo
        self.pos = 0
        self.linea = 1

        # --- Especificación de tokens ---
        # Puedes agregar más si lo deseas
        self.patrones = [
            ('KEYWORD', r'\b(if|else|while|for|return|int|float|void|main)\b'),
            ('IDENTIFIER', r'[a-zA-Z_]\w*'),
            ('NUMBER', r'\d+(\.\d+)?'),
            ('OPERATOR', r'==|<=|>=|!=|[+\-*/=<>]'),
            ('DELIMITER', r'[;:,(){}]'),
            ('WHITESPACE', r'[ \t]+'),
            ('NEWLINE', r'\n'),
            ('ERROR', r'.'),
        ]

    # =========================
    # Método para tokenizar
    # =========================
    def tokenizar(self):
        tokens = []

        while self.pos < len(self.codigo):
            encontrado = False

            for tipo, patron in self.patrones:
                regex = re.compile(patron)
                match = regex.match(self.codigo, self.pos)

                if match:
                    valor = match.group(0)

                    if tipo == 'NEWLINE':
                        self.linea += 1
                    elif tipo != 'WHITESPACE':
                        tokens.append(Token(tipo, valor, self.linea))

                    self.pos = match.end()
                    encontrado = True
                    break

            if not encontrado:
                # En caso de error (carácter no reconocido)
                tokens.append(Token('ERROR', self.codigo[self.pos], self.linea))
                self.pos += 1

        return tokens


# =========================
# Ejemplo 1: Código simple
# =========================
print("-" * 50)
print("EJEMPLO 1: Código simple")
print("-" * 50)

codigo1 = "int x = 10;"
lexer1 = AnalizadorLexico(codigo1)
tokens1 = lexer1.tokenizar()

print(f"\nCódigo fuente: {codigo1}")
print("\nTokens generados:")
for token in tokens1:
    print(token)


# =========================
# Ejemplo 2: Declaración con operaciones
# =========================
print("\n" + "-" * 50)
print("EJEMPLO 2: Declaración con operaciones")
print("-" * 50)

codigo2 = "float precio = 99.99 + 10;"
lexer2 = AnalizadorLexico(codigo2)
tokens2 = lexer2.tokenizar()

print(f"\nCódigo fuente: {codigo2}")
print("\nTokens generados:")
for token in tokens2:
    print(token)


# =========================
# Ejemplo 3: Estructura de control
# =========================
print("\n" + "-" * 50)
print("EJEMPLO 3: Estructura de control")
print("-" * 50)

codigo3 = """if (x > 5) {
    return x;
}"""
lexer3 = AnalizadorLexico(codigo3)
tokens3 = lexer3.tokenizar()

print(f"\nCódigo fuente:\n{codigo3}")
print("\nTokens generados:")
for token in tokens3:
    print(token)


# =========================
# Ejemplo 4: Múltiples líneas
# =========================
print("\n" + "-" * 50)
print("EJEMPLO 4: Programa completo (múltiples líneas)")
print("-" * 50)

codigo4 = """int suma = 0;
for (i = 1; i < 10; i = i + 1) {
    suma = suma + i;
}
return suma;
"""

lexer4 = AnalizadorLexico(codigo4)
tokens4 = lexer4.tokenizar()

print(f"\nCódigo fuente:\n{codigo4}")
print(f"\nTotal de tokens generados: {len(tokens4)}")
print("Tokens generados:")
for token in tokens4:
    print(token)
