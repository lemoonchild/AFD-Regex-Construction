# Definición de operadores (se usa para la construcción del árbol)
OPERADORES = {'+', '.', '*'}

class Nodo:
    def __init__(self, valor, izquierdo=None, derecho=None):
        self.valor = valor    # Operador o operando
        self.izquierdo = izquierdo
        self.derecho = derecho

    def __str__(self):
        # Representación sencilla del árbol para depuración
        if self.izquierdo is None and self.derecho is None:
            return self.valor
        elif self.valor == '*':  # Operador unario
            return f"({str(self.izquierdo)}{self.valor})"
        else:  # Operador binario
            return f"({str(self.izquierdo)}{self.valor}{str(self.derecho)})"

def postfix_a_arbol_sintactico(postfix: str) -> Nodo:
    """
    Construye un árbol sintáctico a partir de la expresión en notación postfix.
    
    Para cada símbolo:
      - Si es operando, crea un nodo hoja.
      - Si es operador unario (por ejemplo '*'), extrae un nodo y lo asigna como hijo.
      - Si es operador binario (por ejemplo '.' o '+'), extrae dos nodos 
        (el primero extraído es el hijo derecho y el segundo el izquierdo) y crea un nodo.
    """
    pila = []
    for token in postfix:
        if token.isalnum() or token == '#':
            pila.append(Nodo(token))
        elif token in OPERADORES:
            if token == '*':  # Operador unario
                if not pila:
                    raise ValueError("Error: Operador '*' sin operando.")
                nodo = Nodo(token, izquierdo=pila.pop())
                pila.append(nodo)
            else:  # Operadores binarios: '.' y '+'
                if len(pila) < 2:
                    raise ValueError(f"Error: Operador '{token}' sin suficientes operandos.")
                derecho = pila.pop()
                izquierdo = pila.pop()
                nodo = Nodo(token, izquierdo, derecho)
                pila.append(nodo)
        else:
            raise ValueError(f"Token desconocido en postfix: {token}")

    if len(pila) != 1:
        raise ValueError("Error en la construcción del árbol sintáctico: elementos sobrantes en la pila.")
    return pila[0]
