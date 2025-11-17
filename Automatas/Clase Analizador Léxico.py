import re

class Token:
    def __init__(self, tipo, valor, linea):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea

    def __repr__(self):
        return f"Token({self.tipo!r}, {self.valor!r}, linea={self.linea})"
    
class Token:
    def __init__(self, tipo, valor, linea):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea

    # Muestra los tokens en texto legible (en lugar de objetos con direcciones)
    def __str__(self):
        return f"Tipo: {self.tipo:12} | Valor: {self.valor:10} | Línea: {self.linea}"

class AnalizadorLexico:
    def __init__(self, codigo):
        self.codigo = codigo
        self.pos = 0
        self.linea = 1

        # Especificación de tokens (el orden importa)
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
                tokens.append(Token('ERROR', self.codigo[self.pos], self.linea))
                self.pos += 1

        return tokens
