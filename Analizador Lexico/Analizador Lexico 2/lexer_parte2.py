import re

#  1. CLASE TOKEN  
# Almacena un Token de tipo corto y un tipo de Categoria largo
class Token:
    def __init__(self, tipo_corto, tipo_largo, valor, linea):
        self.tipo_corto = tipo_corto  
        self.tipo_largo = tipo_largo  
        self.valor = valor           
        self.linea = linea

    def __repr__(self):
        # Impresion para depuracion en consola
        return f"Línea {self.linea}: <{self.tipo_corto}, '{self.valor}'> ({self.tipo_largo})"

#  2. CLASE ANALIZADOR LEXICO 
class AnalizadorLexico:
    def __init__(self, codigo):
        self.codigo = codigo
        self.pos = 0
        self.linea = 1
        
        # Especificacion de tokens 
        # Formato: (Tipo Corto, Tipo Largo, Regex)
        self.patrones = [
            ('PR', 'PALABRA_RESERVADA', r'\b(int|float|if|while|for|return)\b'),
            ('ID', 'IDENTIFICADOR', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('NUM', 'NÚMERO', r'\d+\.?\d*'),
            ('MAS', 'OPERADOR_ARITMÉTICO', r'\+'),
            ('MENOS', 'OPERADOR_ARITMÉTICO', r'-'),
            ('MULT', 'OPERADOR_ARITMÉTICO', r'\*'),
            ('DIV', 'OPERADOR_ARITMÉTICO', r'/'),
            ('ASIG', 'OPERADOR_ASIGNACION', r'='),
            ('IGUAL', 'OPERADOR_RELACIONAL', r'=='),
            ('NO_IGUAL', 'OPERADOR_RELACIONAL', r'!='),
            ('MENOR', 'OPERADOR_RELACIONAL', r'<'),
            ('MAYOR', 'OPERADOR_RELACIONAL', r'>'),
            ('MENOR_IG', 'OPERADOR_RELACIONAL', r'<='),
            ('MAYOR_IG', 'OPERADOR_RELACIONAL', r'>='),
            ('PA', 'AGRUPACIÓN', r'\('),
            ('PC', 'AGRUPACIÓN', r'\)'), 
            ('LLA', 'AGRUPACIÓN', r'\{'),
            ('LLC', 'AGRUPACIÓN', r'\}'), 
            ('PUNTOCOMA', 'DELIMITADOR', r';'),
            ('COMA', 'DELIMITADOR', r','),

            ('COMENT', 'COMENTARIO', r'//.*'),
            ('NUEVALINEA', 'NUEVA_LINEA', r'\n'),
            ('ESPACIO', 'ESPACIO_BLANCO', r'[ \t]+'),

            ('ERROR', 'ERROR_LEXICO', r'.')
        ]
        
        # Compilar las expresiones regulares para eficiencia
        self.regex_compilado = []
        for tipo_corto, tipo_largo, patron in self.patrones:
            regex = re.compile(patron)
            self.regex_compilado.append((tipo_corto, tipo_largo, regex))

    def tokenizar(self):
        tokens = []
        while self.pos < len(self.codigo):
            encontrado = False
            for tipo_corto, tipo_largo, regex in self.regex_compilado:
                match = regex.match(self.codigo, self.pos)
                if match:
                    valor = match.group(0)
                    # Crear el token con toda la información
                    token = Token(tipo_corto, tipo_largo, valor, self.linea)
                    tokens.append(token)
                    
                    self.pos = match.end()
                    encontrado = True
                    break
            
            if not encontrado:
                # Si algo falla 
                self.pos += 1
                
        # --- Manejo de tokens post-análisis ---
        # Actualizar líneas y filtrar los tokens que no queremos
        tokens_finales = []
        for token in tokens:
            if token.tipo_corto == 'NUEVALINEA':
                self.linea += 1
            elif token.tipo_corto not in ['ESPACIO', 'COMENT', 'NUEVALINEA']:
                # Re-asignar el número de línea (ahora es correcto)
                token.linea = self.linea 
                tokens_finales.append(token)
                
# Corregir un error comun: el primer token de una línea debe tener el número de línea correcto ANTES de procesar los 'NUEVALINEA'
        self.pos = 0
        self.linea = 1
        tokens_finales = []
        
        while self.pos < len(self.codigo):
            match = None
            for tipo_corto, tipo_largo, regex in self.regex_compilado:
                match = regex.match(self.codigo, self.pos)
                if match:
                    valor = match.group(0)
                    
                    if tipo_corto == 'NUEVALINEA':
                        self.linea += 1
                    elif tipo_corto not in ['ESPACIO', 'COMENT']:
                        # Solo agregar tokens validos a la lista final
                        token = Token(tipo_corto, tipo_largo, valor, self.linea)
                        tokens_finales.append(token)
                    
                    self.pos = match.end()
                    break
            if not match:
                self.pos += 1 # Avanzar si no hay match                
        return tokens_finales


# --- 3. FUNCION PARA GENERAR LA TABLA ---
def generar_tabla_tokens(tokens):
    """
    Toma la lista de tokens y la exporta a un archivo .txt
    con el formato Renglon | Token | Lexema | Categoría
    """
    archivo_salida = "tabla_simbolos.txt"
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            # Escribir el encabezado
            # Usar \t (tabulacion) para separar las columnas
            f.write("Renglón\tToken\tLexema\tCategoría\n")
            
            # Escribir cada token en la tabla
            for token in tokens:
                f.write(f"{token.linea}\t{token.tipo_corto}\t{token.valor}\t{token.tipo_largo}\n")
        
        print(f"¡Exito! Tabla de simbolos generada en: {archivo_salida}")

    except IOError as e:
        print(f"Error al escribir el archivo: {e}")


# --- 4. SCRIPT PRINCIPAL ---
if __name__ == "__main__":
    
    # --- Objetivo 1: Leer desde un archivo ---
    archivo_entrada = "programa.txt"
    
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as file:
            codigo_fuente = file.read()
            
        print(f"--- Leyendo código desde: {archivo_entrada} ---")
        print(codigo_fuente)
        print("------------------------------------------")
        
        # 1. Analizar el codigo
        lexer = AnalizadorLexico(codigo_fuente)
        tokens = lexer.tokenizar()
        
        # 2. Imprimir tokens en consola (para depuracion)
        print("--- Tokens Generados (Consola) ---")
        for token in tokens:
            print(token)
        print("----------------------------------")

        # --- Objetivo 2: Generar la tabla ---
        generar_tabla_tokens(tokens)

    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{archivo_entrada}'")
        print("Por favor, crea un archivo llamado 'programa.txt' con tu codigo fuente.")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")