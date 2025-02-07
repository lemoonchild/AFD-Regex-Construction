from validateRegex import validar_regex
from regexToSY import infix_a_postfix
from syToSyntaxTree import postfix_a_arbol_sintactico, visualizar_arbol_sintactico

def main():
    regex_entrada = input("Ingrese la expresión regular: ")

    # Validación
    if not validar_regex(regex_entrada):
        print("La expresión regular no es válida.")
        return

    # Conversión de infix a postfix (el proceso tokeniza, inserta concatenaciones y aplica Shunting Yard)
    try:
        postfix_tokens = infix_a_postfix(regex_entrada)

    except ValueError as error:
        print("Error al convertir a notación postfix:", error)
        return

    # Construcción del árbol sintáctico a partir de los tokens en postfix
    try:
        arbol_sintactico = postfix_a_arbol_sintactico(postfix_tokens)
        print("Árbol sintáctico construido:")
        print(arbol_sintactico)
    except ValueError as error:
        print("Error al construir el árbol sintáctico:", error)
        return

    # Visualización del árbol con Graphviz (se genera un archivo 'syntax_tree.png')
    try:
        visualizar_arbol_sintactico(arbol_sintactico, "syntax_tree")
        print("Se ha generado y abierto el archivo 'syntax_tree.png' con la visualización del árbol sintáctico.")
    except Exception as e:
        print("Error al generar la visualización con Graphviz:", e)

if __name__ == "__main__":
    main()
