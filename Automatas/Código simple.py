import re

class AnalizadorLexico:
    def __init__(self, codigo):
        self.codigo = codigo

    def tokenizar(self):
        token_spec = [
            ('NUMBER',      r'\d+'),
            ('ID',          r'[A-Za-z_]\w*'),
            ('ASSIGN',      r'='),
            ('SEMICOLON',   r';'),
            ('SKIP',        r'[ \t]+'),
            ('MISMATCH',    r'.'),
        ]
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_spec)
        tokens = []
        for mo in re.finditer(tok_regex, self.codigo):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'NUMBER':
                tokens.append(('NUMBER', value))
            elif kind == 'ID':
                tokens.append(('ID', value))
            elif kind == 'ASSIGN':
                tokens.append(('ASSIGN', value))
            elif kind == 'SEMICOLON':
                tokens.append(('SEMICOLON', value))
            elif kind == 'SKIP':
                continue
            else:
                raise SyntaxError(f'Caracter inesperado: {value!r}')
        return tokens

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
