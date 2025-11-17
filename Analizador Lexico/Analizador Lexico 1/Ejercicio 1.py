import re

# 1. Clase Token 

class Token:
    def __init__(self, tipo, valor, linea):
        self.tipo = tipo
        self.valor = valor
        self.linea = linea

    def __repr__(self):
        """
        (Tarea 4) Modifica la impresión del token para que sea legible
        en lugar de '<__main__.Token object at ...>'.
        """
        return f'<Token tipo={self.tipo:10} valor="{self.valor}" linea={self.linea}>'

# 2. Clase Analizador Léxico 
class AnalizadorLexico:
    def __init__(self, codigo):
        self.codigo = codigo
        self.pos = 0
        self.linea = 1
        
        # Especificación de tokens 
        # Se agregaron OPERATOR y DELIMITER, y se corrigió NUMBER.
        self.patrones_defs = [
            ('KEYWORD',    r'\b(if|while|for|return|int|float)\b'),
            ('OPERATOR',   r'==|!=|<=|>=|=|\+|-|\*|/|<|>'), # Operadores
            ('DELIMITER',  r'[;(){}]'),                     # Delimitadores
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('NUMBER',     r'\d+(\.\d+)?'),                # Corregido para floats
            ('WHITESPACE', r'[ \t]+'),
            ('NEWLINE',    r'\n'),
            ('ERROR',      r'.')                           # Para cualquier otro caracter
        ]
        
        # (Mejora de eficiencia) Compilamos las expresiones regulares una sola vez
        self.patrones = []
        for tipo, patron in self.patrones_defs:
            self.patrones.append((tipo, re.compile(patron)))
        
    def tokenizar(self):
        tokens = []
        while self.pos < len(self.codigo):
            encontrado = False
            for tipo, regex in self.patrones: # Usamos los regex pre-compilados
                match = regex.match(self.codigo, self.pos)
                
                if match:
                    valor = match.group(0)
                    
                    if tipo == 'NEWLINE':
                        self.linea += 1
                    elif tipo not in ['WHITESPACE']: # Ignoramos WHITESPACE
                        # Nota: No ignoramos NEWLINE aquí para poder contarlo,
                        # pero tampoco lo agregamos como token.
                        # Si quisieras agregar NEWLINE como token, quítalo
                        # de la condición 'elif' y añádelo a 'tokens.append'.
                        # Por ahora, solo contamos la línea y no lo añadimos.
                        if tipo != 'NEWLINE':
                             tokens.append(Token(tipo, valor, self.linea))
                    
                    self.pos = match.end()
                    encontrado = True
                    break
            
            if not encontrado:
                # Esto no debería pasar gracias al token 'ERROR'
                print(f"Error léxico irrecuperable en línea {self.linea}")
                self.pos += 1
                
        return tokens

# ----------------------------------------------------------------
# 3. Implementación de los Ejemplos 
# ----------------------------------------------------------------

# --- Ejemplo 1: Código simple ---
print("\n" + "=" * 50)
print("EJEMPLO 1: Código simple")
print("=" * 50)

codigo1 = "int x = 10;"
lexer1 = AnalizadorLexico(codigo1)
tokens1 = lexer1.tokenizar()

print(f"Código fuente:\n{codigo1}")
print("\nTokens generados:")
for token in tokens1:
    print(token)
