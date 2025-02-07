# syToSyntaxTree.py

from graphviz import Digraph
import os
import platform

OPERADORES = {'+', '.', '*'}

class Nodo:
    def __init__(self, valor, izquierdo=None, derecho=None):
        self.valor = valor    # Operador o operando
        self.izquierdo = izquierdo
        self.derecho = derecho

    def __str__(self):
        # Representación sencilla del árbol para depuración.
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

def visualizar_arbol_sintactico(arbol: Nodo, filename="syntax_tree"):
    """
    Genera y visualiza el árbol sintáctico utilizando Graphviz.
    
    - Cada nodo muestra dos líneas: la primera con el símbolo original y la segunda con
      el número (para hojas) o la letra griega (para operadores).
    - La asignación se realiza en postorden (de abajo hacia arriba).
    
    Se genera un archivo (por defecto syntax_tree.png) con la visualización y se abre automáticamente.
    """
    dot = Digraph()
    leaf_counter = [1]     # Contador mutable para hojas (números)
    branch_counter = [0]   # Contador mutable para nodos internos (letras griegas)
    greek_letters = ['α','β','γ','δ','ε','ζ','η','θ','ι','κ','λ','μ','ν','ξ','ο','π','ρ','σ','τ','υ','φ','χ','ψ','ω']

    def add_nodes(node):
        node_id = str(id(node))
        left_id = None
        right_id = None
        # Recorrer primero los hijos (postorden)
        if node.izquierdo is not None:
            left_id = add_nodes(node.izquierdo)
        if node.derecho is not None:
            right_id = add_nodes(node.derecho)
        
        if node.izquierdo is None and node.derecho is None:
            # Nodo hoja: asignar número
            label_sub = str(leaf_counter[0])
            leaf_counter[0] += 1
        else:
            # Nodo interno (operador): asignar letra griega
            if branch_counter[0] < len(greek_letters):
                label_sub = greek_letters[branch_counter[0]]
            else:
                label_sub = "G" + str(branch_counter[0])
            branch_counter[0] += 1

        # Se crea la etiqueta con el símbolo y en la siguiente línea el número/letra
        label = f"{node.valor}\n{label_sub}"
        dot.node(node_id, label)
        
        # Se agregan las aristas hacia los hijos, si existen
        if left_id is not None:
            dot.edge(node_id, left_id)
        if right_id is not None:
            dot.edge(node_id, right_id)
        return node_id

    add_nodes(arbol)
    dot.render(filename, cleanup=True, view=True)
    return dot
