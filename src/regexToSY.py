# Definición de operadores, precedencia y asociatividad para el algoritmo Shunting Yard.
OPERADORES = {'+', '.', '*'}
PRECEDENCIA = {'*': 3, '.': 2, '+': 1}
ASOCIATIVIDAD = {'*': 'right', '.': 'left', '+': 'left'}

def insertar_operador_concatenacion(regex: str) -> str:
    """
    Inserta el operador de concatenación '.' de forma explícita en la expresión regular,
    cuando se omite de forma implícita.
    
    Por ejemplo, transforma "ab(c+d)*" en "a.b.(c+d)*".
    """
    nuevo_regex = ""
    # Conjunto de símbolos considerados como operandos
    operandos = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#")
    for i in range(len(regex)):
        nuevo_regex += regex[i]
        if i + 1 < len(regex):
            actual = regex[i]
            siguiente = regex[i + 1]
            # Si el símbolo actual es un operando, '*' o ')' y el siguiente es un operando o '(',
            # se inserta un operador de concatenación
            if (actual in operandos or actual == '*' or actual == ')') and (siguiente in operandos or siguiente == '('):
                nuevo_regex += '.'
    return nuevo_regex

def infix_a_postfix(regex: str) -> str:
    """
    Convierte una expresión regular en notación infix a notación postfix (RPN)
    usando el algoritmo de Shunting Yard.
    """
    salida = []
    pila = []
    for token in regex:
        if token.isalnum() or token == '#':  # Es un operando
            salida.append(token)
        elif token in OPERADORES:
            # Mientras haya operadores en la pila con mayor o igual precedencia, se extraen
            while pila and pila[-1] in OPERADORES:
                tope = pila[-1]
                if (ASOCIATIVIDAD[token] == 'left' and PRECEDENCIA[token] <= PRECEDENCIA[tope]) or \
                   (ASOCIATIVIDAD[token] == 'right' and PRECEDENCIA[token] < PRECEDENCIA[tope]):
                    salida.append(pila.pop())
                else:
                    break
            pila.append(token)
        elif token == '(':
            pila.append(token)
        elif token == ')':
            # Extrae de la pila hasta encontrar el '('
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            if not pila:
                raise ValueError("Error: Paréntesis no balanceados.")
            pila.pop()  # Elimina el '('
        else:
            raise ValueError(f"Token desconocido: {token}")

    # Vaciar la pila
    while pila:
        if pila[-1] in "()":
            raise ValueError("Error: Paréntesis no balanceados.")
        salida.append(pila.pop())

    return ''.join(salida)
